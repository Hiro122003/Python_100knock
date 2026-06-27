# %%
import pandas as pd

# %%
sales_df = pd.read_csv("Sales_Data.csv")
member_df = pd.read_csv("Member_Data.csv")

# %%
# 5質的変数に型変換
sales_df["Transaction_ID"] = sales_df["Transaction_ID"].astype("string")
sales_df["Member_ID"] = sales_df["Member_ID"].astype("string")
sales_df["Product_ID"] = sales_df["Product_ID"].astype("string")
sales_df["Store_ID"] = sales_df["Store_ID"].astype("string")

member_df["Member_ID"] = member_df["Member_ID"].astype("string")

# %%
sales_df["Transaction_Date"] = pd.to_datetime(sales_df["Transaction_Date"])

# %%
# sales_df.describe()
sales_df.info()

# %%
# member_df.describe()
member_df.info()

# %%
# 売上データと会員データを結合しmerged_dfとして定義してください
merge_df = pd.merge(sales_df,member_df,on='Member_ID',how='left')
merge_df


# %%
# 41. 性別と店舗IDごとに取引数を集計してください
merge_df.groupby(['Gender','Store_ID'])['Transaction_ID'].count()



# %%

# 42. Store_ID が [1, 5, 9] の取引を抽出し、Store_ID ごとに Quantity の合計を計算してください
filtered_store_id = merge_df[merge_df['Store_ID'].isin(['1','5','9'])]
filtered_store_id.head()
filtered_store_id.groupby('Store_ID')['Quantity'].sum()


# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%
