from typing import Optional

from pyregistry import PyRegistry


class PyRegistryMulti(PyRegistry):
    """
    Extended class for registering and managing classes with multiple base class support.
    """

    def __init__(self, default: Optional[object] = None) -> None:
        """
        Initializes an instance of PyRegistryMulti.

        Args:
            default (Optional[object]): The default value returned if the requested class is not registered.

        """
        super().__init__(None, default)

    def get_class(self, item: str, base_class: type) -> Optional[type]:
        """
        Get a registered class by its identifier and base class.

        Args:
            item (str): The class identifier.
            base_class (type): The base class that the registered class must be a subclass of.

        Returns:
            Optional[type]: The corresponding registered class, or None if not found.

        """
        for registry in self._registers:
            if registry.get("id") == item and registry.get("cls").__base__ == base_class:
                return registry.get("cls")

        return self._default

    def _add_registry(self, cls: type, id: str) -> None:
        """
        Add a class to the internal registry with support for multiple base classes.

        Args:
            cls (type): The class to be registered.
            id (str): The class identifier.

        Raises:
            Exception: If a class with the same identifier or an existing class with the same base class is found.

        """
        for register in self._registers:
            if register.get("cls") == cls:
                raise Exception("This class already exists")

            if self.get_class(id, cls.__base__):
                raise Exception("Has the same subclass and the same id")

        if self._base_class is not None:
            if issubclass(cls, self._base_class) is False:
                raise Exception("Is not a subclass of base_class defined")

        registry = {"id": id, "cls": cls}
        self._registers.append(registry)
