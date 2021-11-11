from manim import * 
import manim

variable = '          '
class formulas:
    a = f'SV = KV(1+{variable}) => {variable} = {variable}-1'
    aOffset = 3
    b = f'UV = SV(1-{variable}) => {variable} = 1-{variable}'
    bOffset = 1.5
    c = f''
    cOffset = 0

class main(Scene):
    def construct(self):
        self.create.text(self, txt=f'{formulas.a}', posX=0, posY=formulas.aOffset)
        self.create.divOver(self, posX=-1.05, posY=formulas.aOffset)
        self.create.divOver(self, posX=1.6, posY=formulas.aOffset)
        self.create.divOver(self, posX=3.7, posY=formulas.aOffset, top='SV', bottom='KV')

        self.create.text(self, txt=f'{formulas.b}', posX=0, posY=formulas.bOffset)
        self.create.divOver(self, posX=-1.05, posY=formulas.bOffset)
        self.create.divOver(self, posX=1.6, posY=formulas.bOffset)
        self.create.divOver(self, posX=3.7, posY=formulas.bOffset, top='UV', bottom='SV')
        self.wait(5)
    
    class create:
        def text(self, txt:str='', posX:float=0, posY:float=0):

            self.play(Create(Text(txt).set_x(posX).set_y(posY)))
        def divOver(self, posX:float=0, posY:float=0, top:str='P', bottom:str='100', sizeDiv=2):
            a = Text(top, font_size=DEFAULT_FONT_SIZE/sizeDiv)
            b = Text(bottom, font_size=DEFAULT_FONT_SIZE/sizeDiv)
            c = Line(LEFT, RIGHT)
            a.set_x(posX)
            b.set_x(posX)
            c.set_x(posX)
            a.set_y(.3+posY)
            b.set_y(-.3+posY)
            c.set_y(posY)
            c.set_length(2/sizeDiv)
            self.play(Create(a))
            self.play(Create(b))
            self.play(Create(c))
            return
    
