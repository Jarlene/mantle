from ..ice40 import FAMILY, \
    A0, A1, A2, A3, \
    I0, I1, I2, I3, \
    ALL, ANY, PARITY, ZERO, ONE, \
    LUTS_PER_LOGICBLOCK, BITS_PER_LUT, LOG_BITS_PER_LUT

from .IO import *

from .LUT import *
from .ROM import *
from .MUX import *
from .BUF import *
from .FF import *

#from .cascade import *
from .flatcascade import *

from .logic import *
from .adder import *
from .arith import *
from .compare import *

#from .decode import *
#from .encoder import *
#from .decoder import *
#from .arbiter import *

#from .register import *
#from .shift import *
#from .ring import *

#from .counter import *

print('import mantle lattice mantle40')
