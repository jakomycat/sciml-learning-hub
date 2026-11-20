# SciML Learning Hub

Personal repository where I study **Scientific Machine Learning (SciML)**. Everything here is a learning exercise. The goal is to understand the methods by implementing them myself, not to build a library or reach state-of-the-art results.

## `papers/`

For each paper, I read it and then reproduce or implement a small experiment based on it. Each experiment is a reduced version of something in the paper, not a full reproduction of all its results.

Each folder is named `<year>_<first-author>_<topic>` and contains:

- one or more **notebooks** (`.ipynb`) with the theory, the experiment and the results;
- a **`src/`** folder with the code the notebooks use (model, data generation, physics/residuals).

| Folder | Paper | What is implemented | Status |
|---|---|---|---|
| [`2019_raissi_pinns`](papers/2019_raissi_pinns) | Raissi, Perdikaris & Karniadakis (2019). *Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations.* [J. Comput. Phys. 378](https://doi.org/10.1016/j.jcp.2018.10.045) | Continuous-time PINN solving the 1D Burgers equation; data-driven discovery of the KdV equation coefficients from noisy data | Done |
| [`2021_lu_deeponet`](papers/2021_lu_deeponet) | Lu, Jin, Pang, Zhang & Karniadakis (2021). *Learning nonlinear operators via DeepONet based on the universal approximation theorem of operators.* [Nat. Mach. Intell. 3](https://doi.org/10.1038/s42256-021-00302-5) | DeepONet learning the solution operator $u_0 \mapsto u(x, t)$ of the 1D heat equation | Done |
| [`2021_li_fno`](papers/2021_li_fno) | Li et al. (2021). *Fourier Neural Operator for Parametric Partial Differential Equations.* [ICLR 2021](https://arxiv.org/abs/2010.08895) | 2D Fourier Neural Operator architecture | In progress |