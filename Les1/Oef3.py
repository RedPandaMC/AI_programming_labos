import timeit
import random

class ListSorter:

    @staticmethod
    def insertion_sort(numbers):
        for i in range(1, len(numbers)):
            key = numbers[i]
            j = i - 1
            while j >= 0 and key < numbers[j]:
                numbers[j + 1] = numbers[j]
                j -= 1
            numbers[j + 1] = key
        return numbers

    @staticmethod
    def quick_sort(numbers):
        if len(numbers) <= 1:
            return numbers
        else:
            pivot = numbers[0]
            greater = [element for element in numbers[1:] if element > pivot]
            lesser = [element for element in numbers[1:] if element <= pivot]
            return ListSorter.quick_sort(lesser) + [pivot] + ListSorter.quick_sort(greater)


for size in [10, 100, 1000, 100_000]:
    unsorted_list = [random.randint(0, size) for _ in range(size)]

    start_time = timeit.default_timer()
    ListSorter.insertion_sort(unsorted_list.copy())
    print(f"Insertion sort time for size {size}: {timeit.default_timer() - start_time}")

    start_time = timeit.default_timer()
    ListSorter.quick_sort(unsorted_list.copy())
    print(f"Quick sort time for size {size}: {timeit.default_timer() - start_time}")