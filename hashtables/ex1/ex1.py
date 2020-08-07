

def get_indices_of_item_weights(weights, length, limit):
    cache = {}
    if length == 2 and sum(weights) == limit:
        if weights[0] > weights[1]:
            return (0, 1)
        elif weights[0] <= weights[1]:
            return (1, 0)
    else:

        res = None
        for i in range(0, length):
            cache[weights[i]] = i
        for k, v in cache.items():
            if limit-k in cache.keys():
                res = (v, cache[limit-k])
        return res
