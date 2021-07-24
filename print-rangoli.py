def print_rangoli(size):
    # your code goes here
    chars = [chr(97+i) for i in range(size)]
    lines = ["-".join(chars[-i+1:][::-1]+chars[-i:]
                      if not i==1 else chars[-i:]).center(4*size-3,"-")
             for i in range (1,size+1)]
    print("\n".join(lines))
    print("\n".join(lines[:size-1][::-1]))
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

