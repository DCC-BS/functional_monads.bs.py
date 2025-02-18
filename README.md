# Functional Monads

`functional_monads` is a Python package that provides implementations of common functional programming monads, such as `Maybe` and `Either`.

## Installation

To install the package, use pip:

```sh
uv add git+https://github.com/DCC-BS/functional-monads.bs.py
```

## Usage

### Maybe Monad

The `Maybe` monad represents an optional value. A value of type `Maybe` is either `Just` a value or `Nothing`.

#### Example

```python
from functional_monads.maybe import just, nothing

value = just(42)
no_value = nothing()

print(value)  # Output: Just(42)
print(no_value)  # Output: Nothing

result = value.map(lambda x: x + 1)
print(result)  # Output: Just(43)

default_value = no_value.get_or_else(0)
print(default_value)  # Output: 0
```

### Either Monad

The `Either` monad represents a value of one of two possible types (a disjoint union). Instances of `Either` are either an instance of `Left` or `Right`.

#### Example

```python
from functional_monads.either import left, right

success = right(42)
failure = left("error")

print(success)  # Output: Right(42)
print(failure)  # Output: Left(error)

result = success.map_right(lambda x: x + 1)
print(result)  # Output: Right(43)

default_value = failure.get_or_else_right(0)
print(default_value)  # Output: 0
```

## Development

To contribute to the development of this package, clone the repository and install the development dependencies:

```sh
git clone https://github.com/DCC-BS/functional-monads.bs.py
cd functional-monads
uv sync
```

Run the tests with:

```sh
uv run hatch test
```

Update version:

```sh
uv run hatch version patch
# or
uv run hatch version minor
# or
uv run hatch version major
```
see also [https://hatch.pypa.io/latest/version/](https://hatch.pypa.io/latest/version/)