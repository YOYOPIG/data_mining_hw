import fp_tree
import preprocessor

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
    #print(sorted_freq_items)
    return sorted_freq_items

def construct_sorted_itemset(dataset, sorted_freq_items):
    ordered = []
    for transaction in dataset:
        tmp=[]
        for item in sorted_freq_items.keys():
            if item in transaction:
                tmp.append(item)
        ordered.append(tmp)
    #print(ordered)
    return ordered

def find_conditional_pattern(header_table, sorted_freq_items):
    conditional_pattern_base = {}
    for item in sorted_freq_items:
        # print(item)
        patterns_list = []
        node_list = header_table.get(item)
        # Find the path of nodes in header table
        for node in node_list:
            cur = node.parent
            path = []
            # Loop til the root
            while cur:
                if cur.item != 'root':
                    path.append(cur.item)
                cur = cur.parent
            path.reverse()
            # Add current path and its weight to the
            patterns_list.append({tuple(path): node.value})
        conditional_pattern_base.update({item: patterns_list})
    # print(conditional_pattern_base)
    return conditional_pattern_base

def fp_tree_growth(prefix, value, min_support, ordered, patternList):
    itemsets = []
    # print(value)
    for item in value:
        # print(list(item.keys())[0])
        count = int(list(item.values())[0])
        while count:
            itemsets.append(list(item.keys())[0])
            count += -1
    freq_list = construct_frequency_list(itemsets, min_support)
    itemset = construct_sorted_itemset(dataset, freq_list)
    tree = fp_tree.FPTree(itemset)
    for transaction in itemset:
        tree.insert(transaction)

    if not tree.header_table:
        # print(patternList)
        return patternList


    conditional_pattern_base = find_conditional_pattern(tree.header_table,freq_list)

    for key, value in conditional_pattern_base.items():
        count = 0
        for item in value:
            count = count + int(list(item.values())[0])
        pattern = []
        item = []
        item.append(key)
        pattern.append(prefix + item)
        pattern.append(count)
        patternList.append(pattern)
        fp_tree_growth(prefix + item, value, min_support, ordered, patternList)

    return patternList

if __name__ == "__main__":
    dataset = preprocessor.preprocess()
    # main
    min_support = 500
    ptn = {}
    freq_list = construct_frequency_list(dataset, min_support)
    itemset = construct_sorted_itemset(dataset, freq_list)
    tree = fp_tree.FPTree(itemset)
    for transaction in itemset:
        tree.insert(transaction)
    conditional_pattern_base = find_conditional_pattern(tree.header_table,freq_list)
    for key, value in conditional_pattern_base.items():
        if value:
            patternList = fp_tree_growth(list(), value, min_support, itemset, list())
            ptn.update({key: patternList})
    print(ptn)