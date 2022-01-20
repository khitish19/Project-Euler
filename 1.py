def get_multiples(num_till: int, divisor: int) -> list:
    multiples = []
    for num in range(1, num_till):
        if num % divisor == 0:
            multiples.append(num)
    return multiples


if __name__ == '__main__':
    multiples_5 = get_multiples(1000, 5)
    multiples_3 = get_multiples(1000, 3)
    print(sum(set(multiples_5 + multiples_3)))
