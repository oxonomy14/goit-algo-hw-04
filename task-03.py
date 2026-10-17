import timeit


from insertion_sort import insertion_sort
from merge_sort import merge_sort


import random

if __name__ == "__main__":
    # Генерація випадкового списку чисел
    data_small = [random.randint(1, 1_000) for _ in range(1_000)]
    data_medium = [random.randint(1, 10_000) for _ in range(10_000)]

    # Вимірювання часу виконання для кожного алгоритму сортування

    time_insertion_small = timeit.timeit(lambda: insertion_sort(data_small[:]), number=10)
    time_merge_small = timeit.timeit(lambda: merge_sort(data_small[:]), number=10)
    time_insertion_medium = timeit.timeit(lambda: insertion_sort(data_medium[:]), number=10)
    time_merge_medium = timeit.timeit(lambda: merge_sort(data_medium[:]), number=10)
    time_sorted_small = timeit.timeit(lambda: sorted(data_small[:]), number=10)
    time_sorted_medium = timeit.timeit(lambda: sorted(data_medium[:]), number=10)
    time_sort_small = timeit.timeit(lambda: data_small[:].sort(), number=10)
    time_sort_medium = timeit.timeit(lambda: data_medium[:].sort(), number=10)

    print("")
    print("Результати вимірювання часу виконання алгоритмів сортування:")
    print("")
    print(f"{'Algorithm':<20} | {'Time Small Dataset (1,000)':<30} | {'Time Medium Dataset (10,000)':<30}")
    print("-" * 90)
    print(f"{'Insertion Sort':<20} | {time_insertion_small:<30} | {time_insertion_medium:<30}")
    print(f"{'Merge Sort':<20} | {time_merge_small:<30} | {time_merge_medium:<30}")
    print(f"{'Sorted':<20} | {time_sorted_small:<30} | {time_sorted_medium:<30}")
    print(f"{'List.sort()':<20} | {time_sort_small:<30} | {time_sort_medium:<30}")
    print("")

 
