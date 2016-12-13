import sys
import logging
import day9b

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)


def test_1():
    assert len("ADVENT") == day9b.decompressed_length("ADVENT")


def test_2():
    assert len("ABBBBBC") == day9b.decompressed_length("A(1x5)BC")


def test_3():
    assert len("XYZXYZXYZ") == day9b.decompressed_length("(3x3)XYZ")


def test_4():
    assert len("ABCBCDEFEFG") == day9b.decompressed_length("A(2x2)BCD(2x2)EFG")


def test_5():
    assert len("AAA") == day9b.decompressed_length("(6x1)(1x3)A")


def test_6():
    assert len("XABCABCABCABCABCABCY") == day9b.decompressed_length("X(8x2)(3x3)ABCY")


def test_7():
    assert 241920 == day9b.decompressed_length("(27x12)(20x12)(13x14)(7x10)(1x12)A")


def test_8():
    assert 445 == day9b.decompressed_length("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN")
