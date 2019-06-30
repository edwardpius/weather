import pytest

from weather import cli

city = "seattle"
country = "us"

@pytest.fixture
def parser():
    return cli.create_parser()

def test_parser_without_city(parser):
    """
    Without a specific city the parser will exit
    """
    with pytest.raises(SystemExit):
        parser.parse_args(city)

def test_parser_with_country(parser):
    """
    The parser will exit if it receives a country without a name
    """
    with pytest.raises(SystemExit):
        parser.parse_args([city, country])

def test_parser_with_city_and_country(parser):
    """
    The parser will not exit if it received a city and country
    """
    args = parser.parse_args([city, '--country', 'us'])

    assert args.city == city
    assert args.country == country
