def scan(src):
    tokens = []
    i = 0
    while i < len(src):
        c = src[i]
        # Recognizing identifiers (ID) 
        # If is a combination of alphanumeric characters and underscores, 
        # and starting with a letter or underscore, then it is an ID
        # Recognizing comments (COMMENTS)
        if c == '/' and i + 1 < len(src) and src[i + 1] == '/':
            # Skip the comment until the end of the line '\n'
            while i < len(src) and src[i] != '\n':
                i += 1
            continue
        elif c.isalpha() or c == '_':
            start = i
            while i < len(src) and (src[i].isalnum() or src[i] == '_'):
                i += 1
            id = src[start:i]
            # Recognizing keywords (KEYWORDS)
            if id in ["if", "while", "return", "int"]:
                tokens.append(("KEYWORD", id))
            # Else assign it as an identifier (ID)
            else:
                tokens.append(("ID", id))
            continue
        # Recognizing numbers and floating-point numbers (NUMBERS)
        # If the character is a dot followed by a digit, then it is a floating-point number
        elif c.isdigit() or (c == '.' and i + 1 < len(src) and src[i + 1].isdigit()):
            start = i
            while i < len(src) and src[i].isdigit():
                i += 1
            # Check for floating-point numbers
            # if the next character is a dot, then it is a floating-point number
            if i < len(src) and src[i] == '.':
                i += 1
                # Check if the next character is a digit, if not, raise an error
                if i < len(src) and src[i].isdigit():
                    # Loop through the digits after the dot and append the float 
                    while i < len(src) and src[i].isdigit():
                        i += 1
                    tokens.append(("FLOAT", float(src[start:i])))
                else:
                    # If the next character is not a digit, raise an error
                    raise ValueError(f"Invalid floating-point number: {src[start:i]}")
            else:
                # If the next character is not a dot, then it is an integer number
                tokens.append(("NUMBER", int(src[start:i])))
            continue
        # Recognizing symbols/operators (SYMBOLS)
        elif c in ['+', '-', '*', '/', '=', '>', '<', ';', '(', ')', '==', '!=', '>=', '<=']:
            tokens.append(("SYMBOL", c))
            i += 1
            continue
        # Ignore if whitespace
        elif c.isspace():
            i += 1
            continue
        else:
            raise ValueError(f"Invalid character: {c}")
        i += 1
    tokens.append(("EOF", None))
    return tokens

print("1:" + str(scan("xuawdhuh_2q8ho = 23042 + _aiAWodh_y;")))
print("2:" + str(scan("if (x > .4372) return x;")))
print("3:" + str(scan("while (x < 10.33427) x = x + 1; //This is a comment\n return x;")))    
print("4:" + str(scan("$invalid_token")))

