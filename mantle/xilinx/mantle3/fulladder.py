from magma import *
from ..spartan3.CLB import ANDCY, CARRY, A0, A1
from .LUT import LUTN

__all__  = ['FullCarry']
__all__ += ['FullAdder']

# return I0, ..., In, CIN -> O, COUT
#
def FullCarry(k, expr1, expr2):

    assert k <= 4

    lut = LUTN(expr1, k)

    args = []

    if k >= 1:
        I0 = Bit()
        wire(I0, lut.I0)
        args += ['I0', I0]
    if k >= 2:
        I1 = Bit()
        wire(I1, lut.I1)
        args += ['I1', I1]
    if k >= 3:
        args += ['I2', lut.I2]
    if k >= 4:
        args += ['I3', lut.I3]

    if expr2 == A0&A1:
       assert k >= 2
       and1 = ANDCY()
       wire(I0, and1.I0)
       wire(I1, and1.I1)
       DI = and1.LO
    elif expr2 == A0:
       assert k >= 1
       DI = I0
    elif expr2 == A1:
       assert k >= 2
       DI = I1
    elif expr2 == 0: 
       DI = 0
    elif expr2 == 1:
       DI = 1

    CIN = Bit()

    O, COUT = CARRY(lut.O, DI, CIN)

    args += [ "O",    O,
              "CIN",   CIN,
              "COUT", COUT ]

    return AnonymousCircuit( args )

def FullAdder():
    pass

