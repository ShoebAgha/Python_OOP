def reverse(x: int):
        if x<0:
            sign=-1
        else:
            sign=1
        x=x*sign
        reverse_int=0
        while x!=0:
            unit_place=x%10
            reverse_int=reverse_int*10+unit_place
            x=x//10
        if reverse_int*sign > 0x7FFFFFFF or reverse_int*sign < -0x80000000:
             return 0
        return reverse_int*sign

print(reverse((4294967295000)))