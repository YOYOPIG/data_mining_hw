import preprocessor
import rule_generator

class Node:
    def __init__(self, item):
        self.item = item
        

def first_scan(dataset):
    C1 = {}
    for transaction in dataset:
        for item in transaction:
            item = tuple([item]) # Make it a tuple in order to use it as a key of dict
            count = C1.get(item)
            if count:
                C1.update({item: count+1})
            else: 
                C1.update({item: 1})
    return C1

def find_Lk(candidates, min_support):
    Lk = candidates.copy()
    for key in candidates:
        if Lk[key] < min_support:
            del Lk[key]
    return Lk

def find_Ck(Lk, dataset):
    Ck = {}
    # List itemset in Ck
    for i in Lk:
        for j in Lk:
            # Iterate through all possible combinations
            if len(set(i) - set(j)) == 1:
                Ck.update({tuple(set(i).union(set(j))): 0})
    if len(Ck) == 0:
        return Ck
    # Scan database for support of each itemset
    for data in Ck:
        count = 0
        for transaction in dataset:
            if set(data) <= set(transaction):
                count += 1
        Ck.update({tuple(data): count})
    return Ck

def find_Ck_ht(Lk, dataset):
    Ck = {}
    # List itemset in Ck
    for i in Lk:
        for j in Lk:
            # Iterate through all possible combinations
            if len(set(i) - set(j)) == 1:
                Ck.update({tuple(set(i).union(set(j))): 0})
    if len(Ck) == 0:
        return Ck
    # Find support of each itemset using hash tree
    # Build tree
    root = {}
    cur = root
    height = 0
    for candidate in Ck.keys:
        height = 0
        for item in candidate:
            if cur.get(item)==None:
                cur.update({item: {}})
                cur = cur[item]
            else:
                cur = cur[item]
            height += 1
        cur = root
    # Run thru the tree for each transaction
    for transaction in dataset:
        lst = list(combinations(transaction, height))
        for cand in lst:
            traverse_hash_tree(root, cand, [], {})


def traverse_hash_tree(root, items, path, count_dict):
    if bool(root)==False: # End of recursive, push path as ans
        if count_dict.get(path):
            count_dict.update({path:count_dict[path]+1})
        else:
            count_dict.update({path:1})
    for item in root: # keep looping
        if item in items:
            traverse_hash_tree(root[item], items.remove(item), path.append(item), count_dict)
        else:
            return





def apriori(dataset, min_support):
    candidates = first_scan(dataset)
    frequent_itemsets = []
    while candidates:
        Lk = find_Lk(candidates, min_support)
        frequent_itemsets.append(Lk)
        candidates = find_Ck(Lk, dataset)
    print(frequent_itemsets)
    return frequent_itemsets

if __name__ == "__main__":
    dataset = preprocessor.preprocess()
    freq = apriori(dataset, len(dataset)*0.3)
    rule_generator.generate_rule("data.txt", freq)