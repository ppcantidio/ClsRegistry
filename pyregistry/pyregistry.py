import importlib
import inspect
import pkgutil
from typing import Callable, List, Optional, Union


class PyRegistry:
    """
    Class for registering and managing classes in a registry.
    """

    def __init__(self, base_class: Optional[type] = None, default: Optional[object] = None) -> None:
        """
        Initializes an instance of PyRegistry.

        Args:
            base_class (Optional[type]): The base class to which registered classes must be subclasses.
            default (Optional[object]): The default value returned if the requested class is not registered.

        """
        self._registers = []
        self._base_class = base_class
        self._default = default

    def get_class(self, item: str) -> Optional[type]:
        """
        Get a registered class by its identifier.

        Args:
            item (str): The class identifier.

        Returns:
            Optional[type]: The corresponding registered class, or None if not found.

        """
        for registry in self._registers:
            if registry.get("id") == item:
                return registry.get("cls")
        return self._default

    def register(self, custom_id: Optional[str] = None) -> Callable:
        """
        Decorator to register a class in the registry.

        Args:
            custom_id (Optional[str]): A custom identifier for the registered class.

        Returns:
            Callable: The decorator that registers the class.

        """

        def decorator(cls: type) -> type:
            print("Registration!")
            id = cls.__name__
            if custom_id is not None:
                id = custom_id
            self._add_registry(cls, id)
            return cls

        return decorator

    def _add_registry(self, cls: type, id: str) -> None:
        """
        Add a class to the internal registry.

        Args:
            cls (type): The class to be registered.
            id (str): The class identifier.

        Raises:
            Exception: If a class with the same identifier or an existing class is found.

        """
        if self.get_class(id) and self._unique_id is True:
            raise Exception("Already exists user with this id")

        for register in self._registers:
            if register.get("cls") == cls:
                raise Exception("This class already exists")

        if self._base_class is not None:
            if issubclass(cls, self._base_class) is False:
                raise Exception("Is not a subclass of base_class defined")

        registry = {"id": id, "cls": cls}
        self._registers.append(registry)

    def load_classes(self, paths: Union[str, List[str]]) -> None:
        """
        Load classes from specified Python modules.

        Args:
            paths (Union[str, List[str]]): A path or list of paths to Python modules to be loaded.

        """
        if isinstance(paths, str):
            paths = [paths]
        for path in paths:
            importlib.import_module(path)

    def load_package(self, import_path: str) -> None:
        """
        Load all classes from a Python package.

        Args:
            import_path (str): The import path of the package.

        """
        package_path = importlib.import_module(import_path).__file__.replace("__init__.py", "")
        for _, module_name, _ in pkgutil.walk_packages([rf"{package_path}"]):
            module_path = f"{import_path}.{module_name}"
            module = importlib.import_module(module_path)
            if hasattr(module, "__path__"):
                self.load_classes(f"{import_path}.{module_name}")
            for name, obj in inspect.getmembers(module):
                pass
