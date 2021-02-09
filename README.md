# GrabeRotationFall
Repo of Scripts and structures for Kevin Fall rotation.

Index:
1. Reproduce Paola's and Kevin's Data
2. Using PerRes.py
3. Zero Charge Mutants
4. Alanine Mutants
5. Reproducing 



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

**3. Zero Charge Mutants**
1. To reproduce the Zero charge mutations on slide 5, simply directly edit the PQR filees and change the residue you want to have zero charge (second to last column is the charge). make sure the number of digits do not change.
2. Run the calculation and reuse vSGLT_gc_04a.

**4. Alanine Mutants**
1. To reproduce alanine mutants on slide 5, use MODELLER python module with select.mutation function, I added the alanine pqr files I used in AlanineMut.
2. Run the calculation and reuse vSGLT_gc_04a.

**5. Reproducing Machtens Et al. Data- Kv and VSP**
1. To reproduce the data on slide 6:
2. Grab the Kv1.2 PQR structures and load them in along with the parameters KV1.2_gc_02.solv.in
3. Run the calculation.
4. Use PerRes.py to generate the per-residue gating charge graph, comparison graph taken from Macthens et al.
5. Grab the VSP pqr files and load them in along with the parameters VSP_gc_01.solv.in
6. Run the calculation.
7. Use PerRes.py to generate the per-residue gating charge graph, comparison graph was taken from Machtens et al.

**6. Reproducing Machtens et al. Data- Gltp**
1. To reproduce  data on slide 7:
2. I went into the PQRs and manually deleted chains to single out different monomers out of the trimers and run the calculation.
3. The parameters used was Gltp_gc_08.solv.in for each monomer.

**7. Using PQRDiff.py**
1. I found this script to be rather useful for sanity checking and making sure PQR files don't have different charges.
2. Run the script with "python PQRDiff.py" making sure both PQR files you are trying to compare are in the same directory where you are.
3. Input the exact names of the pqr files when prompted.
4. It will first generate a graph showing any peaking which shows differences. A flat line indicates no differences.
5. Exiting out of the graph lets you see specifically which residues have a charge difference.
