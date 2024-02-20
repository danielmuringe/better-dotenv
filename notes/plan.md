## Declaration formats
- env
- ini
- json
- yaml
- toml
- xml

## Loading functions

- load(path, format_, globals_dict, included, type_, variable_names)

    - if path is provided: load_file



- load_file(path, type_, included)

- load_space(variable_names, globals_dict)

- load_to_globals(path, globals_dict, type_)


## Actions
- One can declare variables explicitly or implicitly
- Read file with environment variables: default -> .env
- Break down environment variables

    - Check if type is explicitly declared
    - If not, infer type from value by tokenizing the value

## Types

### Primitive Types
- int
- float
- string
- bool

### Collection Types
- `list[ <type1>, <type2> ]`
- list
- list[int]
- list[float]
- list[string]
- list[bool]

### Mapping Types
- dict


## Examples

### Explicit Declaration

- Primitive Types

    Shell Variable Notation | Type | Python Variable Notation
    ----------------------- | ---- | -------------------------
    `INT_VAR = int: 1` | int | `INT_VAR: int = 1`
    `FLOAT_VAR = float: 1.5` | float | `FLOAT_VAR: float = 1.5`
    `STRING_VAR = string: "Hello"` | str | `STRING_VAR: str = "Hello"`
    `BOOL_VAR = bool: True` | bool | `BOOL_VAR: bool = True`

- Collection Types

    Shell Variable Notation | Type | Python Variable Notation
    ----------------------- | ---- | -------------------------
    `INT_LIST_VAR = list[int]: [1, 2, 3]` | list[int] | `INT_LIST_VAR: list[int] = [1, 2, 3]`
    `FLOAT_LIST_VAR = list[float]: [1, 2, 3]` | list[float] | `FLOAT_LIST_VAR: list[float] = [1, 2, 3]`
    `STRING_LIST_VAR = list[string]: ["Hello", "World"]` | list[str] | `STRING_LIST_VAR: list[str] = ["Hello", "World"]`
    `BOOL_LIST_VAR = list[bool]: [True, False]` | list[bool] | `BOOL_LIST_VAR: list[bool] = [True, False]`

- Mapping Types

    Shell Variable Notation | Python Variable Notation
    ----------------------- | -------------------------
    `DICT_VAR = dict: {"name": "John", "age": 25}` | `DICT_VAR: dict = {"name": "John", "age": 25}`


### Implicit Declaration

- Primitive Types

    Shell Variable Notation | Type | Python Variable Notation
    ----------------------- | ---- | -------------------------
    `INT_VAR = 1` | int | `INT_VAR = 1`
    `FLOAT_VAR = 1.5` | float | `FLOAT_VAR = 1.5`
    `STRING_VAR = "Hello"` | str | `STRING_VAR = "Hello"`
    `BOOL_VAR = True` | bool | `BOOL_VAR = True`


- Collection Types

    Shell Variable Notation | Type | Python Variable Notation
    ----------------------- | ---- | -------------------------
    `INT_LIST_VAR = [1, 2, 3]` | list[int] | `INT_LIST_VAR = [1, 2, 3]`
    `FLOAT_LIST_VAR = [1, 2, 3]` | list[float] | `FLOAT_LIST_VAR = [1.0, 2.0, 3.0]`
    `STRING_LIST_VAR = ["Hello", "World"]` | list[str] | `STRING_LIST_VAR = ["Hello", "World"]`
    `BOOL_LIST_VAR = [True, False]` | list[bool] | `BOOL_LIST_VAR = [True, False]`

- Mapping Types
    
    Shell Variable Notation | Python Variable Notation
    ----------------------- | -------------------------
    `DICT_VAR = {"name": "John", "age": 25}` | `DICT_VAR = {"name": "John", "age": 25}`