class Square:
    side = 1.0
    
    def setSide(self, side):
        if side < 0:
            self.side = 0
            print("Side: ", self.side)
        else:
            self.side = side
            print("Side: ", self.side)
        
side1 = Square(-6)
side2 = Square(5)

side1.setSide()
side2.setSide()