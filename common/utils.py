from time import time


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def print_time(func):
    def wrappers(*args, **kwargs):
        start = time()
        print('func: {}'.format(func.__name__))
        print('result: {}'.format(func(*args, **kwargs)))
        end = time()
        print("spent time:%.4f" % ((end - start) * 1000))
        print("***************")

    return wrappers


def exchange_maskint(mask_int):
    bin_arr = ['0' for i in range(32)]
    for i in range(mask_int):
        bin_arr[i] = '1'
    tmp_mask = [''.join(bin_arr[i * 8:i * 8 + 8]) for i in range(4)]
    tmp_mask = [str(int(tmp_str, 2)) for tmp_str in tmp_mask]
    return '.'.join(tmp_mask)


if __name__ == '__main__':
    print(exchange_maskint(8))
