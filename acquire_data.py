from __future__ import division, print_function
import sys
import argparse
try:
    from urllib.request import urlretrieve
except ImportError:  # python2
    from urllib2 import urlretrieve


def parse_args(argv):
    parser = argparse.ArgumentParser()

    args = parser.parse_args(argv)
    return args


def main():
    args = parse_args(sys.argv[1:])

    print("Downloading iris data")
    iris_dataset_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    local_filename = "raw/iris.csv"
    returned_filename, response_headers = urlretrieve(iris_dataset_url, local_filename)


if __name__ == '__main__':
    main()