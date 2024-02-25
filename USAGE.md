# [secret-garden](https://github.com/danielmuringe/secret-garden)
## A better way to manage your dotenv variables


### Installation
- You can use your most preferred package manager to install the package

    `pip install secret-garden` or `poetry add secret-garden` ...


## Table of Contents

1. [Usage](#usage)
    - [load_file function](#load_file-function)
    - [load_space function](#load_space-function)

1. [Examples](#examples)
    - [Using a file](#using-a-file)
        - [env](#env)
        - [json](#json)
        - [toml](#toml)
        - [yaml](#yaml)
    - [Using the environment namespace](#using-the-environment-namespace)

1. [Objects](#objects)
    - [load](#load)
    - [load_file](#load_file)
    - [load_space](#load_space)

1. [Upcoming features](#upcoming-features)


## Usage

- You can package your variables in a file or use the environment namespace

### load_file function

- Create a file using one of the following formats and add your variables:

    - `.env`
    - `.json`
    - `.yaml`
    - `.toml`

        **NB: When using the `.env` file, the variables should be declared as python variables**
    

- Use the `load_file` function to load the variables, specifying the format of the file

    ```python
    from secret_garden import load_file
    load_file('path/to/your/file', format_='<your_format>')
    ```

- Pass the globals dictionary if you want to load the variables into the global namespace

    ```python
    from secret_garden import load_file
    load_file(
        'path/to/your/file',
        format_='<your_format>',
        globals_=globals()
    )
    ```

### load_space function

- Add your variables into the environment namespace

    ```bash
    export STR_VAR="string"
    export INT_VAR=1
    export FLOAT_VAR=1.0
    export BOOL_VAR=True
    export LIST_VAR="['item1', 'item2']"
    export DICT_VAR="{'key1': 'value1', 'key2': 'value2'}"
    ```

- Use the `load_space` function to load the variables

    ```python
    from secret_garden import load_space
    load_space(['STR_VAR', 'INT_VAR', 'FLOAT_VAR', 'BOOL_VAR', 'LIST_VAR', 'DICT_VAR'])
    ```

- Pass the globals dictionary if you want to load the variables into the global namespace

    ```python
    from secret_garden import load_space
    load_space(
        ['STR_VAR', 'INT_VAR', 'FLOAT_VAR', 'BOOL_VAR', 'LIST_VAR', 'DICT_VAR'],
        globals_=globals()
    )
    ```

## Examples

### Using a file

#### env

- Add your variables into the `.env` file

    ```env
    STR_VAR="string"
    INT_VAR=1
    FLOAT_VAR=1.0
    BOOL_VAR=True
    LIST_VAR=['item1', 'item2']
    DICT_VAR={'key1': 'value1', 'key2': 'value2'}
    ```

- Use the `load_file` function to load the variables

    ```python
    from secret_garden import load_file
    load_file('path/to/your/file.env', format_='env')
    ```

- Using the `globals_` parameter

    ```python
    from secret_garden import load_file
    load_file(
        'path/to/your/.env',
        format_='env',
        globals_=globals()
    )
    ```

#### json

- Add your variables into the `.json` file

    ```json
    {
        "STR_VAR": "string",
        "INT_VAR": 1,
        "FLOAT_VAR": 1.0,
        "BOOL_VAR": true,
        "LIST_VAR": ["item1", "item2"],
        "DICT_VAR": {"key1": "value1", "key2": "value2"}
    }
    ```

- Use the `load_file` function to load the variables

    ```python
    from secret_garden import load_file
    load_file('path/to/your/file.json', format_='json')
    ```

- Using the `globals_` parameter

    ```python
    from secret_garden import load_file
    load_file(
        'path/to/your/file.json',
        format_='json',
        globals_=globals()
    )
    ```


#### toml

- Add your variables into the `.toml` file

    ```toml
    STR_VAR = "string"
    INT_VAR = 1
    FLOAT_VAR = 1.0
    BOOL_VAR = true
    LIST_VAR = ["item1", "item2"]
    DICT_VAR = {key1 = "value1", key2 = "value2"}
    ```
- Use the `load_file` function to load the variables

    ```python
    from secret_garden import load_file
    load_file('path/to/your/file.toml', format_='toml')
    ```
- Using the `globals_` parameter

    ```python
    from secret_garden import load_file
    load_file(
        'path/to/your/file.toml',
        format_='toml',
        globals_=globals()
    )
    ```

#### yaml

- Add your variables into the `.yaml` file

    ```yaml
    STR_VAR: string
    INT_VAR: 1
    FLOAT_VAR: 1.0
    BOOL_VAR: true
    LIST_VAR:
        - item1
        - item2
    DICT_VAR:
        key1: value1
        key2: value2
    ```

- Use the `load_file` function to load the variables

    ```python
    from secret_garden import load_file
    load_file('path/to/your/file.yaml', format_='yaml')
    ```

- Using the `globals_` parameter

    ```python
    from secret_garden import load_file
    load_file(
        'path/to/your/file.yaml',
        format_='yaml',
        globals_=globals()
    )
    ```


### Using the environment namespace

- Add your variables into the environment namespace

    ```bash
    export STR_VAR="string"
    export INT_VAR=1
    export FLOAT_VAR=1.0
    export BOOL_VAR=True
    export LIST_VAR="['item1', 'item2']"
    export DICT_VAR="{'key1': 'value1', 'key2': 'value2'}"
    ```

- Use the `load_space` function to load the variables

    ```python
    from secret_garden import load_space
    load_space(['STR_VAR', 'INT_VAR', 'FLOAT_VAR', 'BOOL_VAR', 'LIST_VAR', 'DICT_VAR'])
    ```

- Using the `globals_` parameter

    ```python
    from secret_garden import load_space
    load_space(
        ['STR_VAR', 'INT_VAR', 'FLOAT_VAR', 'BOOL_VAR', 'LIST_VAR', 'DICT_VAR'],
        globals_=globals()
    )
    ```


## Objects

### `load`

```python
load(
    path_or_include: str | list, # path to the file or a list of variables to be included from the environment namespace
    format_: str = 'environ', # the format of the file if path_or_include is a path
    globals_: dict = None, # the execution global namespace to load the variables into
)
```

- `path_or_include` - path to the file containing the variables | list of variables to be included from the environment namespace
- The `format_` parameter can be one of the following:
    - 'env' - *Variables are declared as python variables*
    - 'environ' - *Variables are declared as environment variables where value are in quotes*
    - 'json'
    - 'yaml'
    - 'toml'
- `globals_` - If not provided, variables will returned as a dictionary

### `load_file`
```python
load_file(
    path: str, # path to the file
    format_: str = 'environ', # the format of the file
    globals_: dict = None, # the execution global namespace to load the variables into
)
```
- `path` - The path to the file containing the variables
- The `format_` parameter can be one of the following:
    - 'env' - *Variables are declared as python variables*
    - 'json'
    - 'yaml'
    - 'toml'
- `globals_` - If not provided, variables will returned as a dictionary

### `load_space`
```python
load_space(
    include: list, # a list of variables to be included from the environment namespace
    globals_: dict = None, # the execution global namespace to load the variables into
)
```
- `include` - A list of variables to be included from the environment namespace
- `globals_` - If not provided, variables will returned as a dictionary



## Upcoming features

- [ ] Make loading function default to environment namespace if provided path is not found

- [ ] Support for multiline declaration in the `'env'` and `'environ'` formats

- [ ] Support for nested dictionary and list types in the `'env'` and `'environ'` formats
