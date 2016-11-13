import re

class Cube:
    def __init__(self):
        self.u = ['W','W','W','W','W','W','W','W','W']
        self.l = ['O','O','O','O','O','O','O','O','O']
        self.f = ['G','G','G','G','G','G','G','G','G']
        self.r = ['R','R','R','R','R','R','R','R','R']
        self.b = ['B','B','B','B','B','B','B','B','B']
        self.d = ['Y','Y','Y','Y','Y','Y','Y','Y','Y']
        self.moves = ""
        self.cc = 8
        self.ec = 12

    def __repr__(self):
        return "U: %s\nL: %s\nF: %s\nR: %s\nB: %s\nD: %s\nMoves: %s\nCC: %d\nEC: %d" %(self.u, self.l, self.f, self.r, self.b, self.d, self.moves, self.cc, self.ec)

    def right(self,mod=""):
        old_u = [self.u[2],self.u[5],self.u[8]]
        old_f = [self.f[2],self.f[5],self.f[8]]
        old_b = [self.b[0],self.b[3],self.b[6]]
        old_d = [self.d[2],self.d[5],self.d[8]]
        if mod == "":
            new_r = [self.r[6],self.r[3],self.r[0],self.r[7],self.r[4],self.r[1],self.r[8],self.r[5],self.r[2]]
            self.u[2]=old_f[0];self.u[5]=old_f[1];self.u[8]=old_f[2]
            self.f[2]=old_d[0];self.f[5]=old_d[1];self.f[8]=old_d[2]
            self.b[0]=old_u[2];self.b[3]=old_u[1];self.b[6]=old_u[0]
            self.d[2]=old_b[2];self.d[5]=old_b[1];self.d[8]=old_b[0]
        elif mod == "'":
            new_r = [self.r[2],self.r[5],self.r[8],self.r[1],self.r[4],self.r[7],self.r[0],self.r[3],self.r[6]]
            self.u[2]=old_b[2];self.u[5]=old_b[1];self.u[8]=old_b[0]
            self.f[2]=old_u[0];self.f[5]=old_u[1];self.f[8]=old_u[2]
            self.b[0]=old_d[2];self.b[3]=old_d[1];self.b[6]=old_d[0]
            self.d[2]=old_f[0];self.d[5]=old_f[1];self.d[8]=old_f[2]
        elif mod == "2":
            new_r = [self.r[8],self.r[7],self.r[6],self.r[5],self.r[4],self.r[3],self.r[2],self.r[1],self.r[0]]
            self.u[2]=old_d[0];self.u[5]=old_d[1];self.u[8]=old_d[2]
            self.f[2]=old_b[2];self.f[5]=old_b[1];self.f[8]=old_b[0]
            self.b[0]=old_f[2];self.b[3]=old_f[1];self.b[6]=old_f[0]
            self.d[2]=old_u[0];self.d[5]=old_u[1];self.d[8]=old_u[2]
        self.r = new_r

    def left(self,mod=""):
        old_u = [self.u[0],self.u[3],self.u[6]]
        old_f = [self.f[0],self.f[3],self.f[6]]
        old_b = [self.b[2],self.b[5],self.b[8]]
        old_d = [self.d[0],self.d[3],self.d[6]]
        if mod == "":
            new_l = [self.l[6],self.l[3],self.l[0],self.l[7],self.l[4],self.l[1],self.l[8],self.l[5],self.l[2]]
            self.u[0]=old_b[2];self.u[3]=old_b[1];self.u[6]=old_b[0]
            self.f[0]=old_u[0];self.f[3]=old_u[1];self.f[6]=old_u[2]
            self.b[2]=old_d[2];self.b[5]=old_d[1];self.b[8]=old_d[0]
            self.d[0]=old_f[0];self.d[3]=old_f[1];self.d[6]=old_f[2]
        elif mod == "'":
            new_l = [self.l[2],self.l[5],self.l[8],self.l[1],self.l[4],self.l[7],self.l[0],self.l[3],self.l[6]]
            self.u[0]=old_f[0];self.u[3]=old_f[1];self.u[6]=old_f[2]
            self.f[0]=old_d[0];self.f[3]=old_d[1];self.f[6]=old_d[2]
            self.b[2]=old_u[2];self.b[5]=old_u[1];self.b[8]=old_u[0]
            self.d[0]=old_b[2];self.d[3]=old_b[1];self.d[6]=old_b[0]
        elif mod == "2":
            new_l = [self.l[8],self.l[7],self.l[6],self.l[5],self.l[4],self.l[3],self.l[2],self.l[1],self.l[0]]
            self.u[0]=old_d[0];self.u[3]=old_d[1];self.u[6]=old_d[2]
            self.f[0]=old_b[2];self.f[3]=old_b[1];self.f[6]=old_b[0]
            self.b[2]=old_f[2];self.b[5]=old_f[1];self.b[8]=old_f[0]
            self.d[0]=old_u[0];self.d[3]=old_u[1];self.d[6]=old_u[2]
        self.l = new_l

    def up(self,mod=""):
        old_l = [self.l[0],self.l[1],self.l[2]]
        old_f = [self.f[0],self.f[1],self.f[2]]
        old_r = [self.r[0],self.r[1],self.r[2]]
        old_b = [self.b[0],self.b[1],self.b[2]]
        if mod == "":
            new_u = [self.u[6],self.u[3],self.u[0],self.u[7],self.u[4],self.u[1],self.u[8],self.u[5],self.u[2]]
            self.l[0]=old_f[0];self.l[1]=old_f[1];self.l[2]=old_f[2]
            self.f[0]=old_r[0];self.f[1]=old_r[1];self.f[2]=old_r[2]
            self.r[0]=old_b[0];self.r[1]=old_b[1];self.r[2]=old_b[2]
            self.b[0]=old_l[0];self.b[1]=old_l[1];self.b[2]=old_l[2]
        elif mod == "'":
            new_u = [self.u[2],self.u[5],self.u[8],self.u[1],self.u[4],self.u[7],self.u[0],self.u[3],self.u[6]]
            self.l[0]=old_b[0];self.l[1]=old_b[1];self.l[2]=old_b[2]
            self.f[0]=old_l[0];self.f[1]=old_l[1];self.f[2]=old_l[2]
            self.r[0]=old_f[0];self.r[1]=old_f[1];self.r[2]=old_f[2]
            self.b[0]=old_r[0];self.b[1]=old_r[1];self.b[2]=old_r[2]
        elif mod == "2":
            new_u = [self.u[8],self.u[7],self.u[6],self.u[5],self.u[4],self.u[3],self.u[2],self.u[1],self.u[0]]
            self.l[0]=old_r[0];self.l[1]=old_r[1];self.l[2]=old_r[2]
            self.f[0]=old_b[0];self.f[1]=old_b[1];self.f[2]=old_b[2]
            self.r[0]=old_l[0];self.r[1]=old_l[1];self.r[2]=old_l[2]
            self.b[0]=old_f[0];self.b[1]=old_f[1];self.b[2]=old_f[2]
        self.u = new_u

    def front(self,mod=""):
        old_l = [self.l[2],self.l[5],self.l[8]]
        old_u = [self.u[6],self.u[7],self.u[8]]
        old_r = [self.r[0],self.r[3],self.r[6]]
        old_d = [self.d[0],self.d[1],self.d[2]]
        if mod == "":
            new_f = [self.f[6],self.f[3],self.f[0],self.f[7],self.f[4],self.f[1],self.f[8],self.f[5],self.f[2]]
            self.l[2]=old_d[0];self.l[5]=old_d[1];self.l[8]=old_d[2]
            self.u[6]=old_l[2];self.u[7]=old_l[1];self.u[8]=old_l[0]
            self.r[0]=old_u[0];self.r[3]=old_u[1];self.r[6]=old_u[2]
            self.d[0]=old_r[2];self.d[1]=old_r[1];self.d[2]=old_r[0]
        elif mod == "'":
            new_f = [self.f[2],self.f[5],self.f[8],self.f[1],self.f[4],self.f[7],self.f[0],self.f[3],self.f[6]]
            self.l[2]=old_u[2];self.l[5]=old_u[1];self.l[8]=old_u[0]
            self.u[6]=old_r[0];self.u[7]=old_r[1];self.u[8]=old_r[2]
            self.r[0]=old_d[2];self.r[3]=old_d[1];self.r[6]=old_d[0]
            self.d[0]=old_l[0];self.d[1]=old_l[1];self.d[2]=old_l[2]
        elif mod == "2":
            new_f = [self.f[8],self.f[7],self.f[6],self.f[5],self.f[4],self.f[3],self.f[2],self.f[1],self.f[0]]
            self.l[2]=old_r[2];self.l[5]=old_r[1];self.l[8]=old_r[0]
            self.u[6]=old_d[2];self.u[7]=old_d[1];self.u[8]=old_d[0]
            self.r[0]=old_l[2];self.r[3]=old_l[1];self.r[6]=old_l[0]
            self.d[0]=old_u[2];self.d[1]=old_u[1];self.d[2]=old_u[0]
        self.f = new_f

    def down(self,mod=""):
        old_l = [self.l[6],self.l[7],self.l[8]]
        old_f = [self.f[6],self.f[7],self.f[8]]
        old_r = [self.r[6],self.r[7],self.r[8]]
        old_b = [self.b[6],self.b[7],self.b[8]]
        if mod == "":
            new_d = [self.d[6],self.d[3],self.d[0],self.d[7],self.d[4],self.d[1],self.d[8],self.d[5],self.d[2]]
            self.l[6]=old_b[0];self.l[7]=old_b[1];self.l[8]=old_b[2]
            self.f[6]=old_l[0];self.f[7]=old_l[1];self.f[8]=old_l[2]
            self.r[6]=old_f[0];self.r[7]=old_f[1];self.r[8]=old_f[2]
            self.b[6]=old_r[0];self.b[7]=old_r[1];self.b[8]=old_r[2]
        elif mod == "'":
            new_d = [self.d[2],self.d[5],self.d[8],self.d[1],self.d[4],self.d[7],self.d[0],self.d[3],self.d[6]]
            self.l[6]=old_f[0];self.l[7]=old_f[1];self.l[8]=old_f[2]
            self.f[6]=old_r[0];self.f[7]=old_r[1];self.f[8]=old_r[2]
            self.r[6]=old_b[0];self.r[7]=old_b[1];self.r[8]=old_b[2]
            self.b[6]=old_l[0];self.b[7]=old_l[1];self.b[8]=old_l[2]
        elif mod == "2":
            new_d = [self.d[8],self.d[7],self.d[6],self.d[5],self.d[4],self.d[3],self.d[2],self.d[1],self.d[0]]
            self.l[6]=old_r[0];self.l[7]=old_r[1];self.l[8]=old_r[2]
            self.f[6]=old_b[0];self.f[7]=old_b[1];self.f[8]=old_b[2]
            self.r[6]=old_l[0];self.r[7]=old_l[1];self.r[8]=old_l[2]
            self.b[6]=old_f[0];self.b[7]=old_f[1];self.b[8]=old_f[2]
        self.d = new_d

    def back(self,mod=""):
        old_l = [self.l[0],self.l[3],self.l[6]]
        old_u = [self.u[0],self.u[1],self.u[2]]
        old_r = [self.r[2],self.r[5],self.r[8]]
        old_d = [self.d[6],self.d[7],self.d[8]]
        if mod == "":
            new_b = [self.b[6],self.b[3],self.b[0],self.b[7],self.b[4],self.b[1],self.b[8],self.b[5],self.b[2]]
            self.l[0]=old_u[2];self.l[3]=old_u[1];self.l[6]=old_u[0]
            self.u[0]=old_r[0];self.u[1]=old_r[1];self.u[2]=old_r[2]
            self.r[2]=old_d[2];self.r[5]=old_d[1];self.r[8]=old_d[0]
            self.d[6]=old_l[0];self.d[7]=old_l[1];self.d[8]=old_l[2]
        elif mod == "'":
            new_b = [self.b[2],self.b[5],self.b[8],self.b[1],self.b[4],self.b[7],self.b[0],self.b[3],self.b[6]]
            self.l[0]=old_d[0];self.l[3]=old_d[1];self.l[6]=old_d[2]
            self.u[0]=old_l[2];self.u[1]=old_l[1];self.u[2]=old_l[0]
            self.r[2]=old_u[0];self.r[5]=old_u[1];self.r[8]=old_u[2]
            self.d[6]=old_r[2];self.d[7]=old_r[1];self.d[8]=old_r[0]
        elif mod == "2":
            new_b = [self.b[8],self.b[7],self.b[6],self.b[5],self.b[4],self.b[3],self.b[2],self.b[1],self.b[0]]
            self.l[0]=old_r[2];self.l[3]=old_r[1];self.l[6]=old_r[0]
            self.u[0]=old_d[2];self.u[1]=old_d[1];self.u[2]=old_d[0]
            self.r[2]=old_l[2];self.r[5]=old_l[1];self.r[8]=old_l[0]
            self.d[6]=old_u[2];self.d[7]=old_u[1];self.d[8]=old_u[0]
        self.b = new_b

    def mid(self,mod=""):
        old_u = [self.u[1],self.u[4],self.u[7]]
        old_f = [self.f[1],self.f[4],self.f[7]]
        old_d = [self.d[1],self.d[4],self.d[7]]
        old_b = [self.b[1],self.b[4],self.b[7]]
        if mod == "":
            self.u[1]=old_b[2];self.u[4]=old_b[1];self.u[7]=old_b[0]
            self.f[1]=old_u[0];self.f[4]=old_u[1];self.f[7]=old_u[2]
            self.d[1]=old_f[0];self.d[4]=old_f[1];self.d[7]=old_f[2]
            self.b[1]=old_d[2];self.b[4]=old_d[1];self.b[7]=old_d[0]
        elif mod == "'":
            self.u[1]=old_f[0];self.u[4]=old_f[1];self.u[7]=old_f[2]
            self.f[1]=old_d[0];self.f[4]=old_d[1];self.f[7]=old_d[2]
            self.d[1]=old_b[2];self.d[4]=old_b[1];self.d[7]=old_b[0]
            self.b[1]=old_u[2];self.b[4]=old_u[1];self.b[7]=old_u[0]
        elif mod == "2":
            self.u[1]=old_d[0];self.u[4]=old_d[1];self.u[7]=old_d[2]
            self.f[1]=old_b[2];self.f[4]=old_b[1];self.f[7]=old_b[0]
            self.d[1]=old_u[0];self.d[4]=old_u[1];self.d[7]=old_u[2]
            self.b[1]=old_f[2];self.b[4]=old_f[1];self.b[7]=old_f[0]

    def rWide(self,mod=""):
        self.right(mod)
        if mod == "'": self.mid()
        elif mod == "": self.mid("'")
        else: self.mid(mod)

    def lWide(self,mod=""):
        self.left(mod)
        self.mid(mod)

    def fWide(self,mod=""):
        self.front(mod)
        old_l = [self.l[1],self.l[4],self.l[7]]
        old_u = [self.u[3],self.u[4],self.u[5]]
        old_r = [self.r[1],self.r[4],self.r[7]]
        old_d = [self.d[3],self.d[4],self.d[5]]
        if mod == "":
            self.l[1]=old_d[0];self.l[4]=old_d[1];self.l[7]=old_d[2]
            self.u[3]=old_l[2];self.u[4]=old_l[1];self.u[5]=old_l[0]
            self.r[1]=old_u[0];self.r[4]=old_u[1];self.r[7]=old_u[2]
            self.d[3]=old_r[2];self.d[4]=old_r[1];self.d[5]=old_r[0]
        elif mod == "'":
            self.l[1]=old_u[2];self.l[4]=old_u[1];self.l[7]=old_u[0]
            self.u[3]=old_r[0];self.u[4]=old_r[1];self.u[5]=old_r[2]
            self.r[1]=old_d[2];self.r[4]=old_d[1];self.r[7]=old_d[0]
            self.d[3]=old_l[0];self.d[4]=old_l[1];self.d[5]=old_l[2]
        elif mod == "2":
            self.l[1]=old_r[2];self.l[4]=old_r[1];self.l[7]=old_r[0]
            self.u[3]=old_d[2];self.u[4]=old_d[1];self.u[5]=old_d[0]
            self.r[1]=old_l[2];self.r[4]=old_l[1];self.r[7]=old_l[0]
            self.d[3]=old_u[2];self.d[4]=old_u[1];self.d[5]=old_u[0]

    def rotX(self, mod=""):
        if mod == "":
            new_u = [self.f[0],self.f[1],self.f[2],self.f[3],self.f[4],self.f[5],self.f[6],self.f[7],self.f[8]]
            new_l = [self.l[2],self.l[5],self.l[8],self.l[1],self.l[4],self.l[7],self.l[0],self.l[3],self.l[6]]
            new_f = [self.d[0],self.d[1],self.d[2],self.d[3],self.d[4],self.d[5],self.d[6],self.d[7],self.d[8]]
            new_r = [self.r[6],self.r[3],self.r[0],self.r[7],self.r[4],self.r[1],self.r[8],self.r[5],self.r[2]]
            new_b = [self.u[8],self.u[7],self.u[6],self.u[5],self.u[4],self.u[3],self.u[2],self.u[1],self.u[0]]
            new_d = [self.b[8],self.b[7],self.b[6],self.b[5],self.b[4],self.b[3],self.b[2],self.b[1],self.b[0]]
        elif mod == "'":
            new_u = [self.b[8],self.b[7],self.b[6],self.b[5],self.b[4],self.b[3],self.b[2],self.b[1],self.b[0]]
            new_l = [self.l[6],self.l[3],self.l[0],self.l[7],self.l[4],self.l[1],self.l[8],self.l[5],self.l[2]]
            new_f = [self.u[0],self.u[1],self.u[2],self.u[3],self.u[4],self.u[5],self.u[6],self.u[7],self.u[8]]
            new_r = [self.r[2],self.r[5],self.r[8],self.r[1],self.r[4],self.r[7],self.r[0],self.r[3],self.r[6]]
            new_b = [self.d[8],self.d[7],self.d[6],self.d[5],self.d[4],self.d[3],self.d[2],self.d[1],self.d[0]]
            new_d = [self.f[0],self.f[1],self.f[2],self.f[3],self.f[4],self.f[5],self.f[6],self.f[7],self.f[8]]
        elif mod == "2":
            new_u = [self.d[0],self.d[1],self.d[2],self.d[3],self.d[4],self.d[5],self.d[6],self.d[7],self.d[8]]
            new_l = [self.l[8],self.l[7],self.l[6],self.l[5],self.l[4],self.l[3],self.l[2],self.l[1],self.l[0]]
            new_f = [self.b[8],self.b[7],self.b[6],self.b[5],self.b[4],self.b[3],self.b[2],self.b[1],self.b[0]]
            new_r = [self.r[8],self.r[7],self.r[6],self.r[5],self.r[4],self.r[3],self.r[2],self.r[1],self.r[0]]
            new_b = [self.f[8],self.f[7],self.f[6],self.f[5],self.f[4],self.f[3],self.f[2],self.f[1],self.f[0]]
            new_d = [self.u[0],self.u[1],self.u[2],self.u[3],self.u[4],self.u[5],self.u[6],self.u[7],self.u[8]]
        self.u = new_u
        self.l = new_l
        self.f = new_f
        self.r = new_r
        self.b = new_b
        self.d = new_d

    def rotY(self, mod=""):
        if mod == "":
            new_u = [self.u[6],self.u[3],self.u[0],self.u[7],self.u[4],self.u[1],self.u[8],self.u[5],self.u[2]]
            new_l = [self.f[0],self.f[1],self.f[2],self.f[3],self.f[4],self.f[5],self.f[6],self.f[7],self.f[8]]
            new_f = [self.r[0],self.r[1],self.r[2],self.r[3],self.r[4],self.r[5],self.r[6],self.r[7],self.r[8]]
            new_r = [self.b[0],self.b[1],self.b[2],self.b[3],self.b[4],self.b[5],self.b[6],self.b[7],self.b[8]]
            new_b = [self.l[0],self.l[1],self.l[2],self.l[3],self.l[4],self.l[5],self.l[6],self.l[7],self.l[8]]
            new_d = [self.d[2],self.d[5],self.d[8],self.d[1],self.d[4],self.d[7],self.d[0],self.d[3],self.d[6]]
        elif mod == "'":
            new_u = [self.u[2],self.u[5],self.u[8],self.u[1],self.u[4],self.u[7],self.u[0],self.u[3],self.u[6]]
            new_l = [self.b[0],self.b[1],self.b[2],self.b[3],self.b[4],self.b[5],self.b[6],self.b[7],self.b[8]]
            new_f = [self.l[0],self.l[1],self.l[2],self.l[3],self.l[4],self.l[5],self.l[6],self.l[7],self.l[8]]
            new_r = [self.f[0],self.f[1],self.f[2],self.f[3],self.f[4],self.f[5],self.f[6],self.f[7],self.f[8]]
            new_b = [self.r[0],self.r[1],self.r[2],self.r[3],self.r[4],self.r[5],self.r[6],self.r[7],self.r[8]]
            new_d = [self.d[6],self.d[3],self.d[0],self.d[7],self.d[4],self.d[1],self.d[8],self.d[5],self.d[2]]
        elif mod == "2":
            new_u = [self.u[8],self.u[7],self.u[6],self.u[5],self.u[4],self.u[3],self.u[2],self.u[1],self.u[0]]
            new_l = [self.r[0],self.r[1],self.r[2],self.r[3],self.r[4],self.r[5],self.r[6],self.r[7],self.r[8]]
            new_f = [self.b[0],self.b[1],self.b[2],self.b[3],self.b[4],self.b[5],self.b[6],self.b[7],self.b[8]]
            new_r = [self.l[0],self.l[1],self.l[2],self.l[3],self.l[4],self.l[5],self.l[6],self.l[7],self.l[8]]
            new_b = [self.f[0],self.f[1],self.f[2],self.f[3],self.f[4],self.f[5],self.f[6],self.f[7],self.f[8]]
            new_d = [self.d[8],self.d[7],self.d[6],self.d[5],self.d[4],self.d[3],self.d[2],self.d[1],self.d[0]]
        self.u = new_u
        self.l = new_l
        self.f = new_f
        self.r = new_r
        self.b = new_b
        self.d = new_d

    def rotZ(self,mod=""):
        if mod == "":
            new_u = [self.l[6],self.l[3],self.l[0],self.l[7],self.l[4],self.l[1],self.l[8],self.l[5],self.l[2]]
            new_l = [self.d[6],self.d[3],self.d[0],self.d[7],self.d[4],self.d[1],self.d[8],self.d[5],self.d[2]]
            new_f = [self.f[6],self.f[3],self.f[0],self.f[7],self.f[4],self.f[1],self.f[8],self.f[5],self.f[2]]
            new_r = [self.u[6],self.u[3],self.u[0],self.u[7],self.u[4],self.u[1],self.u[8],self.u[5],self.u[2]]
            new_b = [self.b[2],self.b[5],self.b[8],self.b[1],self.b[4],self.b[7],self.b[0],self.b[3],self.b[6]]
            new_d = [self.r[6],self.r[3],self.r[0],self.r[7],self.r[4],self.r[1],self.r[8],self.r[5],self.r[2]]
        elif mod == "'":
            new_u = [self.r[2],self.r[5],self.r[8],self.r[1],self.r[4],self.r[7],self.r[0],self.r[3],self.r[6]]
            new_l = [self.u[2],self.u[5],self.u[8],self.u[1],self.u[4],self.u[7],self.u[0],self.u[3],self.u[6]]
            new_f = [self.f[2],self.f[5],self.f[8],self.f[1],self.f[4],self.f[7],self.f[0],self.f[3],self.f[6]]
            new_r = [self.d[2],self.d[5],self.d[8],self.d[1],self.d[4],self.d[7],self.d[0],self.d[3],self.d[6]]
            new_b = [self.b[6],self.b[3],self.b[0],self.b[7],self.b[4],self.b[1],self.b[8],self.b[5],self.b[2]]
            new_d = [self.l[2],self.l[5],self.l[8],self.l[1],self.l[4],self.l[7],self.l[0],self.l[3],self.l[6]]
        elif mod == "2":
            new_u = [self.d[8],self.d[7],self.d[6],self.d[5],self.d[4],self.d[3],self.d[2],self.d[1],self.d[0]]
            new_l = [self.r[8],self.r[7],self.r[6],self.r[5],self.r[4],self.r[3],self.r[2],self.r[1],self.r[0]]
            new_f = [self.f[8],self.f[7],self.f[6],self.f[5],self.f[4],self.f[3],self.f[2],self.f[1],self.f[0]]
            new_r = [self.l[8],self.l[7],self.l[6],self.l[5],self.l[4],self.l[3],self.l[2],self.l[1],self.l[0]]
            new_b = [self.b[8],self.b[7],self.b[6],self.b[5],self.b[4],self.b[3],self.b[2],self.b[1],self.b[0]]
            new_d = [self.u[8],self.u[7],self.u[6],self.u[5],self.u[4],self.u[3],self.u[2],self.u[1],self.u[0]]
        self.u = new_u
        self.l = new_l
        self.f = new_f
        self.r = new_r
        self.b = new_b
        self.d = new_d

    def move(self,moves=""):
        moves = filter(None,re.split("\s*([UDFBRLMfrlyxz][2']*)\s*",moves))
        self.moves+=''.join(moves)
        for move in moves:
            if move[0] == 'R': self.right() if len(move) == 1 else self.right(move[1])
            elif move[0] == 'L': self.left() if len(move) == 1 else self.left(move[1])
            elif move[0] == 'U': self.up() if len(move) == 1 else self.up(move[1])
            elif move[0] == 'D': self.down() if len(move) == 1 else self.down(move[1])
            elif move[0] == 'F': self.front() if len(move) == 1 else self.front(move[1])
            elif move[0] == 'B': self.back() if len(move) == 1 else self.back(move[1])
            elif move[0] == 'M': self.mid() if len(move) == 1 else self.mid(move[1])
            elif move[0] == 'r': self.rWide() if len(move) == 1 else self.rWide(move[1])
            elif move[0] == 'l': self.lWide() if len(move) == 1 else self.lWide(move[1])
            elif move[0] == 'f': self.fWide() if len(move) == 1 else self.fWide(move[1])
            elif move[0] == 'x': self.rotX() if len(move) == 1 else self.rotX(move[1])
            elif move[0] == 'y': self.rotY() if len(move) == 1 else self.rotY(move[1])
            elif move[0] == 'z': self.rotZ() if len(move) == 1 else self.rotZ(move[1])
        self.cc = self.cornersCorrect()
        self.ec = self.edgesCorrect()

    def crossOK(self):
        return ((self.l[4] == self.l[7]) and (self.f[4] == self.f[7]) and \
        (self.r[4] == self.r[7]) and (self.b[4] == self.b[7]) and \
        (self.d[4] == self.d[1] == self.d[3] == self.d[5] == self.d[7]))

    def cornersCorrect(self):
        corners = 0
        if (self.u[4] == self.u[0]) and (self.b[4] == self.b[2]) and (self.l[4] == self.l[0]): corners = corners + 1 #UBL
        if (self.u[4] == self.u[2]) and (self.b[4] == self.b[0]) and (self.r[4] == self.r[2]): corners = corners + 1 #UBR
        if (self.u[4] == self.u[6]) and (self.f[4] == self.f[0]) and (self.l[4] == self.l[2]): corners = corners + 1 #UFL
        if (self.u[4] == self.u[8]) and (self.f[4] == self.f[2]) and (self.r[4] == self.r[0]): corners = corners + 1 #UFR
        if (self.d[4] == self.d[6]) and (self.b[4] == self.b[8]) and (self.l[4] == self.l[6]): corners = corners + 1 #DBL
        if (self.d[4] == self.d[8]) and (self.b[4] == self.b[6]) and (self.r[4] == self.r[8]): corners = corners + 1 #DBR
        if (self.d[4] == self.d[0]) and (self.f[4] == self.f[6]) and (self.l[4] == self.l[8]): corners = corners + 1 #DFL
        if (self.d[4] == self.d[2]) and (self.f[4] == self.f[8]) and (self.r[4] == self.r[6]): corners = corners + 1 #DFR
        return corners

    def edgesCorrect(self):
        edges = 0
        if (self.u[4] == self.u[1]) and (self.b[4] == self.b[1]): edges = edges +1 #UB
        if (self.u[4] == self.u[5]) and (self.r[4] == self.r[1]): edges = edges +1 #UR
        if (self.u[4] == self.u[7]) and (self.f[4] == self.f[1]): edges = edges +1 #UF
        if (self.u[4] == self.u[3]) and (self.l[4] == self.l[1]): edges = edges +1 #UL
        if (self.f[4] == self.f[3]) and (self.l[4] == self.l[5]): edges = edges +1 #FL
        if (self.f[4] == self.f[5]) and (self.r[4] == self.r[3]): edges = edges +1 #FR
        if (self.b[4] == self.b[5]) and (self.l[4] == self.l[3]): edges = edges +1 #BL
        if (self.b[4] == self.b[3]) and (self.r[4] == self.r[5]): edges = edges +1 #BR
        if (self.d[4] == self.d[7]) and (self.b[4] == self.b[7]): edges = edges +1 #DB
        if (self.d[4] == self.d[5]) and (self.r[4] == self.r[7]): edges = edges +1 #DR
        if (self.d[4] == self.d[1]) and (self.f[4] == self.f[7]): edges = edges +1 #DF
        if (self.d[4] == self.d[3]) and (self.l[4] == self.l[7]): edges = edges +1 #DL
        return edges

    def slotsFilled(self):
        slots = 0
        if ((self.b[4] == self.b[5] == self.b[8]) and (self.l[4] == self.l[3] == self.l[6]) and (self.d[4] == self.d[6])): slots = slots + 1 #BL Slot
        if ((self.b[4] == self.b[3] == self.b[6]) and (self.r[4] == self.r[5] == self.r[8]) and (self.d[4] == self.d[8])): slots = slots + 1 #BR Slot
        if ((self.f[4] == self.f[3] == self.f[6]) and (self.l[4] == self.l[5] == self.l[8]) and (self.d[4] == self.d[0])): slots = slots + 1 #FL Slot
        if ((self.f[4] == self.f[5] == self.f[8]) and (self.r[4] == self.r[3] == self.r[6]) and (self.d[4] == self.d[2])): slots = slots + 1 #FR Slot
        return slots

    def numPairs(self):
        pairs = 0
        if ((self.u[0] == self.u[1]) and (self.b[1] == self.b[2])): pairs = pairs + 1
        if ((self.u[1] == self.u[2]) and (self.b[0] == self.b[1])): pairs = pairs + 1
        if ((self.u[2] == self.u[5]) and (self.r[1] == self.r[2])): pairs = pairs + 1
        if ((self.u[5] == self.u[8]) and (self.r[0] == self.r[1])): pairs = pairs + 1
        if ((self.u[7] == self.u[8]) and (self.f[1] == self.f[2])): pairs = pairs + 1
        if ((self.u[7] == self.u[6]) and (self.f[0] == self.f[1])): pairs = pairs + 1
        if ((self.u[6] == self.u[3]) and (self.l[1] == self.l[2])): pairs = pairs + 1
        if ((self.u[3] == self.u[0]) and (self.l[0] == self.l[1])): pairs = pairs + 1

        if ((self.d[0] == self.d[1]) and (self.f[6] == self.f[7])): pairs = pairs + 1
        if ((self.d[1] == self.d[2]) and (self.f[7] == self.f[8])): pairs = pairs + 1
        if ((self.d[2] == self.d[5]) and (self.r[6] == self.r[7])): pairs = pairs + 1
        if ((self.d[5] == self.d[8]) and (self.r[7] == self.r[8])): pairs = pairs + 1
        if ((self.d[7] == self.d[8]) and (self.b[6] == self.b[7])): pairs = pairs + 1
        if ((self.d[7] == self.d[6]) and (self.b[7] == self.b[8])): pairs = pairs + 1
        if ((self.d[6] == self.d[3]) and (self.l[6] == self.l[7])): pairs = pairs + 1
        if ((self.d[3] == self.d[0]) and (self.l[7] == self.l[8])): pairs = pairs + 1

        if ((self.f[3] == self.f[0]) and (self.l[2] == self.l[5])): pairs = pairs + 1
        if ((self.f[3] == self.f[6]) and (self.l[8] == self.l[5])): pairs = pairs + 1

        if ((self.f[5] == self.f[2]) and (self.l[0] == self.l[3])): pairs = pairs + 1
        if ((self.f[5] == self.f[8]) and (self.l[6] == self.l[3])): pairs = pairs + 1

        if ((self.b[3] == self.b[0]) and (self.r[2] == self.r[5])): pairs = pairs + 1
        if ((self.b[3] == self.b[6]) and (self.r[5] == self.r[8])): pairs = pairs + 1

        if ((self.b[5] == self.b[2]) and (self.l[0] == self.l[3])): pairs = pairs + 1
        if ((self.b[5] == self.b[8]) and (self.l[3] == self.l[6])): pairs = pairs + 1
        return pairs

    def numBlocks221(self):
        blocks = 0
        if ((self.u[0] == self.u[1] == self.u[3] == self.u[4]) and (self.b[1] == self.b[2]) and (self.l[0] == self.l[1])): blocks = blocks + 1
        if ((self.u[2] == self.u[1] == self.u[5] == self.u[4]) and (self.b[1] == self.b[0]) and (self.r[2] == self.r[1])): blocks = blocks + 1
        if ((self.u[4] == self.u[5] == self.u[7] == self.u[8]) and (self.f[1] == self.f[2]) and (self.r[0] == self.r[1])): blocks = blocks + 1
        if ((self.u[3] == self.u[4] == self.u[6] == self.u[7]) and (self.f[0] == self.f[1]) and (self.l[1] == self.l[2])): blocks = blocks + 1

        if ((self.l[0] == self.l[1] == self.l[3] == self.l[4]) and (self.u[0] == self.u[3]) and (self.b[2] == self.b[5])): blocks = blocks + 1
        if ((self.l[2] == self.l[1] == self.l[5] == self.l[4]) and (self.u[3] == self.u[6]) and (self.f[0] == self.f[3])): blocks = blocks + 1
        if ((self.l[4] == self.l[5] == self.l[7] == self.l[8]) and (self.f[3] == self.f[6]) and (self.d[0] == self.d[3])): blocks = blocks + 1
        if ((self.l[3] == self.l[4] == self.l[6] == self.l[7]) and (self.b[5] == self.b[8]) and (self.d[3] == self.d[6])): blocks = blocks + 1

        if ((self.f[0] == self.f[1] == self.f[3] == self.f[4]) and (self.u[6] == self.u[7]) and (self.l[2] == self.l[5])): blocks = blocks + 1
        if ((self.f[2] == self.f[1] == self.f[5] == self.f[4]) and (self.u[7] == self.u[8]) and (self.r[0] == self.r[3])): blocks = blocks + 1
        if ((self.f[4] == self.f[5] == self.f[7] == self.f[8]) and (self.d[1] == self.d[2]) and (self.r[3] == self.r[6])): blocks = blocks + 1
        if ((self.f[3] == self.f[4] == self.f[6] == self.f[7]) and (self.d[0] == self.d[1]) and (self.l[5] == self.l[8])): blocks = blocks + 1

        if ((self.r[0] == self.r[1] == self.r[3] == self.r[4]) and (self.u[5] == self.u[8]) and (self.f[2] == self.f[5])): blocks = blocks + 1
        if ((self.r[2] == self.r[1] == self.r[5] == self.r[4]) and (self.u[2] == self.u[5]) and (self.b[0] == self.b[3])): blocks = blocks + 1
        if ((self.r[4] == self.r[5] == self.r[7] == self.r[8]) and (self.d[5] == self.d[8]) and (self.b[3] == self.b[6])): blocks = blocks + 1
        if ((self.r[3] == self.r[4] == self.r[6] == self.r[7]) and (self.d[2] == self.d[5]) and (self.f[5] == self.f[8])): blocks = blocks + 1

        if ((self.b[0] == self.b[1] == self.b[3] == self.b[4]) and (self.u[1] == self.u[2]) and (self.r[1] == self.r[2])): blocks = blocks + 1
        if ((self.b[2] == self.b[1] == self.b[5] == self.b[4]) and (self.u[0] == self.u[1]) and (self.l[0] == self.l[3])): blocks = blocks + 1
        if ((self.b[4] == self.b[5] == self.b[7] == self.b[8]) and (self.d[6] == self.d[7]) and (self.l[3] == self.l[6])): blocks = blocks + 1
        if ((self.b[3] == self.b[4] == self.b[6] == self.b[7]) and (self.d[7] == self.d[8]) and (self.r[5] == self.r[8])): blocks = blocks + 1

        if ((self.d[0] == self.d[1] == self.d[3] == self.d[4]) and (self.f[6] == self.f[7]) and (self.l[7] == self.l[8])): blocks = blocks + 1
        if ((self.d[2] == self.d[1] == self.d[5] == self.d[4]) and (self.f[7] == self.f[8]) and (self.r[6] == self.r[7])): blocks = blocks + 1
        if ((self.d[4] == self.d[5] == self.d[7] == self.d[8]) and (self.r[7] == self.r[8]) and (self.b[6] == self.b[7])): blocks = blocks + 1
        if ((self.d[3] == self.d[4] == self.d[6] == self.d[7]) and (self.b[7] == self.b[8]) and (self.l[6] == self.l[7])): blocks = blocks + 1
        return blocks

    def numBlocks222(self):
        blocks = 0
        if ((self.u[0] == self.u[1] == self.u[3] == self.u[4]) and (self.b[1] == self.b[2] == self.b[4] == self.b[5]) and \
        (self.l[0] == self.l[1] == self.l[3] == self.l[4])): blocks = blocks + 1
        if ((self.u[1] == self.u[2] == self.u[4] == self.u[5]) and (self.b[0] == self.b[1] == self.b[3] == self.b[4]) and \
        (self.r[1] == self.r[2] == self.r[4] == self.r[5])): blocks = blocks + 1
        if ((self.u[4] == self.u[5] == self.u[7] == self.u[8]) and (self.f[1] == self.f[2] == self.f[4] == self.f[5]) and \
        (self.r[0] == self.r[1] == self.r[3] == self.r[4])): blocks = blocks + 1
        if ((self.u[3] == self.u[4] == self.u[6] == self.u[7]) and (self.f[0] == self.f[1] == self.f[3] == self.f[4]) and \
        (self.l[1] == self.l[2] == self.l[4] == self.l[5])): blocks = blocks + 1

        if ((self.d[0] == self.d[1] == self.d[3] == self.d[4]) and (self.f[3] == self.f[4] == self.f[6] == self.f[7]) and \
        (self.l[4] == self.l[5] == self.l[7] == self.l[8])): blocks = blocks + 1
        if ((self.d[1] == self.d[2] == self.d[4] == self.d[5]) and (self.f[4] == self.f[5] == self.f[7] == self.f[8]) and \
        (self.r[3] == self.r[4] == self.r[6] == self.r[7])): blocks = blocks + 1
        if ((self.d[4] == self.d[5] == self.d[7] == self.d[8]) and (self.b[3] == self.b[4] == self.b[6] == self.b[7]) and \
        (self.r[4] == self.r[5] == self.r[7] == self.r[8])): blocks = blocks + 1
        if ((self.d[3] == self.d[4] == self.d[6] == self.d[7]) and (self.b[4] == self.b[5] == self.b[7] == self.b[8]) and \
        (self.l[3] == self.l[4] == self.l[6] == self.l[7])): blocks = blocks + 1
        return blocks


# Example Usage

print ("*")
listofalgs = [line.rstrip() for line in open('algs.txt')]
# print (len(listofalgs))
print ("*")
c = Cube()
for alg in listofalgs:
    c.move(alg)
    if (c.ec == 9 and c.cc == 5):
        print c
    c.__init__()

# Use of list for sorting algs by ...

# biglist.sort(key=lambda x: x.cc, reverse=True)
#
# countscc = [0,0,0,0,0,0,0,0,0]
# countsec = [0,0,0,0,0,0,0,0,0,0,0,0,0]
# for i in range(len(biglist)):
#     countscc[biglist[i].cc] = countscc[biglist[i].cc] + 1
#     countsec[biglist[i].ec] = countsec[biglist[i].ec] + 1
# print countscc
# print countsec





#for alg in biglist:
#    print alg
#biglist.sort(key=lambda x: x.cc, reverse=True)
#for alg in biglist:
#    print (alg)
# c = Cube()
# c.move("RF2LDB2Rf2zU2l")
# c.move("B2 x R2 F2 y R2 U2 z R U2 x' F2 L z'  B2 U2 z2 F D x2 ")
# c.move("L2 F' U2 B D2 R2 B F2 R2 F2 R' B2 U B R2 F L' U F' U2 R' U B' L' F U' L' R'B'R L' D'F'D2F'")
#print(c)
#print c.numPairs()
#print c.numBlocks221()
#print c.numBlocks222()
#if c.crossOK():
#    print "CROSS OK!"
#print ("CORNERS:", c.cornersCorrect())
#print ("EDGES:", c.edgesCorrect())
#print ("SLOTS:", c.slotsFilled())
