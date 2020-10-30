from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import fpgrowth
import pandas as pd
import mlxtend
import preprocessor

def generate_rule(data_file, frequent_itemsets):

    frequent_itemsets[0].update((x, y*0.001) for x, y in frequent_itemsets[0].items())
    lst = list(frequent_itemsets[0].items())
    new_lst = []
    for item in lst:
        # item[0] = item[0][0]
        # print(set(item[0]))
        new_lst.append((item[0][0], item[1]))
    a = pd.DataFrame(new_lst,
                   columns=['itemsets', 'support'])
    a = a.reindex(columns=['support', 'itemsets'])
    print(a)
    dataset = preprocessor.preprocess()
    te = TransactionEncoder()
    te_ary = te.fit(dataset).transform(dataset)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    ans = apriori(df, min_support=0.3)
    # print(ans.dtypes)
    rules = association_rules(ans,metric='confidence', min_threshold=0.5)
    print(rules[['antecedents', 'consequents', 'support', 'confidence']])