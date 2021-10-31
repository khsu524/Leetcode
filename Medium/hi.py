def vanity(codes, numbers):
    vanity_map = {
        "A": 2, "B": 2, "C": 2,
        "D": 3, "E": 3, "F": 3,
        "G": 4, "H": 4, "I": 4,
        "J": 5, "K": 5, "L": 5,
        "M": 6, "N": 6, "O": 6,
        "P": 7, "Q": 7, "R": 7,"S": 7, 
        "T": 8, "U": 8,"V": 8, 
        "W": 9, "X": 9, "Y": 9, "Z": 9, 
    }
    res = []
    
    num_list = []
    
    for code in codes:
        num_to_search = []
        for letter in code:
            num_to_search.append(str(vanity_map[letter]))
            # Now i know what to search for
        
        num_str = "".join(num_to_search)
        print(num_str)
        num_list.append(num_str)
            
    
    for num in numbers:
        for num_str_2 in num_list:
            if num_str_2 in num:
                res.append(num)
    
    return res

codes = ["TWLO"]
numbers = ["+17474824380",
"+14157088956",
"+919810155555",
"+15109926333",
"+1415123456"
]
vanity(codes, numbers)