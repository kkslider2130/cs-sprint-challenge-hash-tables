def has_negatives(a):
    cache = {}
    result = []
    for i in a:
        if -i in cache.keys():
            cache[-i] += 1
            if cache[-i] > 1:
                result.append(abs(i))
        else:
            cache[i] = 1

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
