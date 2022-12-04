import sqlite3
import pandas as pd
import random
#from pandas import IntegrityError
conn = sqlite3.connect('./A3Small.db')
c=conn.cursor()

c.execute('PRAGMA foreign_keys=ON;')
n = 112650 #number of records in file
s = 2000 #desired sample size
col_list=['order_id','order_item_id','product_id','seller_id']
filename = "olist_order_items_dataset.csv"
skip =  sorted(random.sample(range(1,n+1),n-s))
db = pd.read_csv(filename,skiprows = skip, usecols=col_list)
for i in range(len(db)):
    try:
        db.iloc[i:i+1].to_sql('Order_items', conn, if_exists='append', index = False)
    except:
        pass
#db.to_sql('Order_items', conn, if_exists='append', index = False)


#rows = c.fetchone()
#print(rows[0])
conn.commit()
