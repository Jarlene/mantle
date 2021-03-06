import magma as m
from .FF import DefineCoreirReg
import mantle


@m.cache_definition
def DefineRegister(n, init=0, has_ce=False, has_reset=False,
                   has_async_reset=False, _type=m.Bits):
    T = _type(n)
    if has_reset and has_async_reset:
        raise ValueError("Cannot have synchronous and asynchronous reset")

    if has_reset or has_ce:
        class Register(m.Circuit):
            name = f"Register__has_ce_{has_ce}__has_reset_{has_reset}__" \
                   f"has_async_reset__{has_async_reset}__" \
                   f"type_{_type.__name__}__n_{n}"
            IO = ["I", m.In(T), "O", m.Out(T)]
            IO += m.ClockInterface(has_ce=has_ce,
                                   has_reset=has_reset,
                                   has_async_reset=has_async_reset)

            @classmethod
            def definition(io):
                reg = DefineCoreirReg(n, init, has_async_reset, _type)()
                I = io.I
                if has_reset:
                    I = mantle.mux([io.I, m.bits(init, n)], io.RESET)
                if has_ce:
                    I = mantle.mux([reg.O, I], io.CE)
                m.wire(I, reg.I)
                m.wire(io.O, reg.O)
        return Register
    else:
        return DefineCoreirReg(n, init, has_async_reset, _type)


def Register(n, init=0, has_ce=False, has_reset=False, has_async_reset=False,
             **kwargs):
    return DefineRegister(n, init, has_ce, has_reset,
                          has_async_reset)(**kwargs)


def register(I, ce=None, reset=None, async_reset=None, **kwargs):
    has_ce = ce is not None
    has_reset = reset is not None
    has_async_reset = async_reset is not None
    reg = Register(len(I),
                   has_ce=has_ce,
                   has_reset=has_reset,
                   has_async_reset=has_async_reset,
                   **kwargs)
    reg(I)
    if has_ce:
        m.wire(ce, reg.CE)
    if has_reset:
        m.wire(reset, reg.RESET)
    if has_async_reset:
        m.wire(reset, reg.ASYNCRESET)
