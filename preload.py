
def preload(parser):
    parser.add_argument("--wildcards-dir", type=str, help="directory with wildcards", default=None)
    parser.add_argument("--wildcards-start", type=str, help="index of first item to take", default=None)
    parser.add_argument("--wildcards-count", type=str, help="number of items to take", default=None)
