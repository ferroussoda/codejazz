def create_heap(data, n, i): 
    largest = i  # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and data[i] < data[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and data[largest] < data[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        data[i],data[largest] = data[largest],data[i]  # swap 
  
        # Heapify the root. 
        create_heap(data, n, largest) 
  
# The main function to sort an dataay of given size 
def heapsort(data): 
    n = len(data) 
  
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        create_heap(data, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        data[i], data[0] = data[0], data[i]   # swap 
        create_heap(data, i, 0) 
  
# Driver code to test above 
data = [ 12, 11, 13, 5, 6, 7] 
heapsort(data) 
n = len(data) 
print ("Sorted dataay is") 
for i in range(n): 
    print ("%d" %data[i])

