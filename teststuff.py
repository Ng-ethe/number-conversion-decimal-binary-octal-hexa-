def print_formatted(n):
    # your code goes 
    num = n
    for k in range(1, num+1):
        decimal = str(k)
        octal=''
        n=k
        while (n/8) > 0:
            rem = n%8
            octal= str(rem) + octal
            n=n//8
        

        n=k
        hexa =''
        while (n/16) > 0:
            rem = n%16
            if rem==10:
                rem='A'
            elif rem==11:
                rem='B'
            elif rem==12:
                rem='C'
            elif rem==13:
                rem='D'
            elif rem==14:
                rem='E'
            elif rem== 15:
                rem='F'
            hexa= str(rem) + hexa
            n=n//16
        
        n=k
        binary =''
        while (n/2) > 0:
            rem = n%2
            binary= str(rem) + binary
            n=n//2
        

        print(decimal+ "  " + octal + "  " + hexa + "  " + binary)
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)