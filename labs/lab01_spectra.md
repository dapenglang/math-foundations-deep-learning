# Lab 01 — Spectra and Conditioning

1. Run `code/01_spectra.py`. In words, why does the dense Gaussian have a *bulk*
   of singular values while the banded matrix varies smoothly?
2. Scale the Gaussian by `c` (try `1, sqrt(n), n`). Report `σ_max/σ_min`. Which choice keeps
   the map contractive (`σ_max < 1`)?
3. Gradient-flow preview: if `f(w)=½wᵀAw` with `A` PSD, the update `w←w−ηAw`
   converges only if `η < 2/λ_max`. Verify with `A` from step 2 in a 20-line loop.

**Deliverable:** short report with numbers and two-sentence explanations.