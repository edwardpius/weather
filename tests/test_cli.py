import pytest

from weather import cli

city = "seattle"

def test_parser_without_city():
    """
    Without a specific city the parser will exit
    """
    with pytest.raises(SystemExit):
        parser = cli.create_parser()
        parser.parse_args([city])

def test_parser_with_country():
    """
    The parser will exit if it receives a country without a name
    """
    parser = cli.create_parser()
    with pytest.raises(SystemExit):
        parser.parse_args([city, "--country", "us"])

def test_parser_with_city_and_country():
    """
    The parser will not exit if it received a city and country
    """
    parser = cli.create_parser()

    args = parser.parse_args([city, '--country', 'us'])

    assert args.city == city
    assert args.country == 'us'
