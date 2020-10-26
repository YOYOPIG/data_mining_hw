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