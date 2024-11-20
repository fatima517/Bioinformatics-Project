from Bio import AlignIO
from Bio.Align import AlignInfo
import os 

#Loading the aligned sequences file 
os.chdir("mafft")
alignment = AlignIO.read("aligned_combined_insulin.fasta", "fasta")

#This is going to give the summary of the alignment
summary_align = AlignInfo.SummaryInfo(alignment)

# The threshold to consider which sequences are similar and its based on 70%
consensus  = summary_align.dumb_consensus(threshold=0.7, ambiguous="N")
print("Consensus sequence:")
print(consensus)

#Save the conserved regions to a file
with open("conserved_regions.txt", "w") as output_file:
	output_file.write(f"Consensus sequence:\n{consensus}\n")

