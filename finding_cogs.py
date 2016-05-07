import os
from Bio import SeqIO
q = open ('query.txt', "r")
d = open ('database.txt', "r")
per_iden = input("What would you like the percent identity threshold at: ")
qcov = input("What would you like the query coverage threshold at: ")
queries = []
databases = []
outputs = []
for line in q:
    queries = line.strip('\n').split(",")
print queries
for line in d:
    databases = line.strip('\n').split(",")
print databases
unique = 0

####Create total lists for each genome##
genomeA = []
genomeB = []
genomeC = []
for record in SeqIO.parse(queries[0], "fasta"):
    genomeA.append(record)
for record in SeqIO.parse(queries[1], "fasta"):
    genomeB.append(record)
for record in SeqIO.parse(queries[2], "fasta"):
    genomeC.append(record)

array = [0,0]

def Compare_genomes (query, database,array):

    print "Currently blasting " + query + " against " + database + "..."
    os.system ('blastp -task blastp-short -query ' + query + ' -db ' + database + ' -out ' + query + database + '.xml -outfmt "5" ')
    match = 0
    result_handle = open(query+database+ '.xml')
    matchlistquery = []
    matchlistdb = []
    from Bio.Blast import NCBIXML
    blast_records = NCBIXML.parse(result_handle)
    for blast_record in blast_records:
        percent_identity_thresh = per_iden
        query_cov_thresh = qcov
        for alignment in blast_record.alignments:
            for hsp in alignment.hsps:
                percent_identity = (100.0 * hsp.identities) / hsp.align_length
                query_cov = ((float(hsp.align_length)/float(blast_record.query_length))*100)
                if percent_identity >= percent_identity_thresh and query_cov>= query_cov_thresh:
                    matchlistquery.append(blast_record.query)
                    ind = alignment.title.index("gi")
                    matchlistdb.append(alignment.title[ind:])
    array[0] = matchlistquery
    array[1] = matchlistdb
    return 0

##Compare AtoB and BtoA
reciprocalAb = []
reciprocalBa = []
if Compare_genomes(queries[0],databases[1],array)== 0:
    A = array[0]
    B = array[1]
array = [0,0]
if Compare_genomes(queries[1],databases[0], array) == 0:
    C = array[1]
    D = array[0]
for item in A:
    if item in C:
        reciprocalAb.append(item)
for item in B:
    if item in D:
        reciprocalBa.append(item)
##Compare AtoC and CtoA
array = [0,0]
reciprocalAc = []
reciprocalCa = []
if Compare_genomes(queries[0],databases[2],array)== 0:
    A = array[0]
    B = array[1]
array = [0,0]
if Compare_genomes(queries[2],databases[0], array) == 0:
    C = array[1]
    D = array[0]
for item in A:
    if item in C:
        reciprocalAc.append(item)
for item in B:
    if item in D:
        reciprocalCa.append(item)
##Compare BtoC and CtoB
reciprocalBc = []
reciprocalCb = []
array = [0,0]
if Compare_genomes(queries[1],databases[2],array)== 0:
    A = array[0]
    B = array[1]
array = [0,0]
if Compare_genomes(queries[2],databases[1], array) == 0:
    C = array[1]
    D = array[0]
for item in A:
    if item in C:
        reciprocalBc.append(item)
for item in B:
    if item in D:
        reciprocalCb.append(item)
matches = []

for item in reciprocalAb:
    if item in reciprocalAc:
        matches.append(item)

matchesB = []
for item in reciprocalBa:
    if item in reciprocalBc:
        matchesB.append(item)
uniquegenomeA = genomeA
for item in reciprocalAb:
    if item in uniquegenomeA:
        uniquegenomeA.remove(item)
for item in reciprocalAc:
    if item in uniquegenomeA:
        uniquegenomeA.remove(item)
for item in matches:
    if item in reciprocalAb and item in reciprocalAc:
        reciprocalAb.remove(item)
        reciprocalAc.remove(item)
uniquegenomeB = genomeB
for item in reciprocalBa:
    if item in uniquegenomeB:
        uniquegenomeB.remove(item)
for item in reciprocalBc:
    if item in uniquegenomeB:
        uniquegenomeB.remove(item)
for item in matchesB:
    if item in reciprocalBc:
        reciprocalBc.remove(item)

uniquegenomeC = genomeC
for item in reciprocalCa:
    if item in uniquegenomeC:
        uniquegenomeC.remove(item)
for item in reciprocalCb:
    if item in uniquegenomeC:
        uniquegenomeC.remove(item)

print "Making FASTA files..."
##create all fasta files##
my_records = []
for seq in genomeA:
    for item in matches:
        if item == seq.description:
            my_records.append(seq)
SeqIO.write(my_records, "match" + queries[0] + queries[1] + queries[2] + ".faa", "fasta")
my_records = []
for seq in genomeA:
    for item in reciprocalAb:
        if item == seq.description:
            my_records.append(seq)
SeqIO.write(my_records, "match" + queries[0] + queries[1] + ".faa", "fasta")
my_records = []
for seq in genomeA:
    for item in reciprocalAc:
        if item == seq.description:
            my_records.append(seq)
            if seq in genomeA:
                genomeA.remove(seq)
SeqIO.write(my_records, "match" + queries[0] + queries[2] + ".faa", "fasta")
my_records = []
for seq in genomeB:
    for item in reciprocalBc:
        if item == seq.description:
            my_records.append(seq)
SeqIO.write(my_records, "match" + queries[1] + queries[2] + ".faa", "fasta")
my_records = []
for seq in uniquegenomeA:
            my_records.append(seq)
SeqIO.write(my_records, queries[0] + "unique.faa", "fasta")
my_records = []
for seq in uniquegenomeB:
            my_records.append(seq)
SeqIO.write(my_records, queries[1] + "unique.faa", "fasta")
my_records = []
for seq in uniquegenomeC:
            my_records.append(seq)
SeqIO.write(my_records, queries[2] + "unique.faa", "fasta")
venn = open ("venn.txt", "w")
match = len(matches)/3
recipAb = len(reciprocalAb)/2
recipAc = len(reciprocalAc)/2
recipBc = len(reciprocalBc)/2
uniqueA = len(uniquegenomeA)- match - recipAb - recipAc
uniqueB = len(genomeB) - match - recipAb - recipBc
uniqueC = len(genomeC) - match - recipAc - recipBc
venn.write(str(uniqueA) + ',' + str(uniqueB)+ ',' + str(recipAb) + ',' + str(uniqueC) + ',' + str(recipAc)
           + ',' + str(recipBc)+ ',' + str(match) + '\n')
venn.write(queries[0] + ',' + queries[1] + ',' + queries[2] + '\n')
venn.write("Gene Counts")


q.close()
d.close()
venn.close()

from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles
import numpy as np
num = []
number = []
names = []

print "Making the Venn diagram..."
file = open('venn.txt', 'r+')
num= file.readline().strip('\n').split(',')
names = file.readline().strip('\n').split(',')
test= file.readline().strip('\n').split(',')

for item in num:
    number.append(int(item))


a = number[0]
b = number[1]
c = number[2]
d = number[3]
e = number[4]
f = number[5]
g = number[6]


v = venn3(subsets=(a,b,c,d,e,f,g), set_labels = ('A', 'B', 'C'))
v.get_label_by_id('A').set_text(names[0])
v.get_label_by_id('B').set_text(names[1])
v.get_label_by_id('C').set_text(names[2])
plt.title(test[0])
plt.savefig('gene_counts_random' + '.pdf', dpi = 600, format = 'pdf', bbox_inches = 'tight')
plt.close()
venn.close()
print ("The program has finished running.")