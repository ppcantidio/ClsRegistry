import unittest
from clsregistry import ClsRegistry


class TestClsRegistry(unittest.TestCase):
    def setUp(self):
        self.registry = ClsRegistry()

    def test_register_and_get_class(self):
        # Register a class using the decorator
        @self.registry.register()
        class MyClass:
            pass

        # Get the registered class by its identifier
        my_class = self.registry.get_class("MyClass")

        self.assertIs(my_class, MyClass)

    def test_register_with_custom_id(self):
        # Register a class with a custom identifier using the decorator
        @self.registry.register("custom_id")
        class CustomIDClass:
            pass

        # Get the registered class by its custom identifier
        custom_id_class = self.registry.get_class("custom_id")

        self.assertIs(custom_id_class, CustomIDClass)

    def test_get_nonexistent_class(self):
        # Attempt to get a class that is not registered
        nonexistent_class = self.registry.get_class("NonExistentClass")

        self.assertIsNone(nonexistent_class)

    def test_register_duplicate_class(self):
        # Register a class with a duplicate identifier
        @self.registry.register("DuplicateClass")
        class DuplicateClass:
            pass

        with self.assertRaises(Exception) as context:
            @self.registry.register("DuplicateClass")
            class DuplicateClass2:
                pass

        self.assertIn("This class already exists", str(context.exception))

    def test_register_duplicate_id(self):
        # Register a class with a duplicate identifier
        @self.registry.register("DuplicateID")
        class DuplicateIDClass:
            pass

        with self.assertRaises(Exception) as context:
            @self.registry.register("DuplicateID")
            class DuplicateIDClass2:
                pass

        self.assertIn("This class already exists", str(context.exception))

    def test_register_invalid_subclass(self):
        # Attempt to register a class that is not a subclass of the specified base class
        class BaseClass:
            pass

        with self.assertRaises(Exception) as context:
            @self.registry.register()
            class InvalidSubclass:
                pass

        self.assertIn("Is not a subclass of base_class defined", str(context.exception))

if __name__ == "__main__":
    unittest.main()
