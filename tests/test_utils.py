from sgmc.utils import siblings


def test_siblings():
    for sibs in ((0, 1, 2), (5001, 5002), (5999, 6000), (4998, 4999, 5000), (45001, )):
        for s in sibs:
            assert siblings(s) == sibs
