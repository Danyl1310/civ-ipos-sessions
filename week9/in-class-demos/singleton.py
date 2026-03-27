class ConfigManager:
    # Class-level attribute to store a process level single instance (everything pounts to the one object)
    _instance = None

    def __new__(my_singleton_class):
        # Check if an instance already exists
        if my_singleton_class._instance is None:
            # If not, create a new instance using the superclass's __new__ method
            my_singleton_class._instance = super().__new__(my_singleton_class)
            # Initialise a settings dictionary on the instance
            my_singleton_class._instance._initialised = False
        # Return the single shared instance
        return my_singleton_class._instance

    def __init__(self):
        """This guard prevents resetting the class data when it is called multiple times."""
        # Use the guard
        if self._initialised:
            return
        
        self.settings = {}

        # Switch the guard on
        self._initialised = True

a = ConfigManager()
b = ConfigManager()
a.settings["permissions"] = "admin"
print(b.settings["permissions"]) 

b.settings["permissions"] = "user"
print(a.settings["permissions"])

print(a is b)
print(id(a), id(b))  # same memory address