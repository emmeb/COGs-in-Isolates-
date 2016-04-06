from Bio import SeqIO
filelist = []
original = 0
for record in SeqIO.parse("NC_014614.faa", "fasta"):
    filelist.append(record.id)
    original = original + 1
print original
match = 0
result_handle = open("output4.xml")
from Bio.Blast import NCBIXML
blast_records = NCBIXML.parse(result_handle)
for blast_record in blast_records:
    E_VALUE_THRESH = 0.000001
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            if hsp.expect < E_VALUE_THRESH:
                if alignment.title[19:51] in filelist:
                    match = match + 1
print match
