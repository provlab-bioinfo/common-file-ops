from scripts.readFiles import *

out = readTabular(path = "./data/240730_N_I_098_nextclade.tsv",
            fields = ["Nextclade_pango","totalSubstitutions"],
            ids = {'index': [1,2,14,66,67], 'Nextclade_pango': ["JN.1","B.1.1.7"]})

print(out)