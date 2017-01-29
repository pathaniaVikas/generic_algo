n=0
count=0

min_heap = []
max_heap = []

def swap(i, j, heap):
    temp = heap[i]
    heap[i] = heap[j]
    heap[j] = temp

def min_heapify_down():
    index = 0
    swap(index, len(min_heap)-1, min_heap)
    min_heap.pop()
    while 2*index + 1 <= len(min_heap)-1:
        smallest_index = 0
        if 2*index + 2 <= len(min_heap)-1:
            if min_heap[2*index + 1] < min_heap[2*index + 2]:
                smallest_index = 2*index + 1
            else:
                smallest_index = 2*index + 2

            if min_heap[index] > min_heap[smallest_index]:
                swap(index, smallest_index, min_heap)
                index = smallest_index
            else:
                break
        else:
            if min_heap[index] > min_heap[2*index + 1 ]:
                swap(index, 2*index + 1 , min_heap)
            break

def max_heapify_down():
    index = 0
    swap(index, len(max_heap)-1, max_heap)
    max_heap.pop()
    while 2*index + 1 <= len(max_heap)-1:
        largest_index = 0
        if 2*index + 2 <= len(max_heap)-1:
            if max_heap[2*index + 1] > max_heap[2*index + 2]:
                largest_index = 2*index + 1
            else:
                largest_index = 2*index + 2

            if max_heap[index] < max_heap[largest_index]:
                swap(index, largest_index, max_heap)
                index = largest_index
            else:
                break
        else:
            if max_heap[index] < max_heap[2*index + 1 ]:
                swap(index, 2*index + 1 , max_heap)
            break

def max_heapify(index):
    while index > 0:
        parent_index = 0
        if index%2 == 0:
            parent_index = int(index/2 -1)
        else:
            parent_index = int(index/2)
        
        if max_heap[index] > max_heap[parent_index]:
            swap(index, parent_index, max_heap)
            index = parent_index
        else:
            break

def min_heapify(index):
    while index > 0:
        parent_index = 0
        if index%2 == 0:
            parent_index = int(index/2 -1)
        else:
            parent_index = int(index/2)
        
        if min_heap[index] < min_heap[parent_index]:
            swap(index, parent_index, min_heap)
            index = parent_index
        else:
            break

def calculate_median():
	# if size of two heaps is same, return sum of roots/2;
	# else check which has greater size return its root
	#print(min_heap)
	#print(max_heap)
	if len(min_heap) - len(max_heap) == 0:
		return (min_heap[0] + max_heap[0])/2
	elif len(min_heap) > len(max_heap):
		return float(min_heap[0])
	else:
		return float(max_heap[0])

def find_median():
	global n
	global count
	while n:

		data = int(input().strip())
		if n == count:
			# this is first element, create a max heap and add it
			max_heap.append(data)
			print(calculate_median())
		elif n == count - 1:
			# this is the second element, check if it should go to min_heap or max_heap
			if data > max_heap[0]:
				min_heap.append(data)
			else:
				min_heap.append(max_heap[0])
				max_heap.pop()
				max_heap.append(data)
			print(calculate_median())
		else:
			# check if element is smaller than max heap root add it to max heap
			# else add it to min heap
			if data < max_heap[0]:
				max_heap.append(data)
				max_heapify(len(max_heap) -1)
			else:
				min_heap.append(data)
				min_heapify(len(min_heap)-1)

			# check if size of min heap and max heap differs by more than 1 
			# remove root element from heap which has more elements and add it to other
			if len(min_heap) - len(max_heap) > 1:
				max_heap.append(min_heap[0])
				max_heapify(len(max_heap) -1)
				min_heapify_down()
			elif len(max_heap) - len(min_heap) > 1:
				min_heap.append(max_heap[0])
				min_heapify(len(min_heap)-1)
				max_heapify_down()

			# calculate median
			print("%.1f" % calculate_median())

		n -= 1

if __name__ == '__main__':
	n = int(input().strip())
	count = n
	find_median()