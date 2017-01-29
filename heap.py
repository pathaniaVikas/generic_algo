min_heap = []

def swap(i, j):
    temp = min_heap[i]
    min_heap[i] = min_heap[j]
    min_heap[j] = temp

def heapify_down():
    index = 0
    swap(index, len(min_heap)-1)
    min_heap.pop()
    while 2*index + 1 <= len(min_heap)-1:
        smallest_index = 0
        if 2*index + 2 <= len(min_heap)-1:
            if min_heap[2*index + 1] > min_heap[2*index + 2]:
                smallest_index = 2*index + 1
            else:
                smallest_index = 2*index + 2

            if min_heap[index] < min_heap[smallest_index]:
                swap(index, smallest_index)
                index = smallest_index
            else:
                break
        else:
            if min_heap[index] < min_heap[2*index + 1 ]:
                swap(index, 2*index + 1 )
            break

def heapify(index):
    while index > 0:
        parent_index = 0
        if index%2 == 0:
            parent_index = int(index/2 -1)
        else:
            parent_index = int(index/2)
        
        if min_heap[index] > min_heap[parent_index]:
            swap(index, parent_index)
            index = parent_index
        else:
            break

count = 0
ls = []
while count < 1000:
    n = int(input())
    ls.append(n)
    min_heap.append(n)
    heapify(len(min_heap)-1)
    count += 1
#print(min_heap)
ls.sort()
while len(ls) > 0:
    print(ls.pop())
# count = 0
# while count < 1000:
#     print(min_heap[0])
#     heapify_down()
#     count += 1

