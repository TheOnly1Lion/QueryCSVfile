import pandas as pd
import random

col_list=['seller_id','seller_zip_code_prefix']

data = pd.read_csv ('olist_sellers_dataset.csv',usecols=col_list)

df= pd.DataFrame(data)

records = df.to_records(index=False)

result = tuple([entry for entry in tuple(df.values)])
	
print(records)

	
