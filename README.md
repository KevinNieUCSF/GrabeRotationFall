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
3. In the APBSmem GUI change the "Calculation Type" field to "Gating charge"
3. In the field "PQR File 1": Select vSGLT_inward-facing.pqr
4. In the field "PQR File 2": Select vSGLT_outward-facing.pqr
5. With every other field remaining untouched; adjust these parameters accordingly:
5a. Grid Dimension: 97 for each field
5b. Two focus levels (Under the dropdown "Focus" in the top left of the GUI)
5c. Grid Length (cubed; focus level 0 - focus level 1 - focus level 2): 300-200-100
5d. Protein Dielectric: 2.1 (This change is arbitrary but I do it to troubleshoot membrane generation)
5e. Membrane Thickness: 46
5f. Head Group Thickness: 8
5g. Membrane Z-position: -23
5h. Flooding ON
6. Run the Calculation by hitting "Run"; Save the results to a folder
7. The slope output after the calculation is done should be -0.59e
8. Use PerRes.py to find the per-residue gating charge.



**2.Reproduce Gltph**
1. To reproduce the results on slide :
2. In the APBSmem GUI change the "Calculation Type" field to "Gating charge"
3. In the field "PQR File 1": Select vSGLT_inward-facing.pqr
4. In the field "PQR File 2": Select vSGLT_outward-facing.pqr
5. With every other field remaining untouched; adjust these parameters accordingly:
5a. Grid Dimension: 97 for each field
5b. Two focus levels (Under the dropdown "Focus" in the top left of the GUI)
5c. Grid Length (cubed; focus level 0 - focus level 1 - focus level 2): 300-200-100
5d. Protein Dielectric: 2.1 (This change is arbitrary but I do it to troubleshoot membrane generation)
5e. Membrane Thickness: 46
5f. Head Group Thickness: 8
5g. Membrane Z-position: -23
5h. Flooding ON
