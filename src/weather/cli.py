from argparse import ArgumentParser

def create_parser():
    parser = ArgumentParser()
    parser.add_argument('city', help="City for weather")
    parser.add_argument('--country', default='us', help='Country of the city belongs to, default is "us"')
    return parser

def main():
    import requests
    from weather import weather

    args = create_parser().parse_args()
    weather.get_weather("d4afb596768c77e175bb8136037eed6a", args.city, args.country)
