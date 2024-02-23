from myPackage import myModule

def test_top_n():
    """
    Make sure that top_n works correctly
    """
    assert myModule.top_n([8, 3, 5, 1, 2], 3) == [8, 5, 3], 'incorrect'
    assert myModule.top_n([1, 10, 9, 12, 2], 2) == [12, 10], 'incorrect'
    assert myModule.top_n([1, 10, 9, 12, 2], 2) == [12, 10], 'incorrect'
    