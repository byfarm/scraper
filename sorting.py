def qick_sort_lh(houses: list[tuple], left: int=0, right: int=None):
	"""
	sorts from low to high assuming the input is an enumerated list. Is using the quicksort algorithm.
	:param houses: enumerated list of price, sqft, or whatever
	:param left: left index
	:param right: right indes
	:return: sorted list of houses, still enumerated
	"""
	# will have list like [(0, price),...]
	if right is None:
		right = len(houses) - 1
	if left >= right:
		return

	piv_idx = partision(houses, left, right)
	qick_sort_lh(houses, left, piv_idx - 1)
	qick_sort_lh(houses, piv_idx + 1, right)
	return houses


def partision(list, left, right):
	piv_val = list[right][1]
	part_ind = left

	for i in range(left, right):
		if list[i][1] < piv_val:
			swap(list, i, part_ind)
			part_ind += 1

	swap(list, right, part_ind)
	return part_ind


def swap(list, firstInd, secondInd):
	temp = list[firstInd]
	list[firstInd] = list[secondInd]
	list[secondInd] = temp