from mlxtend.frequent_patterns import association_rules
import pandas as pd
import Apriori as ap

def generate_rule(data_file, frequent_itemsets):
    data = pd.read_csv(data_file, sep="\\s+", names=["id", "seq", "item"])
    df = pd.DataFrame(data)
    df = df.groupby("id")["item"].apply(list)
    rules = association_rules(frequent_itemsets,metric='confidence', min_threshold=0.8)
    print(rules[['antecedents', 'consequents', 'support','confidence']])