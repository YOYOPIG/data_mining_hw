import pandas as pd
# 傳入的數據須滿足特定的格式,用此方法轉換為bool值
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

def Mlx(itemsets, minimumSup):
	te = TransactionEncoder()	# 定義模型
	df_tf = te.fit_transform(itemsets)
	df = pd.DataFrame(df_tf,columns=te.columns_)
	return apriori(df,min_support=minimumSup,use_colnames=True)

