#Convertion between diferent numerical basis

def decimal_to_binary(number: int):
    number_binary = ''
    while number != 0 and number != 1:
        number_binary += str(int(number%2))
        number = int(number/2)
    number_binary += str(int(number))
    return int(number_binary[::-1])

def binary_to_decimal(number: int):
    return sum(
        [ int(elem)*2**n for n, elem in enumerate(list(str(number)))[::-1] ]
        )