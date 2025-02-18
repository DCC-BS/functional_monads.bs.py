import unittest
from src.functional_monads.either import Either, left, right, Left, Right


class TestEither(unittest.TestCase):
    def test_left_creation(self):
        l = left("error")
        self.assertIsInstance(l, Left)
        self.assertEqual(l.value, "error")

    def test_right_creation(self):
        r = right(42)
        self.assertIsInstance(r, Right)
        self.assertEqual(r.value, 42)

    def test_is_left(self):
        l = left("error")
        self.assertTrue(l.is_left())
        self.assertFalse(l.is_right())

    def test_is_right(self):
        r = right(42)
        self.assertTrue(r.is_right())
        self.assertFalse(r.is_left())

    def test_map_right(self):
        r = right(42).map_right(lambda x: x + 1)
        self.assertEqual(r.value, 43)

    def test_map_left(self):
        l = left("error").map_left(lambda x: x.upper())
        self.assertEqual(l.value, "ERROR")

    def test_bind_right(self):
        r = right(42).bind_right(lambda x: right(x + 1))
        self.assertEqual(r.value, 43)

    def test_bind_left(self):
        l = left("error").bind_left(lambda x: left(x.upper()))
        self.assertEqual(l.value, "ERROR")

    def test_get_or_else_right(self):
        r = right(42)
        self.assertEqual(r.get_or_else_right(0), 42)
        l = left("error")
        self.assertEqual(l.get_or_else_right(0), 0)

    def test_get_or_else_left(self):
        r = right(42)
        self.assertEqual(r.get_or_else_left("default"), "default")
        l = left("error")
        self.assertEqual(l.get_or_else_left("default"), "error")

    def test_fold(self):
        r = right(42).fold(lambda x: f"Error: {x}", lambda x: f"Success: {x}")
        self.assertEqual(r, "Success: 42")
        l = left("error").fold(lambda x: f"Error: {x}", lambda x: f"Success: {x}")
        self.assertEqual(l, "Error: error")


if __name__ == "__main__":
    unittest.main()
