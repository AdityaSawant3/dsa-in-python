class BubbleSort:

	# Time Complexity: O(n2)
	# Auxiliary Space: O(1)
	def bubble_sort(self, array):
		arr_length = len(array)
		for i in range(arr_length):
			for j in range(i+1, arr_length):
				if array[j] < array[i]:
					array[j], array[i] = array[i], array[j]
		return array


if __name__ == "__main__":

	arr = [65, 42, 87, 15, 8, 66, 25, 72]

	sort = BubbleSort()
	print(sort.bubble_sort(arr))