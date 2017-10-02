import os
import json
import sys
import nsetools
import pandas
import datetime

import pandas as pd
input = pd.read_csv("auto.csv");
# input.Symbol[i] input.Series.size
from nsetools import Nse
nse = Nse()
outputlist = []
for script_code in all_stock_codes:	
        try:
                print(script_code)
                q = nse.get_quote(script_code);
                outputlist.append(q)
                print(q);
    # Write to a list 
        except:
                print("Unexpected error:", sys.exc_info()[0]);
#Write Outputlist back to Azure Blob Storage
jsonObject = json.dumps(outputlist)
from azure.storage.blob import AppendBlobService
append_blob_service = AppendBlobService(account_name='aphrostock', account_key='cwAlI7P6WfUqijt0jMP+0CCqM54hmoHRofxqdj9PqPamtIfdm9vRUpC+jrpRv/Idma61sSg7NDIvFwkyhMm7KQ==')
containerName = str(datetime.datetime.now())
append_blob_service.create_blob('stockdata', containerName)
append_blob_service.append_blob_from_text('stockdata', containerName, jsonObject)


response.close()
