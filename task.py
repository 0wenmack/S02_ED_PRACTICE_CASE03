import random

# TARGET ARRAY
A = [5, -3, -10, 4, -1, -2, 1, 7, -5, 8]
TEXT = "MODE:\nType 1 for Manual Array input\nType 2 for Random Generated Array\nType 0 for predefined hardcoded Array\n\n > "

def sum_negative_between_max_min(A):
    if len(A) < 3:
        return 0  # No elements available

    max_index = A.index(max(A))
    min_index = A.index(min(A))

    # Borders
    start = min(max_index, min_index) + 1
    end = max(max_index, min_index)

    # Negative elements between MIN & MAX
    negative_elements = [x for x in A[start:end] if x < 0]
    return sum(negative_elements)

def generate_array(N, lower_bound=-10, upper_bound=10):
    return [random.randint(lower_bound, upper_bound) for _ in range(N)]

if __name__ == "__main__":
    choice = int(input(TEXT))
    if (choice == 1):
        A = [int(i) for i in (input("Enter numbers separated by a space:")).split()]
    elif (choice == 2):
        N = int(input("Array size(int): "))
        A = generate_array(N)
        print("Generated Array:", A)
    elif (choice == 0):
        pass
    else:
        print("Not a valid option")
    
    result = sum_negative_between_max_min(A)
    print("Negative elements sum between min и max:", result)
