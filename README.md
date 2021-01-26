# GrabeRotationFall
Repo of Scripts and structures for Kevin Fall rotation.

Index:
1. Reproduce Paola's and Kevin's Data
2. Reproduce Gltph
3. Reproduce Kv1.2
4. Reproduce VSP
5. Using PerRes.py and PQRdiff.py

**I did not do the APBSmem calculations in headless mode.**

Python modules needed:
sys
os
numpy
matplotlib
scipy
collections


**1. Reproducing Paola's and Kevin's Data**
1. Use the latest APBSmem version; APBS 1.5 or 3.0 should both work. MS is not required for gating charge calculation
2. To reproduce the results on slide :
3. In the APBSmem GUI, open vSGLT_gc_04.solv.in
7. Run the Calculation by hitting "Run"; Save the results to a folder
8. The slope output after the calculation is done should be -0.59e
9. Use PerRes.py to find the per-residue gating charge.



**2.Reproduce Gltph**
1. To reproduce the results on slide :
2. In the APBSmem GUI change the "Calculation Type" field to "Gating charge"

