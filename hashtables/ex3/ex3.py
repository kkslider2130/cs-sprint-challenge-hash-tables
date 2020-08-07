def intersection(arrays):
    # return list(set(arrays[0]).intersection(*arrays))
    cache = {}
    res = []
    for i in arrays:
        for j in i:
            if j in cache.keys():
                cache[j] += 1
                if cache[j] == len(arrays):
                    res.append(j)

            else:
                cache[j] = 1
    return res


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
