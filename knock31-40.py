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
# 31. 新しく作成したカラムを削除してください
# sales_df
# sales_df.drop(["Transaction_Date_yyyyMMdd", "Month", "Day_of_Week", "Week"], axis=1, inplace=True)
# sales_df
# %%
# 32. Amount が1000円を超える取引を抽出し、Store_ID と Product_ID ごとに Amount の合計を計算してください

over_1000_df = sales_df[sales_df['Amount'] > 1000]
over_1000_df.groupby(['Store_ID','Product_ID'])['Amount'].sum()


# %%
# 33. Store_ID ごとの合計Amountを集計し300000円以上の店舗を抽出してください
store_sales = sales_df.groupby('Store_ID')['Amount'].sum().reset_index()
sales_over_300000 = store_sales.query('Amount >=300000')
sales_over_300000
# %%
# 34. 会員ごとに取引回数をカウントしてください
# OK：取引回数（何回取引したか）
# sales_df.groupby('Member_ID')['Transaction_ID'].count()

sales_Quantity = sales_df.groupby('Member_ID')['Transaction_ID'].count().reset_index()
# sales_Quantity
sales_Quantity.sort_values(by='Member_ID', key=lambda x: x.astype(int), ascending=True)


# %%
# 35. 会員ごとに取引回数をカウントし、2回以上の取引がある会員を抽出してください
#データフレーム型で出力 Member_IDごとに並び替え（昇順）
sales_Quantity[sales_Quantity['Transaction_ID'] >=2].sort_values(by='Member_ID',key = lambda x: x.astype(int),ascending=True)
sales_Quantity = sales_Quantity.rename(columns={'Transaction_ID': '取引回数'})
sales_Quantity



# %%
# 36. 年齢グループ（-30歳、31-50歳、51-65歳、66歳-）を作成し、各グループの会員数を集計してください。
#Age_Range列を作成するための関数 Seriesの値（Age）を受け取り、返り値を判定する
# def setAgeRange(age):
#   if age <=30:
#     return "-30歳"
#   elif age >30 and age <=50:
#     return "31-50歳"
#   elif age >50 and age <=65:
#     return "51-65歳"
#   else:
#     return "66歳-"
# #Age_Range列を追加
# member_df["Age_Range"] = member_df["Age"].apply(setAgeRange)

# # member_df

# Age_Range = member_df.groupby('Age_Range')['Member_ID'].count().reset_index()
# Age_Range.rename(columns={'Member_ID':'年齢別会員数'})

member_df['Age_Range'] = pd.cut(
    member_df['Age'],
    bins=[0, 30, 50, 65, 200],
    labels=['-30歳', '31-50歳', '51-65歳', '66歳-']
)
member_df


# %%
# 37. 会員になってからの日数（Days_Since_Registration）のグループ（〜1年、1年〜2年, 2年〜）を作成し、各グループの会員数を集計してください

min_registration = member_df['Days_Since_Registration'].min()
# min_registration
max_registration = member_df['Days_Since_Registration'].max()
# max_registration

member_df['Registration_label'] = pd.cut(
  member_df['Days_Since_Registration'],
  bins=[min_registration-1,365,730,max_registration],
  labels = ['〜1年','1年〜2年','2年〜']
)

# member_df[member_df['Days_Since_Registration'] == 1]

member_df.groupby('Registration_label')['Member_ID'].count().reset_index()


# %%
# 38. 売上データと会員データを結合しmerged_dfとして定義してください
merge_df = pd.merge(sales_df,member_df,on='Member_ID',how='left')
# merge_df



# %%
# 39. 性別 ごとに 平均Amount を計算してください
# merge_df
merge_df.groupby('Gender')["Amount"].mean()
# 

# %%
# 40. 性別ごとの平均 Quantity を集計してください
merge_df.groupby('Gender')["Quantity"].mean()