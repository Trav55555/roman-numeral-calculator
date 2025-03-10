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
