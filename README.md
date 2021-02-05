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
2. To reproduce the results on slide 1-3:
3. In the APBSmem GUI, load parameters vSGLT_gc_04a.solv.in; make sure to select PQR1 as vSGLT_inward-facing3.pqr and PQR2 as vSGLT_outward-facing3.pqr
7. Run the Calculation by hitting "Run"; Save the results to a folder
8. The slope output after the calculation is done should be -0.59e
9. Use PerRes.py to find the per-residue gating charge.
10. To do the calculations for "Flipped X,Y,Z" use the orient function in APBSmem to rotate BOTH pqr's 180 degrees around one axis. Using this APBSmem function will create new PQR files with an "orient1" tag. I suggest using protein solvation mode in order to do one PQR file at a time.
11. To map the potential maps onto a 3D structure of a protein in Chimera (such as in slides 2,3):
12. Open UCSF Chimera
13. Open either the inward or outward facing pqr file for the protein of interest.
14. Go to Actions>Surface>Show. this will display the protein in a more density-like fashion
15. Go to Tools>Surface/Binding Analysis>Electrostatic surface coloring.
16. Select the potential map which looks like pot_#.dx depending on focus level of the calculation, make sure the potential map is the one that corresponds to the pqr used!
17. The default gradient colors is red, white, and blue. The scale of the potential goes from 0 to 1. I typically select 0 for red, 0.5 for white, and 1 for blue.
18. Hit "Color", this will now assign a color based on the potential at any point in the protein, to see a slice of the protein, use the side view function of Chimera.
19. Save the chimera session in order to have the map readily available.

**2. Using PerRes.py**
1. To reproduce the results on slide 4:
2. Have vSGLT_inward-facing3.pqr, the solv.out of a calculation, and the script ready and in the same folder.
3. I unfortunately never coded an input from the commandline so the script requires inputs in >> .
4. Invoke the script with "python PerRes.py" in the command line
5. When prompted for pdb/pqr, you input the precise name of the pqr file being used, in this case "vSGLT_inward-facing.pqr"
6. When prompted for the solv.out, input the precise name of the solv.out file being used
7. The script will generate a plot of charge-contribution per residue of one monomer (this function gets messed up when there are multiple chains in a pqr/pdb file)
8. Exit the plot to query for specific residues. To find the charge contribution of the aspartate at position 189, use the three letter amino acid code plus the position number (ASP189), spaces need to be added if the residue number is below 100. For example: "ASP 90" or "ASP  9" for the 90th or 9th aspartate.

**3. Zero Charge Mutants

