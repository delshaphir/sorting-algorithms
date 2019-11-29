import sys
from typing import List

def insertion_sort(arr: List[int]):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def main():
    if len(sys.argv) < 2:
        print('Usage: python {0} [integer array]'.format(sys.argv[0]))
        sys.exit()
    a = [int(x) for x in sys.argv[1:]]
    print(insertion_sort(a))

if __name__ == '__main__':
    main()