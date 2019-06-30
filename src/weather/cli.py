from argparse import ArgumentParser

def create_parser():
    parser = ArgumentParser()
    parser.add_argument('city', help="City for weather")
    parser.add_argument('--country', default='us', help='Country of the city belongs to, default is "us"')
    return parser
