def construct_frequency_list(dataset, min_support):
    items = {}
    sorted_freq_items = {}
    for transaction in dataset:
        for item in transaction:
            count = items.get(item)
            if count:
                items.update({item: count+1})
            else: 
                items.update({item: 1})
    freq_items = items.copy()
    for key in items:
        if freq_items[key] < min_support:
            del freq_items[key]
    sorted_freq_items = sorted(freq_items.items(), key=lambda x: (-x[1], x[0]))
    sorted_freq_items = dict(sorted_freq_items)
    print(sorted_freq_items)
    return sorted_freq_items

def construct_sorted_itemset(dataset, sorted_freq_items):
    ordered = []
    for transaction in dataset:
        tmp=[]
        for item in sorted_freq_items.keys():
            if item in transaction:
                tmp.append(item)
        ordered.append(tmp)
    print(ordered)
    return ordered


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
    freq = construct_frequency_list(dataset, 10)
    construct_sorted_itemset(dataset, freq)
