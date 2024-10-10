class InsertionSort:

	# Time Complexity: O(n ^ 2)
	# Space Complexity: O(1)
	def insertion_sort(self, array):
		for i in range(1, len(array)):
			current_value = array[i]
			j = i - 1
			while j >= 0 and array[j] > current_value:
				array[j+1] = array[j]
				j -= 1
			array[j+1] = current_value
		return array

if __name__ == "__main__":

	unsorted_array = [7, 2, 63, 85, 45, 295, 45]
	print(f"Unsorted Array: {unsorted_array}")

	sort = InsertionSort()

	sorted_array = sort.insertion_sort(unsorted_array)
	print(f"Sorted Array: {sorted_array}")