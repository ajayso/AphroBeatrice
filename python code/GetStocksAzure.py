import os
import json
import sys
import platform
import six
import nsetools
import csv
import AppendBlobService

# Read the scripts for Auto
my_file = open("auto.csv", 'r')
reader = csv.reader(my_file, delimiter='\t')
all_stock_codes = list(reader)
from nsetools import Nse
nse = Nse()
all_stock_codes = nse.get_stock_codes()  # Replace script code with Auto
all_stock_codes.keys() # Script codes

outputlist = list(1000)
for script_code in all_stock_codes:	
   try:
    #q = nse.get_quote(script_code);
    #print(q);
    # Write to a list 
   except:
    print("Unexpected error:", sys.exc_info()[0]);
#Write Outputlist back to Azure Blob Storage
from azure.storage.blob import AppendBlobService
append_blob_service = AppendBlobService(account_name='aphrostock', account_key='cwAlI7P6WfUqijt0jMP+0CCqM54hmoHRofxqdj9PqPamtIfdm9vRUpC+jrpRv/Idma61sSg7NDIvFwkyhMm7KQ==')

append_blob_service.append_blob_from_text('stockdata', '02102017', outputlist)

append_blob = append_blob_service.get_blob_to_text('mycontainer', 'myappendblob')
response.close()