from common_file_ops.readFiles import *

# out = readTabular(path = "./data/nextclade.tsv",
#             fields = ["qc.overallStatus","totalSubstitutions"],
#             ids = {'index': [1,2,14,66,67], 'Nextclade_pango': ["JN.1","B.1.1.7"], 'boooo':[5]})

# out = readJSON(path = "./data/report_ONT.json",
#             fields=[{'protocol_run_info' : {'device' : 'device_type'}},{'protocol_run_info' : {'device' : 'device_type'}}]
#             )#ids = {'index': [1,2,14,66,67], 'Nextclade_pango': ["JN.1","B.1.1.7"], 'boooo':[5]})



out = readXML(path = "./data/RunParameters.xml",
            fields={'RunParameters' : 'ComputerName'})

print(out)