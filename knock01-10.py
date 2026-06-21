# %%
import pandas as pd
import matplotlib.pyplot as plt

sales_df = pd.read_csv("Sales_Data.csv")
member_df = pd.read_csv("Member_Data.csv")

# %%
sales_df.head()
# %%
member_df.tail()
# %%
#取引データのカラムの件数や型を確認
sales_df.info()
# %%
member_df.info()
# %%
#質的変数に型変換
sales_df['Transaction_ID'] = sales_df["Transaction_ID"].astype('string')
sales_df['Member_ID'] = sales_df["Member_ID"].astype('string')
sales_df['Product_ID'] = sales_df["Product_ID"].astype('string')
sales_df['Store_ID'] = sales_df["Store_ID"].astype('string')

member_df['Member_ID'] = member_df['Member_ID'].astype('string')
# %%
6. #日付データをdatetime型に変換してください
sales_df['Transaction_Date'] = pd.to_datetime(sales_df['Transaction_Date'])
sales_df.info()
# %%
# 7. 取引データの各列の基本的な統計情報（平均、標準偏差など）を表示してください
sales_df.describe()


# %%
# 8. カラム名の変更
# - データフレームのAmountのカラム名をSales_Amountに変更してください
# - データフレームは上書きしないでください
# sales_df['Amount'].rename('Sales_Amount')
sales_df.rename(columns={"Amount":"Sales_Amount"})

# %%

# %%

# %%

# %%

# %%
