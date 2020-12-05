from bear import Bear
import numpy as np

class BearGenerator():
    def __init__(self):
        return
    
    def generate_bears(self, num):
        bears=[]
        for i in range(num):
            bear = Bear()
            bears.append(bear)
        return bears
    
    def generate_dataset(self, num):
        bears = self.generate_bears(num)
        x = []
        y = []
        for bear in bears:
            x.append(bear.to_list())
            y.append(bear.label)
        x = np.array(x)
        y = np.array(y)
        return [x, y]


if __name__ == "__main__":
    bears = BearGenerator().generate_bears(10)
    for bear in bears:
        print(bear.label + ' ' + bear.habitant_area)