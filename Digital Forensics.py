# Given: String consisting of upper-case letters
# Compute: 8-bit checksum of the string

# Function to convert a binary number (input as a string)
# into a decimal number
def bin_to_decimal(binary):
    # Initialize accumulator
    decimal = 0
    # Loop for the length of the string
    for i in range(len(binary)):
        # Compute the power of 2 for the position in the binary number
        power = len(binary) - i - 1
        # Add the power of 2 to the decimal if there is a 1 in the position
        if binary[i] == '1':
            decimal = decimal + 2**power
    return decimal

 

# Function to look up the ASCII representation of a capital letter
# Note: This function only considers capital letters and a space character
def ascii_lookup(ch):
    if ch == 'A':
        return "01000001"
    elif ch == 'B':
        return "01000010"
    elif ch == 'C':
        return "01000011"
    elif ch == 'D':
        return "01000100"
    elif ch == 'E':
        return "01000101"
    elif ch == 'F':
        return "01000110"
    elif ch == 'G':
        return "01000111"
    elif ch == 'H':
        return "01001000"
    elif ch == 'I':
        return "01001001"
    elif ch == 'J':
        return "01001010"
    elif ch == 'K':
        return "01001011"
    elif ch == 'L':
        return "01001100"
    elif ch == 'M':
        return "01001101"
    elif ch == 'N':
        return "01001110"
    elif ch == 'O':
        return "01001111"
    elif ch == 'P':
        return "01010000"
    elif ch == 'Q':
        return "01010001"
    elif ch == 'R':
        return "01010010"
    elif ch == 'S':
        return "01010011"
    elif ch == 'T':
        return "01010100"
    elif ch == 'U':
        return "01010101"
    elif ch == 'V':
        return "01010110"
    elif ch == 'W':
        return "01010111"
    elif ch == 'X':
        return "01011000"
    elif ch == 'Y':
        return "01011001"
    elif ch == 'Z':
        return "01011010"
    elif ch == ' ':
        return "00100000"

def checksumAdler16(string):
    #initialize your variable
    a = 1
    b = 0
    #this is a for loop to loop through eachletter 
    for i in string:
        #lookup the binary for eachletter
        aScii = ascii_lookup(i)
        #get the decimal for the llibrary with first function
        dec = bin_to_decimal(aScii)
        a = (a + dec) % 65521
        b = (b + a) % 65521
        #get checksum
        checksum = (b * 65536) + a

    #return checksum
    return checksum
