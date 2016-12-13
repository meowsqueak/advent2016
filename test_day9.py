import day9


def test_1():
    assert "ADVENT" == day9.decompress("ADVENT")


def test_2():
    assert "ABBBBBC" == day9.decompress("A(1x5)BC")


def test_3():
    assert "XYZXYZXYZ" == day9.decompress("(3x3)XYZ")


def test_4():
    assert "ABCBCDEFEFG" == day9.decompress("A(2x2)BCD(2x2)EFG")


def test_5():
    assert "(1x3)A" == day9.decompress("(6x1)(1x3)A")


def test_6():
    assert "X(3x3)ABC(3x3)ABCY" == day9.decompress("X(8x2)(3x3)ABCY")
