#!/usr/bin/env python3
import argparse
import sys

ROMAN = {
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1
}


class RomanNumerals:
    @staticmethod
    def to_roman(val : int) -> str:
        def roman_num(val):
            for r in ROMAN:
                r_val = ROMAN[r]
                x, y = divmod(val, r_val)
                yield r * x
                val -= (r_val * x)
                if val <= 0:
                    break

        return "".join([a for a in roman_num(val)])

    @staticmethod
    def from_roman(roman_num : str) -> int:
        total = 0
        prev = 0

        for c in reversed(roman_num):
            c_val = ROMAN[c]
            if c_val >= prev:
                total += c_val
            else:
                total -= c_val
            prev = c_val
        return total


def main():
    parser = argparse.ArgumentParser(description='Roman Numeral Calculator')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-t', '--to-roman', type=int, help='Converts an integer to a roman numeral')
    group.add_argument('-f', '--from-roman', type=str, help='Converts a roman numeral to an integer')

    args = parser.parse_args()

    try:
        if args.to_roman:
            if args.to_roman < 1 or args.to_roman > 3999:
                print('Invalid number, must be between 1 and 3999')
                sys.exit(1)
            print(RomanNumerals.to_roman(args.to_roman))
        elif args.from_roman:
            valid_chars = set(ROMAN.keys())
            if not set(args.from_roman).issubset(valid_chars):
                print(f'Invalid Roman Numeral {args.to_roman}, valid characters are {valid_chars}')
                sys.exit(1)
            print(RomanNumerals.from_roman(args.from_roman))
    except Exception as e:
        print(f'Error: {e}')
        sys.exit(1)


if __name__ == '__main__':
    main()
