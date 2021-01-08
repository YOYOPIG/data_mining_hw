import numpy as np 
import matplotlib.pyplot as plt
import preprocessor
import time

def normalize_vector(vec):
    vec_sum = vec.sum()
    norm_vec = vec/vec_sum
    return norm_vec

def normalize_matrix(matrix):
    for i in range(len(matrix)):
        matrix_sum = matrix[:, i].sum()
        if matrix_sum != 0:
            matrix[:, i] = matrix[:, i]/matrix_sum
    return matrix

def HITS(threshold, max_iter):
    hub = hits[0]
    auth = hits[1]
    iter_ctr = 0
    cur_thresh = float('inf')
    while cur_thresh > threshold and iter_ctr < max_iter:
        iter_ctr += 1
        prev_hub = hub.copy()
        prev_auth = auth.copy()
        hub = adj_matrix.dot(adj_matrix.T).dot(hub)
        auth = adj_matrix.T.dot(adj_matrix).dot(auth)
        hub = normalize_vector(hub)
        auth = normalize_vector(auth)
        diff = [hub-prev_hub, auth-prev_auth]
        cur_thresh = max([abs(diff[0]).max(), abs(diff[1]).max()])
    ret_hub=[]
    for item in hub:
        ret_hub.append(item[0])
    ret_auth=[]
    for item in auth:
        ret_auth.append(item[0])
    return ret_hub, ret_auth, iter_ctr

def PageRank(d, max_iter, threshold):
    v = pr[0]
    N = pr[1]
    normalized = normalize_matrix(adj_matrix.T.copy())
    tmp = ((1-d) / N) * np.ones((N, 1), dtype=np.float)
    iter_ctr = 0
    while iter_ctr < max_iter:
        iter_ctr += 1
        prev_v = v.copy()
        v = d * normalized.dot(v) + tmp
        if np.allclose(prev_v, v, atol=threshold):
            break
    rank=[]
    for item in normalize_vector(v):
        rank.append(item[0])
    return rank, iter_ctr

def SimRank(C, threshold, max_iter):
    normalized_adj_matrix = normalize_matrix(adj_matrix.copy())
    sim = np.identity(len(adj_matrix), dtype=np.float)
    iter_ctr = 0 
    while iter_ctr < max_iter:
        iter_ctr += 1
        prev = sim.copy()
        sim = C * np.matmul(np.matmul(normalized_adj_matrix.T, sim), normalized_adj_matrix)
        np.fill_diagonal(sim, 1.0)
        if np.allclose(prev, sim, atol=threshold):
            break
    return sim, iter_ctr

if __name__ == "__main__":
    for i in range(1,7):
        print(i)
        hits, pr, adj_matrix = preprocessor.preprocess('./hw3dataset/graph_'+str(i)+'.txt')
        start = time.time()
        hub, auth, itera_H = HITS(threshold=1e-08, max_iter=1000)
        end = time.time()
        print(end - start)
        start = time.time()
        rank, itera_P = PageRank(d=0.85, max_iter=100, threshold=1e-08)
        end = time.time()
        print(end - start)
        if i<=5:
            start = time.time()
            sim, itera_S = SimRank(C=0.9, threshold=1e-04, max_iter=1000)
            end = time.time()
            print(end - start)
            np.savetxt('./output/graph_'+str(i)+'_SimRank.txt', sim, fmt='%f')
        np.savetxt('./output/graph_'+str(i)+'_HITS_authority.txt', auth, fmt='%f', newline=' ')
        np.savetxt('./output/graph_'+str(i)+'_HITS_hub.txt', hub, fmt='%f', newline=' ')
        np.savetxt('./output/graph_'+str(i)+'_PageRank.txt', rank, fmt='%f', newline=' ')
        