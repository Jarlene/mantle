from magma import *
from mantle import And, Decode
from .counter import Counter

__all__ = ['DefineUpCounterModM', 'UpCounterModM']
#__all__ += ['DefineDownCounterModM', 'DownCounterModM']
__all__ += ['DefineCounterModM', 'CounterModM']

def _CounterName(name, n, m, ce, r, s):
    name += '{}'.format(n)
    name += 'Mod{}'.format(m)
    if ce: name += 'CE'
    if r:  name += 'R'
    if s:  name += 'S'
    return name

#
# Create an n-bit mod-m counter
#
@cache_definition
def DefineCounterModM(m, n, cin=False, cout=True, incr=1, next=False,
    has_ce=False, has_reset=False):

    r = has_reset
    s = False
    name = _CounterName('Counter', n, m, has_ce, r, s)

    args = []
    if cin:
        args += ['CIN', In(Bit)]

    args += ["O", Out(UInt(n))]
    if cout:
        args += ["COUT", Out(Bit)]

    args += ClockInterface(has_ce, r, s)

    CounterModM = DefineCircuit(name, *args)

    counter = Counter(n, cin=cin, cout=cout, incr=incr, next=next,
                   has_ce=has_ce, has_reset=True)
    reset = Decode(m - 1, n)(counter.O)

    if has_reset:
        reset = Or(2)(reset, counter.RESET)

    if has_ce:
        CE = In(Bit)()
        reset = And(2)(reset, CE)
        # reset is sometimes called rollover or RO
        # note that we don't return RO in Counter

        # should also handle r in the definition

    wire(reset, counter.RESET) # synchronous reset

    if has_ce:
        wire(CE, counter.CE)

    if cin:
        wire( CounterModM.CIN, counter.CIN )

    wire( counter.O, CounterModM.O )

    if cout:
        wire( reset, CounterModM.COUT )

    wire(CounterModM.CLK, counter.CLK)
    if hasattr(counter,"CE"):
        wire(CounterModM.CE, counter.CE)

    EndCircuit()

    return CounterModM

def CounterModM(m, n, cin=False, cout=True, incr=1, next=False,
    has_ce=False, **kwargs):
    return DefineCounterModM(m, n, cin, cout, incr, next, has_ce)(**kwargs)

DefineUpCounterModM = DefineCounterModM
UpCounterModM = CounterModM
