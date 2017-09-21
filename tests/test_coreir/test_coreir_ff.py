from magma import *
from magma.testing import check_files_equal
from mantle.coreir import DefineDFF

def test_ff():
    DFF = DefineDFF()
    print(repr(DFF))
    compile("build/test_coreir_dff", DFF, output="coreir")
    assert check_files_equal(__file__,
            "build/test_coreir_dff.json", "gold/test_coreir_dff.json")
