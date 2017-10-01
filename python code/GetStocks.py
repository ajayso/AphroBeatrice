# Function Name: getstockquotesrealime
# Description: This function will be called every 2 mins on a week day
# between 0900 - 1600 HRS IST, The code will do the following
# 1. will get the script code from NSE 
# 2. will get individual prices for the given script_code
# 3. will store the data on Blob storage...
#
import sys
from nsetools import Nse
nse = Nse()
all_stock_codes = nse.get_stock_codes()
all_stock_codes.keys() # Script codes
if 'GREENPOWER' in all_stock_codes:
    del all_stock_codes['GREENPOWER']

for script_code in all_stock_codes:	
   try:
    q = nse.get_quote(script_code);
    print(q);
   except:
    print("Unexpected error:", sys.exc_info()[0]);
   