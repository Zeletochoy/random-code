import click


def flag(country_code):
    return "".join(chr(ord(c) + 127397) for c in country_code.upper())


@click.command()
@click.argument("country_code")
def cli(country_code):
    print(flag(country_code))
