# Bioinformatics-Project
This is my repository for my bioinformatics project. 

Analysis of Conserved Regions in Insulin Protein Sequences Across Species

The goal of this project is to analyze the insulin protein sequences from various species and identify conserved regions that could be essential for insulin's biological role.

Question: How have insulin protein sequences evolved across different species from a selection of species?


1. Downloaded and retrieved data from NCBI by downloading it to my local computer then scp to the cluster.
2. Combined all the sequences into one file for MAFFT which is in the insulin_project folder. 
3. Ran MAFFT
mafft --auto combined_insulin_sequences.fasta > aligned_combined_insulin.fasta

4. Identified the conserved regions using Biopython, the script is in the insulin_project directory
saved to a combined_text.file in MAFFT directory

5. Used iqtree to create a phylo genetic tree 
iqtree2 -s aligned_combined_insulin.fasta -m AUTO -bb 1000 -nt AUTO
saved in MAFFT directory

7. Used R to visualize the tree
