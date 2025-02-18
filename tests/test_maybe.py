from functional_monads import just, nothing

def test_just_creation():
    j = just(5)
    assert j.is_just()
    assert not j.is_nothing()
    assert j.just_value == 5


def test_nothing_creation():
    n = nothing()
    assert n.is_nothing()
    assert not n.is_just()


def test_map_just():
    j = just(5)
    result = j.map(lambda x: x + 1)
    assert result.is_just()
    assert result.just_value == 6


def test_map_nothing():
    n = nothing()
    result = n.map(lambda x: x + 1)
    assert result.is_nothing()


def test_bind_just():
    j = just(5)
    result = j.bind(lambda x: just(x + 1))
    assert result.is_just()
    assert result.just_value == 6


def test_bind_nothing():
    n = nothing()
    result = n.bind(lambda x: just(x + 1))
    assert result.is_nothing()


def test_get_or_else_just():
    j = just(5)
    assert j.get_or_else(0) == 5


def test_get_or_else_nothing():
    n = nothing()
    assert n.get_or_else(0) == 0
