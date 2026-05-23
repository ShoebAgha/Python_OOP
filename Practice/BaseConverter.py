

class Base:
    def __init__(self,number,fromBase, toBase):
        self.number=number
        self.fromBase=fromBase
        self.toBase=toBase
        self.checkCurrentBase()


    def checkCurrentBase(self):
        try:
            int(str(self.number),self.fromBase)
        
        except:
            raise ValueError("all digits must satisfy 0 <= d < input base")
    
        if self.fromBase < 2:
            raise ValueError("input base must be >= 2")
        elif self.fromBase < 2:
            raise ValueError('output base must be >= 2')
    
        else:
            return
    

    def baseCoverter(self):
        digits=str(self.number)
        num_base10 = 0
        power=len(digits)-1
        for face_val in digits:
            face_val=str(face_val)
            if ord(face_val) < 58:
                place_val = (ord(face_val)-48)*(self.fromBase**power)
                num_base10+=place_val
                power-=1
            else:
                place_val = (ord(face_val)-65+10)*(self.fromBase**power)
                num_base10+=place_val
                power-=1
        if self.toBase==10:
            return num_base10
        else:
            converted=''
            while num_base10 !=0:
                face_val=num_base10 % self.toBase
                if face_val < 10:
                    converted=str(face_val)+converted
                    num_base10=(num_base10-face_val)//self.toBase
                elif face_val > 9:
                    char=chr(face_val+65-10)
                    converted=char+converted
                    num_base10=(num_base10-face_val)//self.toBase
        return converted
        

base_obj=Base(42,10,16)
print(base_obj.baseCoverter())


        
        

    
    
    
