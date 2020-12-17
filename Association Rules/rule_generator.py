from mlxtend.frequent_patterns import association_rules # for rule generation only
import pandas as pd
import preprocessor

def generate_rule(data_file, frequent_itemsets):

    #frequent_itemsets[0].update((x, y*0.001) for x, y in frequent_itemsets[0].items())
    ctr=0
    new_lst = []
    while True:
        lst = list(frequent_itemsets[ctr].items())
        if not lst:
            break
        for item in lst:
            # item[0] = item[0][0]
            # print(set(item[0]))
            new_lst.append((frozenset(item[0]), item[1]*0.001))
        ctr+=1
    # print(sorted(new_lst))
    a = pd.DataFrame(sorted(new_lst),
                   columns=['itemsets', 'support'])
    a = a.reindex(columns=['support', 'itemsets'])
    print(a)
    # dataset = preprocessor.preprocess()
    # te = TransactionEncoder()
    # te_ary = te.fit(dataset).transform(dataset)
    # df = pd.DataFrame(te_ary, columns=te.columns_)
    # ans = apriori(df, min_support=0.3)
    # print(ans)
    rules = association_rules(a,metric='confidence', min_threshold=0.5)
    print(rules[['antecedents', 'consequents', 'support', 'confidence']])

def generate_rule_fp(data_file, frequent_itemsets):
    a = pd.DataFrame(sorted(frequent_itemsets),
                   columns=['itemsets', 'support'])
    a = a.reindex(columns=['support', 'itemsets'])
    print(a)
    rules = association_rules(a,metric='confidence', min_threshold=0.5)
    print(rules[['antecedents', 'consequents', 'support', 'confidence']])