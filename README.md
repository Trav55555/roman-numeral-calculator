# Roman Numerals CLI Tool

A command-line utility for converting between Roman numerals and integers.

## Features

- Convert integers to Roman numerals
- Convert Roman numerals to integers
- Input validation and error handling

## Usage

### Converting Integers to Roman Numerals

```
python roman_converter.py -t NUMBER
```

or using the long option:

```
python roman_converter.py --to-roman NUMBER
```

Example:
```
$ python roman_converter.py -t 1984
MCMLXXXIV
```

### Converting Roman Numerals to Integers

```
python roman_converter.py -f ROMAN_NUMERAL
```

or using the long option:

```
python roman_converter.py --from-roman ROMAN_NUMERAL
```

Example:
```
$ python roman_converter.py -f MCMLXXXIV
1984
```

### Getting Help

```
$ python roman_converter.py --help
usage: roman_converter.py [-h] (-t TO_ROMAN | -f FROM_ROMAN)

Convert between Roman numerals and integers

options:
  -h, --help            show this help message and exit
  -t TO_ROMAN, --to-roman TO_ROMAN
                        Convert integer to Roman numeral
  -f FROM_ROMAN, --from-roman FROM_ROMAN
                        Convert Roman numeral to integer
```

## Limitations

- Integers must be between 1 and 3999
- Roman numerals must use valid characters: I, V, X, L, C, D, M

## Technical Details

The conversion uses the standard Roman numeral system:

| Symbol | Value |
|--------|-------|
| I      | 1     |
| IV     | 4     |
| V      | 5     |
| IX     | 9     |
| X      | 10    |
| XL     | 40    |
| L      | 50    |
| XC     | 90    |
| C      | 100   |
| CD     | 400   |
| D      | 500   |
| CM     | 900   |
| M      | 1000  |

## Examples

```
$ python roman_converter.py -t 42
XLII

$ python roman_converter.py -f CDXLIV
444

$ python roman_converter.py -t 3999
MMMCMXCIX
```

## Error Handling

The script provides clear error messages for invalid inputs:

```
$ python roman_converter.py -t 0
Error: Integer must be between 1 and 3999

$ python roman_converter.py -t 4000
Error: Integer must be between 1 and 3999

$ python roman_converter.py -f IIIIV
Error: Invalid Roman numeral. Valid characters are I, V, X, L, C, D, M
```

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
