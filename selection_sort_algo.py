# Time Complexity: O(n ^ 2)
# Space Complexity: O(1)
class Selection_Sort:
	def __init__(self, array):
		self.array = array

	def sort_array(self):
		for i in range(len(self.array) - 1):
			min_index = i
			for j in range(i+1, len(self.array)):
				# Compare with the minimum index.
				if self.array[j] < self.array[min_index]:
					min_index = j
			self.array[i], self.array[min_index] = self.array[min_index], self.array[i]
		return self.array

if __name__ == "__main__":

	unsorted_array = [7, 2, 63, 85, 45, 295, 45]
	print(f"Before sorting: {unsorted_array}")

	sort = Selection_Sort(unsorted_array)

	sorted_array = sort.sort_array()
	print(f"After sorting: {sorted_array}")