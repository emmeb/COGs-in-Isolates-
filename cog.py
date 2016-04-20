import os
q = open ("query.txt", "r")
d = open ("database.txt", "r")
g = open ("genecount.txt", "w")
##n = open ("nonuniqueseq.txt","w")
per_iden = input ("What would you like to set your percent identity threshold at?")
qcov = input ("What would you like to set your query coverage threshold at?")
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
i = 0
j = 0 
for i in range(len(databases)):
    for j in range (len(queries)):
        query = queries[j]
        database = databases[i]
        if i == j:
            print("These files are the same and it is not necessary to BLAST them against each other") 
        else:
            print "Currently blasting " + query + " against " + database + "..."
            os.system ('blastp -task blastp-short -query ' + query + ' -db ' + database + ' -out ' + query + database + '.xml -outfmt "5" ')
            from Bio import SeqIO
            filelist = []
            original = 0
            for record in SeqIO.parse(query, "fasta"):
                filelist.append(record.id)
                original = original + 1
            g.write("Total number of genes in " + query + " is " + str(original) + "\n")
            match = 0
            result_handle = open(query+database+ '.xml')
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
                            match = match + 1
                            unique = original-match
            g.write("The number of genes from " + query + " found in " + database + " is " + str(match) + "\n")
            g.write("Unique genes in " + query + " is " + str(unique) + "\n")
        j = j + 1
    i = i + 1        

g.close()
q.close()
d.close()
