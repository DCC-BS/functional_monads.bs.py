from functional_monads import left, right, Left, Right


def test_left_creation():
    l = left("error")
    assert isinstance(l, Left)
    assert l.value == "error"


def test_right_creation():
    r = right(42)
    assert isinstance(r, Right)
    assert r.value == 42


def test_is_left():
    l = left("error")
    assert l.is_left()
    assert not l.is_right()


def test_is_right():
    r = right(42)
    assert r.is_right()
    assert not r.is_left()


def test_map_right():
    r = right(42).map_right(lambda x: x + 1)
    l = left("error").map_right(lambda x: x + 1)
    assert r.value == 43
    assert l.value == "error"


def test_map_left():
    l = left("error").map_left(lambda x: x.upper())
    r = right(42).map_left(lambda x: x.upper())
    assert l.value == "ERROR"
    assert r.value == 42


def test_bind_right():
    r = right(42).bind_right(lambda x: right(x + 1))
    assert r.value == 43


def test_bind_left():
    l = left("error").bind_left(lambda x: left(x.upper()))
    assert l.value == "ERROR"


def test_get_or_else_right():
    r = right(42)
    assert r.get_or_else_right(0) == 42
    l = left("error")
    assert l.get_or_else_right(0) == 0


def test_get_or_else_left():
    r = right(42)
    assert r.get_or_else_left("default") == "default"
    l = left("error")
    assert l.get_or_else_left("default") == "error"


def test_fold():
    r = right(42).fold(lambda x: f"Error: {x}", lambda x: f"Success: {x}")
    assert r == "Success: 42"
    l = left("error").fold(lambda x: f"Error: {x}", lambda x: f"Success: {x}")
    assert l == "Error: error"


def test_left_str():
    l = left("error")
    assert str(l) == "Left(error)"


def test_right_str():
    r = right(42)
    assert str(r) == "Right(42)"


def test_left_repr():
    l = left("error")
    assert repr(l) == "Left(error)"


def test_right_repr():
    r = right(42)
    assert repr(r) == "Right(42)"
