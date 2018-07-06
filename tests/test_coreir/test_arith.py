from magma import *
from magma.testing import check_files_equal
from mantle.coreir.arith import DefineAdd, DefineSub, DefineNegate, DefineASR
from magma.testing.newfunction import testvectors as function_test
from magma.simulator.python_simulator import testvectors as simulator_test


def test_add():
    exit(1)
    width = 4
    mask = 2**width-1
    Add = DefineAdd(width)
    assert function_test(Add, lambda x, y: (x + y) & mask) == simulator_test(Add)


def test_add_cout_two():
    compile("build/test_add_cout_two", DefineAdd(4, cout=True), output="coreir")
    assert check_files_equal(__file__,
            "build/test_add_cout_two.json", "gold/test_add_cout_two.json")


def test_add_cin_two():
    compile("build/test_add_cin_two", DefineAdd(4, cin=True), output="coreir")
    assert check_files_equal(__file__,
            "build/test_add_cin_two.json", "gold/test_add_cin_two.json")


def test_sub_cout_two():
    compile("build/test_sub_cout_two", DefineSub(4, cout=True), output="coreir")
    assert check_files_equal(__file__,
            "build/test_sub_cout_two.json", "gold/test_sub_cout_two.json")


def test_sub_cin_two():
    compile("build/test_sub_cin_two", DefineSub(4, cin=True), output="coreir")
    assert check_files_equal(__file__,
            "build/test_sub_cin_two.json", "gold/test_sub_cin_two.json")


def test_negate():
    compile("build/test_negate", DefineNegate(4), output="coreir")
    assert check_files_equal(__file__,
            "build/test_negate.json", "gold/test_negate.json")


def test_asr():
    compile("build/test_asr", DefineASR(4), output="coreir")
    assert check_files_equal(__file__,
            "build/test_asr.json", "gold/test_asr.json")
