import pandas as pd
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'
user=pd.read_csv(url,sep="|",index_col="user_id")
user
user.head(10)
user.tail(10)

user1=pd.read_csv(url,sep="|")
user1["user_id"].astype("object").nunique()
user.columns.nunique()
user.columns
user.index
user.info()
user["occupation"]
user["occupation"].nunique()
user["occupation"].mode()
user.info()
user.describe(include="all")
user["occupation"].value_counts()
user["age"].mean()
user["age"].min()