from magma import *
from mantle import Mux2
from .register import _RegisterName, Register

__all__ = ['DefinePIPO', 'PIPO']

def DefinePIPO(n, init=0, has_ce=False, has_reset=False, has_set=False):
    """
    Generate Parallel-In, Parallel-Out shift register.

    SI : Bit, PI : Array(n, Bit), LOAD : Bit -> O : Array(n, Bit)
    """

    T = Bits(n)
    class _PIPO(Circuit):
        name = _RegisterName('PIPO', n, init, has_ce, has_reset, has_set)
        IO = ['SI', In(Bit), 'PI', In(T), 'LOAD', In(Bit),
              'O', Out(T)] + ClockInterface(has_ce,has_reset,has_set)
        @classmethod
        def definition(pipo):
            def mux2(y):
                return curry(Mux2(), prefix='I')

            mux = braid(col(mux2, n), forkargs=['S'])
            reg = Register(n, init=init, has_ce=has_ce, has_reset=has_reset, has_set=has_set)

            #si = array(*[pipo.SI] + [reg.O[i] for i in range(n-1)])
            si = concat(array(pipo.SI),reg.O[0:n-1])
            mux(si, pipo.PI, pipo.LOAD)
            reg(mux)
            wire(reg.O, pipo.O)
            wireclock(pipo, reg)

    return _PIPO

def PIPO(n, init=0, has_ce=False, has_reset=False, has_set=False, **kwargs):
    return DefinePIPO(n, init, has_ce, has_reset, has_set)(**kwargs)
    
