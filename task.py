# TARGET ARRAY
A = [5, -3, -10, 4, -1, -2, 1, 7, -5, 8]

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

if __name__ == "__main__":
	# EXAMPLE
	result = sum_negative_between_max_min(A)
	print("Negative elements sum between min и max:", result)
