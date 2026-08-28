"""Week 1: spectra & norms of a random matrix vs. a conv-like matrix.

Shows why operator-norm analysis is tractable and where conv structure changes it.
Run: python code/01_spectra.py
"""
import numpy as np

rng = np.random.default_rng(0)
n = 256

# Dense Gaussian matrix: singular values span a Marcenko-Pastur-ish bulk.
A = rng.standard_normal((n, n)) / np.sqrt(n)
sA = np.linalg.svd(A, compute_uv=False)

# A "convolutional" (banded, Toeplitz) matrix: structure concentrates the spectrum.
B = np.zeros((n, n))
for k in range(n):
    B[k, k] = 1.0
    if k > 0: B[k, k - 1] = -0.5
    if k > 1: B[k, k - 2] = 0.25
sB = np.linalg.svd(B, compute_uv=False)

print("dense:  sigma_max=%.3f sigma_min=%.3f cond=%.1f" % (sA.max(), sA.min(),
      sA.max() / max(sA.min(), 1e-12)))
print("conv:   sigma_max=%.3f sigma_min=%.3f cond=%.1f" % (sB.max(), sB.min(),
      sB.max() / max(sB.min(), 1e-12)))
print("=> conv structure can be analyzed locally; dense needs the whole bulk.")