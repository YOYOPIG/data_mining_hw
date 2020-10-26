class Node:
    def __init__(self, item):
        self.item = item
        self.value = 1
        self.children = []
        self.parent = None
        #self.next = None
    
    def find_child(self, item):
        for child in self.children:
            if item == child.item:
                return child
        return None

class FPTree:
    def __init__(self, sorted_freq_items):
        self.root = Node("root")
        self.root.value = None
        self.header_table = {}

    def insert(self, transaction):
        current_node = self.root
        for item in transaction:
            next_node = current_node.find_child(item)
            if next_node:
                current_node = next_node
                current_node.value += 1
            else:
                new_node = Node(item)
                new_node.parent = current_node
                current_node.children.append(new_node)
                current_node = new_node
                header_list = self.header_table.get(item)
                if header_list:
                    header_list.append(new_node)
                else:
                    self.header_table.update({item: [new_node]})
                

