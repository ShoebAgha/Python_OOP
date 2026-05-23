digits=list('FA1')

# power=len(digits)-1

# num_base10=0
# for face_val in digits:
#             if ord(face_val) < 58:
#                 place_val = (ord(face_val)-48)*(16**power)
#                 num_base10+=place_val
#                 power-=1
#             else:
#                 place_val = (ord(face_val)-65+10)*(16**power)
#                 num_base10+=place_val
#                 power-=1
num_base10=4001
toBase=16
converted=''
while num_base10 !=0:
                face_val=num_base10 % toBase
                if face_val < 10:
                    converted=str(face_val)+converted
                    num_base10=(num_base10-face_val)//toBase
                elif face_val > 9:
                    char=chr(face_val+65-10)
                    converted=char+converted
                    num_base10=(num_base10-face_val)//toBase
print(converted)
