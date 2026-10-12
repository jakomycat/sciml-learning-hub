import torch.nn as nn
import torch

class SpectralConv2d(nn.Module):
    def __init__(self, in_channels, out_channels, modes1, modes2):
        super().__init__()
        self.weights1 = nn.Parameter(
            1 / (in_channels*out_channels) * torch.rand((in_channels, out_channels, modes1, modes2), dtype=torch.cfloat)
            )
        self.weights2 = nn.Parameter(
            1 / (in_channels*out_channels) * torch.rand((in_channels, out_channels, modes1, modes2), dtype=torch.cfloat)
        )
        
        self.m1 = modes1
        self.m2 = modes2
        
        self.in_channels = in_channels
        self.out_channels = out_channels
        
    def compl_mul2d(self, inp, weights):
        """Args:
            inp: (B, C_in, modk1, modk2)
            weights: (C_in, C_out, modk1, modk2)
        """
        out = torch.einsum("bixy, ioxy -> boxy", inp, weights)
        
        return out
        
    def forward(self, x):
        """Args:
            x: this has shape (B, C_in, H, W)
        """
        B, C, H, W = x.shape
        
        t_fourier = torch.fft.rfft2(x) # dim: (B, C_in, H, W//2 + 1)
        
        out_ft = torch.zeros( # this has the same shape than t_fourier
            (B, self.out_channels, H, W//2 + 1),
            dtype=torch.cfloat,
            device=x.device
            )
        
        # Corners
        out_ft[:, :, :self.m1, :self.m2] = self.compl_mul2d(
            t_fourier[:, :, :self.m1, :self.m2],
            self.weights1
            )
        
        out_ft[:, :, -self.m1:, :self.m2] = self.compl_mul2d(
            t_fourier[:, :, -self.m1:, :self.m2],
            self.weights2
            )
        
        return torch.fft.irfft2(out_ft, s=(H,W))