# ClsRegistry

[![PyPI](https://img.shields.io/pypi/v/clsregistry.svg)](https://pypi.org/project/clsregistry/)
[![License](https://img.shields.io/pypi/l/clsregistry.svg)](https://github.com/ppcantidio/clsregistry.py/blob/master/LICENSE)

ClsRegistry is a Python library that provides a simple class for registering and managing classes in a registry. It makes it easier to implement the Registry Pattern in your Python projects, allowing you to efficiently manage and retrieve classes by their identifiers.

## Features

- Register and manage classes by their identifiers.
- Support for specifying a base class for registered classes.
- Retrieve registered classes based on their identifiers and base class.

## Installation

You can install ClsRegistry using pip:

```bash
pip install ClsRegistry
```

## Usage
```bash
from clsregistry import ClsRegistry

# Create an instance of ClsRegistry
registry = ClsRegistry()

# Decorate classes to register them
@registry.register()
class MyClass1:
    pass

@registry.register("custom_id")
class MyClass2:
    pass

# Get registered classes by their identifiers
my_class1 = registry.get_class("MyClass1")
my_class2 = registry.get_class("custom_id")

# Use the registered classes
instance1 = my_class1()
instance2 = my_class2()

```
For more advanced usage, check out the documentation.

## Documentation
Please refer to the official documentation for detailed usage instructions and examples.

## Contributing
Contributions are welcome! If you would like to contribute to ClsRegistry, please check the contribution guidelines.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
- Pedro Cantidio
- Email: ppcantidio@gmail.com
- GitHub: ppcantidio