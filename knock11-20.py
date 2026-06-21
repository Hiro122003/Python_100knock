# %%
import pandas as pd
import matplotlib.pyplot as plt

sales_df = pd.read_csv("Sales_Data.csv")
member_df = pd.read_csv("Member_Data.csv")
# %%
sales_df.head()
# %%
# 5質的変数に型変換
sales_df["Transaction_ID"] = sales_df["Transaction_ID"].astype("string")
sales_df["Member_ID"] = sales_df["Member_ID"].astype("string")
sales_df["Product_ID"] = sales_df["Product_ID"].astype("string")
sales_df["Store_ID"] = sales_df["Store_ID"].astype("string")

member_df["Member_ID"] = member_df["Member_ID"].astype("string")
# %%
6.0  # 日付データをdatetime型に変換してください
sales_df["Transaction_Date"] = pd.to_datetime(sales_df["Transaction_Date"])
sales_df.info()
# %%
member_df.head()
# %%
sales_df.shape
# %%
# 11. 会員データから30歳から50歳の会員を抽出してください
# member_df.query('Age >= 30 and Age <=50')
member_df.query("30 <= Age <= 50")

# %%
# 12. 取引データから"2024-08-01"以降に行われた取引を抽出してください
sales_df.query('Transaction_Date >= "2024-08-01"')

# %%
# 13. Store_ID が「1」または「3」で、かつ Amount が5000円以上の取引を抽出してください == 3 and Amount >= 5000
sales_df.query("(Store_ID == '1' or Store_ID == '3') and Amount >= 5000")


# %%
member_df.info()
# %%
# 14. Product_ID が「10」、「20」、「30」のいずれかに一致する取引を抽出してください
# sales_df.query("Product_ID == '10' or Product_ID == '20' or Product_ID == '30'")

# 別のやり方
sales_df.query("Product_ID in ['10', '20', '30']")

# %%
# 15. Product_ID が「10」、「20」、「30」ではない取引を抽出してください
# 修正版
# sales_df.query("Product_ID != '10' and Product_ID != '20' and Product_ID != '30'")

sales_df.query("Product_ID not in ['10', '20', '30']")

# %%


# 16. Quantity が最頻値で、かつ Store_ID が「3」の取引を抽出してください
# ① クエリの外で先に最頻値を計算しておく
mode_quantity = sales_df["Quantity"].mode()[0]

# ② @を付けて、Python変数であることを示す
sales_df.query('Quantity == @mode_quantity and Store_ID == "3"')

# %%
# 17. Amount が第1四分位から第3四分位の範囲に属する取引を抽出してください
q1 = sales_df["Amount"].quantile(0.25)
q3 = sales_df["Amount"].quantile(0.75)
print(q1)
print(q3)
sales_df.query("@q1 <= Amount <= @q3")



# %%
# 18. Product_IDとStore_IDは何種類あるか確認してください
print(sales_df["Product_ID"].nunique())
print(sales_df["Store_ID"].nunique())


#別のやり方
# prd_ID_len = len(sales_df["Product_ID"].unique())
# str_id_len = len(sales_df["Store_ID"].unique())
# print(f"Product_IDの種類: {prd_ID_len}個\nStore_IDの種類: {str_id_len}個" )


# %%
# 19. 取引データのProduct_ID ごとに Amount の合計を計算してください
sales_df.groupby('Product_ID')['Amount'].sum()

# %%
# 20. Product_ID ごとにQuantityの中央値を計算してください
sales_df.groupby('Product_ID')['Quantity'].median()

# %%

# %%
