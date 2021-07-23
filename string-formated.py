def print_formatted(number):
    # your code goes here
    width = len(bin(number)[2:]) #You can algo use number.bit_length()
    number_list = [" ".join([str(i).rjust(width),
                             oct(i)[2:].rjust(width),
                             hex(i).upper()[2:].rjust(width),
                             bin(i)[2:].rjust(width)]) for i in range(1,number+1)]
    print("\n".join(number_list))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
