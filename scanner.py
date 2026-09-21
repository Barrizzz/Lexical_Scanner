def scan(src):
    tokens = []
    i = 0
    line_num = 1
    col_num = 1

    KEYWORDS = {
        "if", "while", "return", "int", "def", "class", "True", "False", 
        "None", "and", "or", "not", "for", "in", "elif", "else", "break"
    }
    SYMBOLS = {
        '+', '-', '*', '/', '=', '>', '<', ';', '(', ')', '==', '!=', '>=', '<=', ':','"', '!'
    }

    # Helper function to advance the index and update line and column numbers
    def advance():
        nonlocal i, col_num, line_num
        if i < len(src):
            if src[i] == '\n':
                line_num += 1
                col_num = 1
            else:
                col_num += 1
            i += 1
        
    while i < len(src):
        c = src[i]
        # Recognizing identifiers (ID) 
        # If is a combination of alphanumeric characters and underscores, 
        # and starting with a letter or underscore, then it is an ID
        # Recognizing comments (COMMENTS)
        if c == '/' and i + 1 < len(src) and src[i + 1] == '/':
            # Skip the comment until the end of the line '\n'
            while i < len(src) and src[i] != '\n':
                advance()
            continue

        elif c.isalpha() or c == '_':
            start = i
            while i < len(src) and (src[i].isalnum() or src[i] == '_'):
                advance()
            id = src[start:i]
            # Recognizing keywords (KEYWORDS)
            if id in [KEYWORDS]:
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
                advance()
            # Check for floating-point numbers
            # if the next character is a dot, then it is a floating-point number
            if i < len(src) and src[i] == '.':
                advance()
                # Check if the next character is a digit, if not, raise an error
                if i < len(src) and src[i].isdigit():
                    # Loop through the digits after the dot and append the float 
                    while i < len(src) and src[i].isdigit():
                        advance()
                    tokens.append(("FLOAT", float(src[start:i])))
                else:
                    # If the next character is not a digit, raise an error
                    raise ValueError(f"Invalid floating-point number: {src[start:i]}")
            else:
                # If the next character is not a dot, then it is an integer number
                tokens.append(("NUMBER", int(src[start:i])))
            continue

        # Recognizing symbols/operators (SYMBOLS)
        elif c in SYMBOLS:
            tokens.append(("SYMBOL", c))
            advance()
            continue

        # Ignore if whitespace
        elif c.isspace():
            advance()
            continue

        else:
            raise ValueError(f"Line {line_num}, Column {col_num}: Illegal character '{c}'")
    tokens.append(("EOF", None))
    return tokens 

source_code = """
// This is a comment, it should ignore this line
def check_value(x):
    if x >= 3.14:
        return "High"
    elif x != 0:
        return "Low"
"""

print(scan(source_code))