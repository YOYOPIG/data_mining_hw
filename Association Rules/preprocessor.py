import pandas as pd
def preprocess():
    raw = pd.read_csv(
        "data.txt", sep="\\s+", names=["id", "seq", "item"]
    )
    df = pd.DataFrame(raw)
    df = df.groupby("id")["item"].apply(list)
    # Put into List[[],[],.......,[]]
    dataset = []
    for transaction in df:
        dataset.append(transaction)
    return dataset

def preprocess2():
    raw = pd.read_csv(
        "car.data", sep=",", names=["buying", "maint", "doors", "persons", "lug_boot", "safety", "class"]
    )
    dataset = raw.values.tolist()
    # df = pd.DataFrame(raw)
    # df = df.groupby("id")["item"].apply(list)
    # # Put into List[[],[],.......,[]]
    
    return dataset