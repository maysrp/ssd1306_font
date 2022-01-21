import framebuf
class Font(object):
    def __init__(self,display):
        self.file24 = open('ASC24', 'rb')
        self.file32 = open('ASC32', 'rb')
        self.file16 = open('ASC16', 'rb')
        self.display=display
    def text(self,tx,x,y,size=16):
        for i in tx:
            if size==8:
                self.f8(i,x,y)
                x=x+8
            elif size==24:
                self.f24(i,x,y)
                x=x+12
            elif size==32:
                self.f32(i,x,y)
                x=x+16
            else:
                self.f16(i,x,y)
                x=x+8
    def p61(self,tx,x,y):
        c=list(tx)
        c.reverse()
        tx=''.join(c)
        x=128-8*len(tx)
        for i in tx:
            self.f16t(i,x,y)
            x=x+8

    def f8(self,alp,x,y):
        self.display.text(alp,x,y,1)
    def f16(self,alp,x,y):
        self.file16.seek(ord(alp) * 16)
        font_code = self.file16.read(16)
        fb = framebuf.FrameBuffer(bytearray(font_code), 8, 16, framebuf.MONO_HLSB)
        self.display.blit(fb, x, y)
    def f16t(self,alp,x,y):
        self.file16.seek(ord(alp) * 16)
        font_code = self.file16.read(16)
        fb = framebuf.FrameBuffer(bytearray(font_code), 8, 16, framebuf.MONO_HMSB)
        self.display.blit(fb, x, y)
    def f24(self,alp,x,y):
        self.file24.seek((ord(alp)-32) * 36)
        font_code = self.file24.read(36)
        fb = framebuf.FrameBuffer(bytearray(font_code), 12, 24, framebuf.MONO_VLSB)
        self.display.blit(fb, x, y)
    def f32(self,alp,x,y):
        self.file32.seek((ord(alp)) * 64)
        font_code = self.file32.read(64)
        fb = framebuf.FrameBuffer(bytearray(font_code), 16, 32, framebuf.MONO_HLSB)
        self.display.blit(fb, x, y)
    def show(self):
        self.display.show()
    