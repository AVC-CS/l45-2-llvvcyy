import random


def main():
    total = 0
    numbers = []
    
    while total <= 100:
        num = random.randint(1, 10)
        numbers.append(num)
        total += num
    
    total_excluding_last = total - numbers[-1]

    print(" ".join(map(str, numbers[:-1])))
    print(f"The total sum is {total}")

    print(" ".join(map(str, numbers)))
    print(f"The total sum is {total}")
    
    return numbers, total


if __name__ == '__main__':
    main()
