def base_5(n, base):
    result = ""
    while n > 0:
        result += str(n % base)
        n //= base
    return result[::-1]


print(base_5(23, 7))