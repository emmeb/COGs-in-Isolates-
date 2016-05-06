
FINDING COGS: 
The purpose of this project is to determine similar and unique genes among microbial genomes.

Installation: 
To run Finding Cog, you will need: 
Software Requirements:
Linux or Mac OS
Python 2.7
Anaconda
Blast-2.3.0+
BioPython 
Scripts: 
findingCOGs.py
Input Files: 
3 complete genomes downloaded from NCBI in .faa format 
a local blast database for each genome
query.txt
database.txt

When the package Anaconda is downloaded, install Matplotlib, Numpy, Scipy, Venn3 on desired IDE. If using pycharm, click “file -> settings -> project interpreter -> “+” -> find desirable programs from list -> install. Ensure that all packages are located in the correct file path.
All scripts and sample input files can be found on: https://github.com/emmeb/COGs-in-Isolates-.git

Usage: 
Sample data is included in the github repository. If you wish to use your own data, you will need:
3 complete genomes downloaded from NCBI in .faa format 
a local blast database for each genome created using terminal. 
In command line, type: “-makeblastdb –in “NC_00000.faa” –out “NC_00000db” –dbtype prot –hash_index”
a query.txt which is a list of query files
NC_014248.faa,NC_014614.faa,NC_015671.faa
a database.txt which is a list of database files.
NC_014248db,NC_014614db,NC_015671db 
Ensure the list of file names in both documents are in   the same order. 
In the system argument specify your query file, database file, percent identity and query coverage in this order. Percent identity and query coverage must be written to the tenth decimal place. 

If using test data, the query file is “query.txt” and database file, “database.txt” 

Contributing: 
If you wish to contribute: 
Fork it
Create your feature branch
“git checkout -b “my-new-feature””
Commit your changes
“git commit -am “Add some feature””
Push to the branch
“git push origin “my-new-feature””
Submit a pull request 


History: 
This project was part of Computational Biology at Loyola University Chicago. 

Credits:
Acknowledgments to: Dr Putonti, Dr Wheeler and Jon Brenner. 
Data downloaded from: NCBI  
Thanks to the creators of: Python, Biopython, BLAST 2.3.0+, Anaconda, Pycharm. 
