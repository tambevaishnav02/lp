import heapq
class Node: 
    def __init__(self, freq, symbol, left=None, right=None): 
        self.freq = freq 
        self.symbol = symbol 
        self.left = left 
        self.right = right 
        self.huff = '' 
  
    def __lt__(self, nxt): 
        return self.freq < nxt.freq 
  
def printNodes(node, val=''): 
    newVal = val + str(node.huff) 
    if node.left: 
        printNodes(node.left, newVal) 
    if node.right: 
        printNodes(node.right, newVal) 
    if not node.left and not node.right: 
        print(f"{node.symbol} -> {newVal}") 

chars = input("Enter characters (space-separated): ").split()
freq = list(map(int, input("Enter corresponding frequencies (space-separated): ").split()))

if len(chars) != len(freq):
    print("Error: The number of characters and frequencies must be the same.")
else:
    item = [] 
    for i in range(len(chars)): 
        heapq.heappush(item, Node(freq[i], chars[i])) 
  
    while len(item) > 1: 
        left = heapq.heappop(item) 
        right = heapq.heappop(item) 
        left.huff = 0
        right.huff = 1
        newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right) 
        heapq.heappush(item, newNode) 
  
    print("\nHuffman Codes for each character:")
    printNodes(item[0])
