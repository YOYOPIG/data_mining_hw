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

def find_conditional_pattern(header_table, sorted_freq_items):
    conditional_pattern_base = {}
    for item in sorted_freq_items:
        patterns_list = []
        node_list = header_table.get(item)
        # Find the path of nodes in header table
        for node in node_list:
            cur = node.parent
            path = []
            # Loop til the root
            while cur:
                if cur.item != "root":
                    path.append(cur.item)
                cur = cur.parent
            path.reverse()
            # Add current path and its weight to the
            patterns_list.append({path: node.value})
        conditional_pattern_base.update({item: patterns_list})
    return conditional_pattern_base

def Freq_tree(prefix, value, minimumSup, orderList, patternList):
    itemsets = []
    #  將所有的condition pattern base 建成 itesmset
    for item in value:
        count = int(item[1])
        #根據 path權重決定出現次數
        while count:
            itemsets.append(item[0])
            count += -1
    #同FP-Tree流程
    c1 = Apriori.C1(itemsets)
    l1 = Apriori.Lk(c1, minimumSup)
    orderList = Sort(l1)
    #同FP-Tree流程的step1
    freqHd = FPtree(itemsets, orderList)

    # 中止條件 如果 headerTable空 跳出遞迴
    if not freqHd:
        return patternList

    orderList.reverse()
    #同FP-Tree流程的step2
    pathDic = CondPatternBase(freqHd, orderList)

    #同FP-Tree流程的step3
    for key, value in pathDic.items():
        count = 0
        for item in value:
            count = count + int(item[1])
        pattern = []
        #key to list
        item = []
        item.append(key)
        # 與headerTable中的 item組成 frequent Pattern
        pattern.append(prefix + item)
        # frequent
        pattern.append(count)
        patternList.append(pattern)
        FreqTree(prefix + item, value, minimumSup, orderList, patternList)

    return patternList

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
