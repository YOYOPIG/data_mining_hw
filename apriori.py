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

def apriori(dataset, min_support):
    candidates = first_scan(dataset)
    frequent_itemsets = []
    while candidates:
        Lk = find_Lk(candidates, min_support)
        frequent_itemsets.append(Lk)
        candidates = find_Ck(Lk, dataset)

if __name__ == "__main__":
    import pandas as pd

    data = pd.read_csv(
        "data.txt", sep="\\s+", names=["id", "seq", "item"]
    )

    df = pd.DataFrame(data)
    df = df.groupby("id")["item"].apply(list)

    # Put into List[[],[],.......,[]]
    dataset = []
    for data in df:
        dataset.append(data)
    apriori(dataset, 5)