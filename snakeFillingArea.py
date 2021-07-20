def snakefill(n):
    n = int(n)
    body_size = 1
    eat_count = 0
    area = n * n

    while (body_size < area - body_size):

        eat_count += 1
        body_size *= 2

    return f'the snake can eat {eat_count} times before running out of space in a {n}x{n} grid'

print(snakefill(input()))