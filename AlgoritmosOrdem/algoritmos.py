import random
import time

def selection_sort(array):
    for index in range(0, len(array)):
        min_index = index
        for right in range(index + 1, len(array)):
            if array[right] < array[min_index]:
                min_index = right
        array[index], array[min_index] = array[min_index], array[index]
    return array

def insertion_sort(array):
    for index in range(1, len(array)):
        current_element = array[index]
        while index > 0 and array[index - 1] > current_element:
            array[index] = array[index - 1]
            index -= 1
        array[index] = current_element
    return array

def shell_sort(array): 
    gap = len(array) // 2 
    while gap > 0:
        for i in range(gap, len(array)):
            val = array[i]
            j=i
            while j >= gap and array[j - gap] > val:
                array[j] = array[j - gap]
                j -= gap 
            array[j] = val
        gap //= 2
    return array

def partition(arr,low,high): 
    i = (low - 1)
    pivot = arr[high]
    for j in range(low , high):
        if arr[j] < pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i] 
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 )

def quick_sort(array,low=0,high=None):
    if high == None:
        high = len(array)-1
    if low < high:
        pi = partition(array,low,high) 
        quick_sort (array, low, pi-1) 
        quick_sort (array, pi+1, high)
    return array

def heapify(arr, n, i): 
	largest = i 
	l = 2 * i + 1	 
	r = 2 * i + 2	 
	if l < n and arr[i] < arr[l]: 
		largest = l 
	if r < n and arr[largest] < arr[r]: 
		largest = r 
	if largest != i: 
		arr[i],arr[largest] = arr[largest],arr[i] 
		heapify(arr, n, largest) 

def heap_sort(array): 
    n = len(array) 
    #constroi heapmax
    for i in range(n, -1, -1): 
        heapify(array, n, i) 
    #remove os elementos 1 a 1
    for i in range(n-1, 0, -1): 
        array[i], array[0] = array[0], array[i]
    heapify(array, i, 0) 
    return array

def merge_sort(array): 
    if len(array) >1: 
        mid = len(array)//2 
        L = array[:mid] 
        R = array[mid:] 
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                array[k] = L[i] 
                i+=1
            else: 
                array[k] = R[j] 
                j+=1
            k+=1
        while i < len(L): 
            array[k] = L[i] 
            i+=1
            k+=1
        while j < len(R): 
            array[k] = R[j] 
            j+=1
            k+=1
    return array

if __name__ == "__main__":

    vet10 = list(range(0,10))
    vet100 = list(range(0,100))
    vet1000 = list(range(0,1000))
    vet10000 = list(range(0,10000))
    vet100000 = list(range(0,100000))

    start_time = time.time()
    merge_sort(vet10)
    print(f"--- {(time.time() - start_time)} seconds 10---")

    start_time = time.time()
    merge_sort(vet100)
    print(f"--- {(time.time() - start_time)} seconds 100---")

    start_time = time.time()
    merge_sort(vet1000)
    print(f"--- {(time.time() - start_time)} seconds 1000---")
    
    start_time = time.time()
    merge_sort(vet10000)
    print(f"--- {(time.time() - start_time)} seconds 10000---")

    start_time = time.time()
    merge_sort(vet100000)
    print(f"--- {(time.time() - start_time)} seconds 100000---")


    vet10.reverse()
    vet100.reverse()
    vet1000.reverse()
    vet10000.reverse()
    vet100000.reverse()

    print("reverse")

    start_time = time.time()
    merge_sort(vet10)
    print(f"--- {(time.time() - start_time)} seconds 10---")

    start_time = time.time()
    merge_sort(vet100)
    print(f"--- {(time.time() - start_time)} seconds 100---")
   
    start_time = time.time()
    merge_sort(vet1000)
    print(f"--- {(time.time() - start_time)} seconds 1000---")

    start_time = time.time()
    merge_sort(vet10000)
    print(f"--- {(time.time() - start_time)} seconds 10000---")
    
    start_time = time.time()
    merge_sort(vet100000)
    print(f"--- {(time.time() - start_time)} seconds 100000---")

    vet10.clear()
    vet10 = list(range(0,5))
    for i in range(5):
        vet10.append(random.randint(-1000, 1000))

    vet100.clear()
    vet100 = list(range(0,50))
    for i in range(50):
        vet100.append(random.randint(-1000, 1000))

    vet1000.clear()
    vet1000 = list(range(0,500))
    for i in range(500):
        vet1000.append(random.randint(-1000, 1000))
    
    vet10000.clear()
    vet10000 = list(range(0,5000))
    for i in range(5000):
        vet10000.append(random.randint(-1000, 1000))

    vet100000.clear()
    vet100000 = list(range(0,50000))
    for i in range(50000):
        vet100000.append(random.randint(-1000, 1000))

    print("misto")

    start_time = time.time()
    merge_sort(vet10)
    print(f"--- {(time.time() - start_time)} seconds 10---")

    start_time = time.time()
    merge_sort(vet100)
    print(f"--- {(time.time() - start_time)} seconds 100---")
   
    start_time = time.time()
    merge_sort(vet1000)
    print(f"--- {(time.time() - start_time)} seconds 1000---")

    start_time = time.time()
    merge_sort(vet10000)
    print(f"--- {(time.time() - start_time)} seconds 10000---")
    
    start_time = time.time()
    merge_sort(vet100000)
    print(f"--- {(time.time() - start_time)} seconds 100000---")


    vet10.clear()
    for i in range(10):
        vet10.append(random.randint(-1000, 1000))

    vet100.clear()
    for i in range(100):
        vet100.append(random.randint(-1000, 1000))

    vet1000.clear()
    for i in range(1000):
        vet1000.append(random.randint(-1000, 1000))
    
    vet10000.clear()
    for i in range(10000):
        vet10000.append(random.randint(-1000, 1000))

    vet100000.clear()
    for i in range(100000):
        vet100000.append(random.randint(-1000, 1000))

    print("aleatório")

    start_time = time.time()
    merge_sort(vet10)
    print(f"--- {(time.time() - start_time)} seconds 10---")

    start_time = time.time()
    merge_sort(vet100)
    print(f"--- {(time.time() - start_time)} seconds 100---")
   
    start_time = time.time()
    merge_sort(vet1000)
    print(f"--- {(time.time() - start_time)} seconds 1000---")

    start_time = time.time()
    merge_sort(vet10000)
    print(f"--- {(time.time() - start_time)} seconds 10000---")
    
    start_time = time.time()
    merge_sort(vet100000)
    print(f"--- {(time.time() - start_time)} seconds 100000---")
    