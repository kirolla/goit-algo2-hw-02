def find_min_max(arr):
    # Базові випадки
    if len(arr) == 1:
        return arr[0], arr[0]

    if len(arr) == 2:
        return (min(arr[0], arr[1]), max(arr[0], arr[1]))

    # Ділимо масив
    mid = len(arr) // 2
    left_min, left_max = find_min_max(arr[:mid])
    right_min, right_max = find_min_max(arr[mid:])

    # Об'єднуємо
    return min(left_min, right_min), max(left_max, right_max)

if __name__ == "__main__":
    arr = [3, 7, 1, 9, 2, 8]
    print(find_min_max(arr))