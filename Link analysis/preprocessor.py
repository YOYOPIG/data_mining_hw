import numpy as np 

def preprocess(dataset_path):
    with open(dataset_path, "r") as f:
        data = f.read()
    data = data.split("\n")
    diff_element = set()
    for pair in data:
        pair = pair.split(",")
        diff_element |= set(pair)
    else:
        amount = len(diff_element)

    hub = np.ones((amount, 1))
    auth = np.ones((amount, 1))
    hits = [hub, auth]
    pr = [np.ones((amount, 1))/amount, amount]
    adj_matrix = np.zeros((amount,amount), dtype=np.float)
    
    for edge in data:
        edge = edge.split(",")
        adj_matrix[int(edge[0])-1][int(edge[1])-1] = 1  # Initial number is 1
#         adj_matrix[int(edge[0])][int(edge[1])] = 1       # Initial number in IBM data is 0 
    return hits, pr, adj_matrix #, diff_element 