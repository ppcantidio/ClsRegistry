import unittest
from clsregistry.clsregistry_multi import ClsRegistryMulti


class TestClsRegistryMulti(unittest.TestCase):
    def setUp(self):
        self.registry = ClsRegistryMulti()

    def test_register_and_get_class(self):
        class BaseClass:
            pass

        class SubclassA(BaseClass):
            pass

        class SubclassB(BaseClass):
            pass

        # Register classes
        @self.registry.register()
        class MyClass1(BaseClass):
            pass

        @self.registry.register("custom_id")
        class MyClass2(SubclassA):
            pass

        @self.registry.register()
        class MyClass3(SubclassB):
            pass

        # Test get_class
        my_class1 = self.registry.get_class("MyClass1", BaseClass)
        my_class2 = self.registry.get_class("custom_id", SubclassA)
        my_class3 = self.registry.get_class("MyClass3", SubclassB)

        self.assertIs(my_class1, MyClass1)
        self.assertIs(my_class2, MyClass2)
        self.assertIs(my_class3, MyClass3)

    def test_add_registry_duplicate_id(self):
        @self.registry.register()
        class MyClass1:
            pass

        with self.assertRaises(Exception) as context:
            @self.registry.register("MyClass1")
            class DuplicateClass:
                pass

        self.assertIn("This class already exists", str(context.exception))

    def test_add_registry_duplicate_subclass_and_id(self):
        class BaseClass:
            pass

        @self.registry.register()
        class MyClass1(BaseClass):
            pass

        with self.assertRaises(Exception) as context:
            @self.registry.register("MyClass1")
            class DuplicateClass(BaseClass):
                pass

        self.assertIn("Has the same subclass and the same id", str(context.exception))

    def test_add_registry_invalid_subclass(self):
        class BaseClass:
            pass

        with self.assertRaises(Exception) as context:
            @self.registry.register()
            class InvalidSubclass:
                pass

        self.assertIn("Is not a subclass of base_class defined", str(context.exception))

if __name__ == "__main__":
    unittest.main()
