# In-Memory Database: SET Implementation

## The Problem

Build a `SET` operation for an in-memory database (a Python dict) that supports nested fields via dot notation:

```
SET user1 profile.name Alice
SET user1 profile.age 25
SET user1 settings.theme dark
```

`SET <key> <path> <value>` — where `key` is the top-level dict entry, `path` is a dot-separated nesting structure, and `value` is what gets stored at the leaf.

## The Core Intuition: Pointers and In-Place Mutation

The breakthrough was understanding how Python dicts work in memory. Each level of nesting is a separate object at its own memory address, and dict values store **pointers** to those objects — not copies.

```
0x01: {user1: ptr -> 0x08}
0x08: {profile: ptr -> 0x16}
0x16: {name: Alice}
```

When you write `nested_value = self.data_structure[key]`, you're not copying the inner dict — you're getting a second reference to the **same object** in memory. Any mutation through `nested_value` mutates the actual data structure, because they point to the same place.

This means:
- On a second `SET user1 ...`, `nested_value` already reflects prior mutations (proof of in-place updates)
- On `SET user2 ...`, `nested_value` is empty — it points to a different object entirely

## How the Intuition Drove the Implementation

Once the pointer model was clear, the algorithm followed naturally:

1. **Ensure the top-level key exists** — if `user1` isn't in the dict, create an empty dict for it
2. **Point `nested_value` at that inner dict** — this is our "cursor" into the data structure
3. **Walk through path elements**, moving the pointer deeper at each step:
   - **Not the last element?** This is a container. Create it as `{}` if it doesn't exist, then move `nested_value` into it.
   - **Last element?** This is the destination. Stop walking and assign the value here. The mutation propagates up through the pointer chain — no need to reassign anything back.

The `len(path_array) - 1` check is the key decision point: every element before the last is a level to traverse; the last element is where we write. If we walked into it instead of assigning to it, we'd be one level too deep.

## The Code

```python
def set_query(self, key, path, value) -> str:
    path_array = path.split('.')

    if key not in self.data_structure:
        self.data_structure[key] = {}

    nested_value = self.data_structure[key]

    for i in range(0, len(path_array)):
        if i == len(path_array) - 1:
            nested_value[path_array[i]] = value
        else:
            if path_array[i] not in nested_value:
                nested_value[path_array[i]] = {}
            nested_value = nested_value[path_array[i]]

    return ''
```

Each line maps directly back to the pointer model — `nested_value` starts at the top-level key's address, walks through intermediate addresses (creating them if needed), and mutates in place at the final address.
