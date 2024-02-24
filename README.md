# secret-garden
## A better way to manage your dotenv variables

## Table of Contents

1. [Installation](#installation)
1. [Usage](#usage)
    - [Using a file](#using-a-file)
    - [Using the environment namespace](#using-the-environment-namespace)
1. [Contributors guide](#contributors-guide)
    - [Prior Guidelines](#prior-guidelines)
    - [Contribution Process](#contribution-process)
1. [Upcoming features](#upcoming-features)
1. [Acknowledgement](#acknowledgements)
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

You can package your variables in a file or use the environment namespace

### Using a file

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

- Pass the globals dictionary if you want to load the variables into the global namespace

    ```python
    from secret_garden import load_space
    load_space(
        ['STR_VAR', 'INT_VAR', 'FLOAT_VAR', 'BOOL_VAR', 'LIST_VAR', 'DICT_VAR'],
        globals_=globals()
    )
    ```


## Contributors guide


### Prior Guidelines

1. All development is done on the `dev` branch and thus all pull requests should be made here.

1. The `main` branch is only updated after a release is made.

1. Do not include development dependencies in the `requirements.txt` file.

    Update requirements.txt as shown in step 3 of the contribution process.


### Contribution Process

- **Pre-requisites:**

    Pre-requisite | Installation
    --- | ---
    **python3.10** | [python3.10](https://www.python.org/downloads/release/python-3100/)
    **pip3.10** | Download [the get-pip.py file](https://bootstrap.pypa.io/get-pip.py) and run `python3.10 get-pip.py`
    **poetry** | `pip3.10 install poetry`
    **poetry-plugin-export** | `pip3.10 install poetry-plugin-export`

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

- [ ] Make loading function default to environment namespace if provided path is not found

- [ ] Support for multiline declaration in the `'env'` and `'environ'` formats

- [ ] Support for nested dictionary and list types in the `'env'` and `'environ'` formats


## Acknowledgement

Contributor | Email
--- | ---
[Daniel Muringe](https://github.com/danielmuringe) | [danielmuringe@gmail.com](mailto:danielmuringe@gmail.com)


## Licence

This project is licensed under [the MIT License](https://opensource.org/license/mit/) - see the [LICENCE.md](LICENCE.md) file for details.
