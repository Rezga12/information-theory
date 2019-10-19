import sys
import heapq


class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def __lt__(self, other):
        return self.value < other.value


def rec(root, probs, so_far):
    if root.left is None and root.right is None:
        val = root.value
        index = probs.index(val)
        probs[index] = so_far
    else:
        rec(root.right, probs, so_far + '1')
        rec(root.left, probs, so_far + '0')


def main():
    file = open(sys.argv[1])
    file.readline()
    probs = list(map(float, file.readline().split(' ')))
    ps = list(map(Node, probs))
    #print(probs)
    heapq.heapify(ps)

    while len(ps) > 1:
        node_right = heapq.heappop(ps)
        node_left = heapq.heappop(ps)

        node = Node(node_left.value + node_right.value)
        node.right = node_right
        node.left = node_left
        heapq.heappush(ps, node)

    root = heapq.heappop(ps)
    rec(root, probs, '')

    output = open(sys.argv[2], 'w+')
    for x in probs:
        output.write(str(x) + '\n')



if __name__ == "__main__":
    main()
