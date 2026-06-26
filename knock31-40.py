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
sales_df.describe()

# %%
member_df.describe()

# %%

# %%

# %%
