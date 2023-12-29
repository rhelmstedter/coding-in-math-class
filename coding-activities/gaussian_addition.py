def gaussian_addition(figure_number: int) -> None:
    total = 0
    for num in range(int(figure_number) + 1):
        total += num
    print(f"The sum of integers from 0 to {figure_number} is {total}.")


gaussian_addition(100)
