# Syllabus — Mathematical Foundations of Deep Learning

**Instructor:** Dapeng Lang · **University:** Harbin Engineering University
**Credits:** 3 · **Prereqs:** calculus, linear algebra, probability

## Weeks
1. **Spectra & norms** — operator/Schur norms, spectral radius, why conv layers are cheap to
   inspect; `code/01_spectra.py`.
2. **Gradient flow** — ODE view of GD, learning-rate limits, one-step convergence rates
   (`λ_max/λ_min`); `code/02_flow.py`.
3. **Concentration** — LLN, Hoeffding/Chernoff, why minibatch noise shrinks as 1/√B;
   `code/03_concentration.py`.
4. **Entropy/KL/CE** — cross-entropy as KL + entropy; softmax-grad intuition; `code/04_kl.py`.
5. **Local geometry** — Hessian, flat vs. sharp minima, Fisher information (bridge to the
   research program: vulnerability geometry); `code/05_hessian.py`.

## Assessment
- Weekly reports (numerical) 50% · midterm proof+trial 20% · final portfolio 30%.