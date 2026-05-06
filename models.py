# ==================== LEVEL 1: Nested Data Structures ====================
    # '''
    # Implement record manipulation with support for nested fields using dot notation:

    # SET <key> <path> <value> — Add or update nested field-value pairs using dot notation (e.g., user.profile.name); creates intermediate objects as needed; 
    # returns empty string
    # GET <key> <path> — Retrieve values from nested paths; returns empty string if path doesn't exist

    # SET user1 profile.name Alice
    # SET user1 profile.age 25
    # SET user2 name Bob
    # SET user1 profile.age 30
    # SET user1 settings.theme dark 
    # GET user1 profile.name           # Returns: "Alice"
    # GET user2 name                   # Returns: "Bob"
    # GET user1 profile                # Returns: {name: Alice, age: 30}
    # '''

    # result of set: {user1: {name: Alice } , user2: {} }
    
    # path: profile.name, value = Alice, self.data_structure = {}
    # iteration1, current path element = profile, self.data_structure = {profile: {}}
    # iteration2, current path elemetn - name, self.data_structure = {profile: {name: Alice}}
    # ...

    # self.data_structure = {user1: {name: Alice}}
    # nested value ->
    # iteration 1: ->{user1: {name: Alice}}
    # nested_value = nested_value[key], {user1: ->{name: Alice}}
    # nested_value[age] = 25, {user1: ->{name: Alice, age: 25}}

    # MEMORY VISUALIZATION 
    # insight: every address in memory stores the key and a pointer to the next nested data
    # 0x01: user -> 0x08
    # 0x08: profile -> 0x16
    # 0x16: {name: Alice}

    # we therefore need to loop through
    # TODO: Implement SET <key> <path> <value>


    # TODO: Implement GET <key> <path>
    # Retrieves value at path, returns empty string if not found

class InMemoryDatabase:
    def __init__(self):
        """Initialize your database here"""
        # TODO: Initialize your data structures
        self.data_structure = {}

    def execute_query(self, query: str) -> str:
        """
        Execute a query and return the result as a string

        Args:
            query: A space-separated command string

        Returns:
            Result as a string (may be empty string for some operations)
        """
        split_query = query.split(' ')
        method = split_query[0]
        key = split_query[1]
        path = split_query[2]
        value = split_query[3]
        if method == "SET":
            return self.set_query(key, path, value)

    def set_query(self, key, path, value) -> str:

        if key not in self.data_structure:
            self.data_structure[key] = {}
        
        user_data = self.data_structure[key]
        # what are we trying to do here 
        # we have the dictionary for the user the set query is for 
        # now we need to put the data coming from the request into the dictionary
        # the data coming in may require nesting 
        # path = name, value = Jon -> { user_1: {name: Jon} }
        # path = profile.age, value = 25 -> { user_1: { profile: age: 25 } }



    def get_query():
        pass


class TestRunner:
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.test_number = 0

    def assert_equal(self, actual, expected, test_name):
        self.test_number += 1
        if actual == expected:
            self.passed += 1
            print(f"✓ Test {self.test_number}: {test_name}")
        else:
            self.failed += 1
            print(f"✗ Test {self.test_number}: {test_name}")
            print(f"  Expected: '{expected}'")
            print(f"  Got:      '{actual}'")

    def print_summary(self):
        total = self.passed + self.failed
        print(f"\n{'='*60}")
        print(f"Results: {self.passed}/{total} tests passed")
        if self.failed == 0:
            print("🎉 All tests passed!")
        else:
            print(f"❌ {self.failed} test(s) failed")
        print(f"{'='*60}")
        return self.failed == 0