from time import time


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
