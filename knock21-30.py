# %%
import pandas as pd
import matplotlib.pyplot as plt
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
sales_df.info()

# %%
member_df.info()

# %%
# 21. Store_ID ごとに平均Amountを集計してください
# sales_df.groupby('Store_ID')['Amount'].mean()
#Store_IDを基準に並び替え
sales_df.groupby('Store_ID')['Amount'].mean().reset_index().sort_values(
    by='Store_ID', key=lambda x: x.astype(int)
)

# %%
# 22. 会員データの性別 (Gender) ごとに平均年齢を計算してください
member_df.groupby('Gender')['Age'].mean()


# %%
# 23. 会員ごとに平均 Amount を計算してください
sales_df.groupby('Member_ID')['Amount'].mean()

#会員の平均Amount Top5
sales_df.groupby('Member_ID')['Amount'].mean().sort_values(ascending=False).head(5)


# %%
# 24. Transaction_Dateから日付だけ取り出して日付ごとに Amount の合計を集計してください
# sales_df.groupby('Transaction_Date')['Amount'].sum() これは間違い

sales_df.groupby(sales_df['Transaction_Date'].dt.date)['Amount'].sum()

# %%
# おまけ
# ピボットの行ラベルを2つ使うイメージ
sales_df.groupby(['Store_ID', 'Product_ID'])['Amount'].sum()

# %%
# 25. 日付ごとの合計Amountを集計し、合計Amountが小さい順にソートしてください
sales_df.groupby('Transaction_Date')['Amount'].sum().sort_values(ascending=True)

# %%
# sales_df.groupby(sales_df["Transaction_Date"].dt.to_period('M'))['Amount'].sum()

# ② 別変数で受け取る
month_col = sales_df['Transaction_Date'].dt.to_period('M')
sales_df.groupby(month_col)['Amount'].sum()

#別解⇒新しい列を作成する
# sales_df["Month"] = sales_df["Transaction_Date"].dt.to_period("M")
# sales_df.groupby("Month")["Amount"].sum()
# sales_df.head()

# %%
# 27. 月ごとのAmountの増減の絶対値を前月と比較して計算してください
monthly = sales_df.groupby(sales_df["Transaction_Date"].dt.to_period('M'))['Amount'].sum()

abs(monthly.diff())


# %%
# テスト
monthly_list = monthly.to_list()
type(monthly_list)
result = []
for i,val in enumerate(monthly):
  if i == 0:
    result.append(None)
  else:
    res = abs(val - monthly_list[i-1])
    result.append(res)

print(result)

# %%
# 28. 曜日ごとの合計Amountを集計してください
# date_col = sales_df['Transaction_Date'].dt.day_name()
# sales_df.groupby(date_col)['Amount'].sum()

# 曜日の順番を定義
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

date_col = sales_df['Transaction_Date'].dt.day_name()
sales_df.groupby(date_col)['Amount'].sum().reindex(day_order)

# %%
# 29. 1週間ごとに合計Amountを集計してください
week_col = sales_df['Transaction_Date'].dt.to_period('W')
sales_df.groupby(week_col)['Amount'].sum()



# %%
# 30. 1週間ごとのAmountの増減を計算し、増加率をパーセンテージで表示してください
#1週間ごとの売上（例：2024-04-29/2024-05-05	241190）
week_col = sales_df['Transaction_Date'].dt.to_period('W')
week_sales = sales_df.groupby(week_col)['Amount'].sum()
week_sales.pct_change() * 100

