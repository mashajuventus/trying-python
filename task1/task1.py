
def unique(e):
    return sorted(set(e))


def transposeDict(d):
    return {d[a]: a for a in d.keys()}


def mex(e):
    for p in range(1, len(e) + 2):
        if p not in e:
            return p


def frequencyDict(s):
    return {a: s.count(a) for a in s}


if __name__ == '__main__':
    assert unique([1, 2, 1, 3]) == [1, 2, 3], 'First unique failed'
    assert unique({5, 1, 3}) == [1, 3, 5], 'Second unique failed'
    assert unique('adsfasdf') == ['a', 'd', 'f', 's'], 'Third unique failed'

    assert transposeDict({1: 'a', 2: 'b'}) == {'a': 1, 'b': 2},\
        'First transposeDict failed'
    assert transposeDict({1: 1}) == {1: 1}, 'Second transposeDict failed'
    assert transposeDict({}) == {}, 'Third transposeDict failed'

    assert mex([1, 2, 3]) == 4, 'First mex failed'
    assert mex(['asdf', 123]) == 1, 'Second mex failed'
    assert mex([0, 0, 1, 0]) == 2, 'Third mex failed'

    assert frequencyDict('') == {}, 'First frequencyDict failed'
    assert frequencyDict('abacaba') == {'a': 4, 'b': 2, 'c': 1},\
        'Second frequencyDict failed'
