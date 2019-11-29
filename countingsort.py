import sys
from typing import List

def counting_sort(arr: List[int]):
    '''
    Accepts a list of integers and returns the
    sorted list, using the Counting-Sort algorithm.
    Complexity: Big-Theta(k + n)
    '''
    M = max(arr) + 1
    output = [0 for i in range(M)]
    count = [0 for i in range(M)]
    ans = [0 for i in arr]

    # Update count with number of instances of each value
    for i in arr:
        count[i] += 1

    # Update count s.t. each element stores sum of previous counts.
    # This will reflect the position of each object in the output.
    for i in range(M):
        count[i] += count[i - 1]

    for i in range(len(arr)):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    for i in range(len(arr)):
        ans[i] = output[i]

    return ans

def main():
    if len(sys.argv) < 2:
        print('Usage: python {0} [integer array]'.format(sys.argv[0]))
        sys.exit()
    a = [int(x) for x in sys.argv[1:]]
    print(counting_sort(a))

if __name__ == '__main__':
    main()