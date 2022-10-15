def heapify(x):
    for i in range(int(len(x)/2) - 1, -1, -1):
        insert_up(x, i)

def insert_up(heap, pos):
    end_ind = len(heap)
    start_ind = pos
    new_item = heap[pos]

    child_ind = 2 * pos + 1
    while child_ind < end_ind:
        right_ind = child_ind + 1
        
        if right_ind < end_ind and heap[child_ind] > heap[right_ind]:
            child_ind = right_ind

        heap[pos] = heap[child_ind]
        pos = child_ind
        child_ind = 2 * pos + 1

    heap[pos] = new_item
    insert_down(heap, start_ind, pos)

def insert_down(heap, start_ind, current_ind):
    current_item = heap[current_ind]
    while current_ind > start_ind:
        parent_ind = (current_ind - 1) >> 1
        parent = heap[parent_ind]
        if current_item < parent:
            heap[current_ind] = parent
            current_ind = parent_ind
        else:
            break
    heap[current_ind] = current_item
    
def heappush(heap, item):
    heap.append(item)
    insert_down(heap, 0, len(heap)-1)

def heappop(heap):
    lastelt = heap.pop()    
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        insert_up(heap, 0)
        return returnitem
    return lastelt

