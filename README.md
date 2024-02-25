# secret-garden
## A better way to manage your dotenv variables

## Table of Contents

1. [Installation](#installation)
1. [Usage](#usage)
    - [loading from a file](#load_file-function)
    - [loading from the environment namespace](#load_space-function)
    - [loading from a file using the environment namespace as an alternative](#load-function)
1. [Contributors guide](#contributors-guide)
    - [Prior Guidelines](#prior-guidelines)
    - [Contribution Process](#contribution-process)
1. [Upcoming features](#upcoming-features)
1. [Acknowledgement](#acknowledgement)
1. [Licence](#licence)


## Installation

- **Pre-requisites:**

    Pre-requisite | Installation
    --- | ---
    **python3.10** | [python3.10 downloads](https://www.python.org/downloads/release/python-3100/)
    **pip3.10** | Download [the get-pip.py file](https://bootstrap.pypa.io/get-pip.py) and run `python3.10 get-pip.py`
    **poetry** (pip improvement) | Run `pip3.10 install poetry`
    
- Installing the package

    ```
    poetry add secret-garden
    ```

- Check if the package is installed

    ```
    poetry show secret-garden
    ```

## Usage

You can put your variables in a file or use the environment namespace

<h3 id="load_file-function">Loading from a file</h3>

Create a file using one of the following formats and add your variables:

- `.env`
- `.json`
- `.yaml`
- `.toml`

    **Note: When using the `.env` file, the variables should be declared as python variables**
    

Use the `load_file` function to load the variables, specifying the format of the file

```python
from secret_garden import load_file
load_file('path/to/your/file', format_='<your_format>')
```

Pass the globals dictionary if you want to load the variables into the global namespace

```python
from secret_garden import load_file
load_file(
    'path/to/your/file',
    format_='<your_format>',
    globals_=globals()
)
```

<h3 id="load_space-function">Loading from the environment namespace</h3>

Add your variables into the environment namespace

```bash
export STR_VAR="string"
export INT_VAR=1
export FLOAT_VAR=1.0
export BOOL_VAR=True
export LIST_VAR="['item1', 'item2']"
export DICT_VAR="{'key1': 'value1', 'key2': 'value2'}"
```

Use the `load_space` function to load the variables

```python
from secret_garden import load_space
load_space(['STR_VAR', 'INT_VAR', 'FLOAT_VAR', 'BOOL_VAR', 'LIST_VAR', 'DICT_VAR'])
```

Pass the globals dictionary if you want to load the variables into the global namespace

```python
from secret_garden import load_space
load_space(
    ['STR_VAR', 'INT_VAR', 'FLOAT_VAR', 'BOOL_VAR', 'LIST_VAR', 'DICT_VAR'],
    globals_=globals()
)
```


<h3 id="load-function">Loading from a file using the environment namespace as an alternative</h3>

- This is done using the `load` function.

- If both path and include are provided, the variables are loaded from the file and the include argument is ignored.

    ```python
    from secret_garden import load
    load(
        "/path/to/your/file", # path to the file containing the variables
        ["VAR1", "VAR2"], # this will be ignored
        format_ = 'env',
        globals_ = None, 
    )
    ```

- If path does not exist, the variables are loaded from the environment namespace. The include argument is used to know which variables to get from the environment namespace.
    ```python
    from secret_garden import load
    load(
        "/path/to/the/non-existent/file", # path to the non-existent file
        ["VAR1", "VAR2"], # variables to be included from the environment namespace
        format_ = 'env',
        globals_ = None, 
    )
    ```


## Contributors guide


### Prior Guidelines

1. All development is done on the `dev` branch and thus all pull requests should be made here.

1. The `main` and `packaging` branches are out of bounds.

1. Do not include development dependencies in the `requirements.txt` file.

    Update requirements.txt as shown in step 3 of the contribution process.


### Contribution Process

- **Pre-requisites:**

    Pre-requisite | Installation
    --- | ---
    **python3.10** | [python3.10](https://www.python.org/downloads/release/python-3100/)
    **pip3.10** | Download [the get-pip.py file](https://bootstrap.pypa.io/get-pip.py) and run `python3.10 get-pip.py`
    **poetry** | `pip3.10 install poetry`

- Fork the repository and clone it
    ```
    git clone https://github.com/danielmuringe/secret-garden
    ```

- Create a new branch from the `dev` branch: 
    ```
    git checkout dev
    git checkout -b <feature-branch-name>
    ```

- Install the development dependencies and activate a virtual environment:
    
    ```
    poetry install --no-root
    poetry shell
    ```

- Make your changes and ensure you have created tests to cover the changes.

- Create a pull request to the `dev` branch and wait for confirmation.


## Upcoming features

- [ ] Support for multiline declaration in the `'env'` and `'environ'` formats

- [ ] Support for nested dictionary and list types in the `'env'` and `'environ'` formats


## Acknowledgement

Contributor | Email
--- | ---
[Daniel Muringe](https://github.com/danielmuringe) | [danielmuringe@gmail.com](mailto:danielmuringe@gmail.com)


## Licence

This project is licensed under [the MIT License](https://opensource.org/license/mit/) - see the [LICENCE.md](LICENCE.md) file for details.
