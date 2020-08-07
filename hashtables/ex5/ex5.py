# Your code here

# def finder(files, queries):
# cache = {}
# res = []
# for i in files:
#     cache[i.split('/')[-1]] = i
# for j in queries:
#     if j in cache.keys():
#         res.append(cache[j])
# return res
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


def finder(files, queries):
    cache = {}
    res = []
    for i in files:
        if i.split('/')[-1] in cache.keys():
            node = cache[i.split('/')[-1]]
            if node.next == None:
                node.next = Node(i.split('/')[-1], i)
            else:
                while node.next:
                    node = node.next
                node.next = Node(i.split('/')[-1], cache[i.split('/')[-1]])
        else:
            cache[i.split('/')[-1]] = Node(i.split('/')
                                           [-1], i)
    for j in queries:
        if j in cache.keys():
            node = cache[j]
            res.append(node.value)
            while node.next:
                node = node.next
                res.append(node.value)

    return res


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz',
        '/usr2/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
