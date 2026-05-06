"""
In-Memory Database - Starter Code
Implement all methods to handle the database operations
"""

from typing import Dict, List, Any, Optional
from models import InMemoryDatabase, TestRunner

def main():
    db = InMemoryDatabase()
    # db.execute_query("SET user1 name Alice")
    db.execute_query("SET user1 profile.age 25")
    print(db.data_structure)
    db.execute_query("SET user1 profile.age 0")
    print(db.data_structure)
    db.execute_query("GET user1 profile.age")





def run_all_tests():
    runner = TestRunner()
    db = InMemoryDatabase()

    # Basic SET and GET
    runner.assert_equal(db.execute_query("SET user1 name Alice"), "", "SET returns empty string")
    runner.assert_equal(db.execute_query("SET user1 profile.age 25"), "", "SET returns empty string")
    runner.assert_equal(db.execute_query("SET user2 profile.age 25"), "", "SET returns empty string")
    runner.assert_equal(db.execute_query("GET user1 name"), "Alice", "GET retrieves value")

main()

