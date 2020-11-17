from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import fpgrowth
import pandas as pd
import mlxtend
import preprocessor

def test():
    dataset = preprocessor.preprocess2()
    print(dataset)
    te = TransactionEncoder()
    te_ary = te.fit(dataset).transform(dataset)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    # print(df)
    ans = apriori(df, min_support=0.4, use_colnames=True)
    # print(ans)
    rules = association_rules(ans,metric='confidence', min_threshold=0.5)
    print(rules[['antecedents', 'consequents', 'support', 'confidence']])

test()