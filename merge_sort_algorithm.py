# Time Complexity: O(n log n)
# Space Complexity: O(n)
class MergeSort:

	def merge_sort(self, array):
		arr_length = len(array)

		if arr_length <= 1:
			return

		mid = arr_length // 2

		left_array = [0] * mid
		remaining_size = arr_length - mid
		right_array = [0] * remaining_size

		i = 0
		j = 0

		# Divide the array.
		for i in range(arr_length):
			if i < mid:
				left_array[i] = array[i]
			else:
				right_array[j] = array[i]
				j += 1

		self.merge_sort(left_array)
		self.merge_sort(right_array)
		self.merge(left_array, right_array, array)

	def merge(self, left_array, right_array, array):
		left_arr_size = len(left_array)
		right_arr_size = len(right_array)

		i = 0
		j = 0
		k = 0

		while i < left_arr_size and j < right_arr_size:
			if left_array[i] < right_array[j]:
				array[k] = left_array[i]
				i += 1
			else:
				array[k] = right_array[j]
				j += 1
			k += 1

		while i < left_arr_size:
			array[k] = left_array[i]
			k += 1
			i += 1

		while j < right_arr_size:
			array[k] = right_array[j]
			k += 1
			j += 1

if __name__ == "__main__":

	sort = MergeSort()
	array = [5, 3, 4, 9, 1, 8, 3, 7, 2]
	print(f"Array before sorting: {array}")
	sort.merge_sort(array)
	print(f"Array after sorting: {array}")