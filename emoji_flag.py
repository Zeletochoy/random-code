import sys

def flag(country_code):
    return "".join(chr(ord(c) + 127397) for c in country_code.upper())

if __name__ == "__main__":
    print(flag(sys.argv[1]))
