import os.path

def build_heap(data):
    swaps = []
    # Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n = len(data)

    def sift_down(i):
        nonlocal swaps
        min_index = i
        left = 2*i +1
        right = 2*i +2

        if left < n and data[left] < data[min_index]:
            min_index = left
        if right < n and data[right] < data[min_index]:
            min_index = right
        if i != min_index:
            swaps.append((i, min_index))
            data[i], data[min_index] = data[min_index], data[i]
            sift_down(min_index)
    for i in range(n//2, -1, -1):
        sift_down(i)

    return swaps


def main():
    # add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    input_type = input()
    if input_type == 'I':
        # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))
    elif input_type == 'F':
        filename = input()
        if not os.path.exists(filename):
            print("File not found")
            return
        with open(filename) as file:
            n = int(file.readline())
            data = list(map(int, file.readline().strip().split()))
    else:
        print("Invalid input type")
        return  

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data
    # and give back all swaps
    swaps = build_heap(data)

    # output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    assert len(swaps) < 4*n

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
