import argparse
import sys

from os.path import join
from scipy.sparse import csr_matrix, save_npz


def run(argv):
    args = parse_args(argv)
    prepare_wishlist(args.path)
    prepare_gift_list(args.path)


def parse_args(argv):
    parser = argparse.ArgumentParser('Prepare happiness matrices')
    parser.add_argument('-p', '--path', default='./data', dest='path', help='Path to data files. (Defaults to "data/")')
    return parser.parse_args(argv)


def prepare_wishlist(path):
    matrix = csr_matrix(read_wishlist(path))
    save_npz(join(path, 'wishlists.npz'), matrix)


def prepare_gift_list(path):
    matrix = csr_matrix(read_gift_list(path)).T
    save_npz(join(path, 'giftlists.npz'), matrix)


def read_wishlist(path):
    result = []
    with open(join(path, 'child_wishlist_v2.csv')) as wishlist_file:
        for line in wishlist_file:
            tokens = line.split(',')[1:]
            happiness = [0] * 1000
            for index, gift_type_id in enumerate(tokens):
                happiness[int(gift_type_id)] = (len(tokens) - index) * 2 + 1
            result.append(happiness)
    return result


def read_gift_list(path):
    result = []
    with open(join(path, 'gift_goodkids_v2.csv')) as wishlist_file:
        for line in wishlist_file:
            tokens = line.split(',')[1:]
            happiness = [0] * 1000000
            for index, child_id in enumerate(tokens):
                happiness[int(child_id)] = (len(tokens) - index) * 2 + 1
            result.append(happiness)
    return result


if __name__ == '__main__':
    run(sys.argv[1:])
