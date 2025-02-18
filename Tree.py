class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __str__(self):
        return str(self.data)
    
def print_tree(node, level=0):
    print(" " * level + str(node.data))
    for child in node.children:
        print_tree(child, level + 1)
    
root = TreeNode("Electronics")

laptop = TreeNode("Laptop")
phone = TreeNode("Phone")
tv = TreeNode("TV")

root.add_child(laptop)
root.add_child(phone)
root.add_child(tv)

dell = TreeNode("Dell")
hp = TreeNode("HP")
laptop.add_child(dell)
laptop.add_child(hp)

iphone = TreeNode("Iphone")
android = TreeNode("Android")
phone.add_child(iphone)
phone.add_child(android)

samsung = TreeNode("Samsung")
lg = TreeNode("LG")
tv.add_child(samsung)
tv.add_child(lg)

print_tree(root)