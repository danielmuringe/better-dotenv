# typed-env
## A better way to manage your dotenv variables

## Table of Contents

1. [Installation](#installation)
1. [Usage](#usage)
1. [Contributors guide](#contributors-guide)
    - [Prior Guidelines](#prior-guidelines)
    - [Contribution Process](#contribution-process)
1. [Acknowledgements](#acknowledgements)
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
    poetry add typed-env
    ```

- Check if the package is installed

    ```
    poetry show typed-env
    ```


## Usage

COMING SOON...


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
    git clone https://github.com/danielmuringe/typed-env
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


## Acknowledgements

Contributor | Role | Email
--- | --- | --- 
[Daniel Muringe](https://github.com/danielmuringe) | Author | [danielmuringe@gmail.com](mailto:danielmuringe@gmail.com)


## Licence

This project is licensed under [the MIT License](https://opensource.org/license/mit/) - see the [LICENCE.md](LICENCE.md) file for details.
