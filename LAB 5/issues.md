# Static Code Analysis – Issues Report

## 1. Bandit Issues

| Sl. No. | Issue | Location | Severity | Description | Fix Applied |
|---|---|---|---|---|---|
| 1 | Pickle module import | Line 3 | Low | The pickle module can be unsafe when processing untrusted data. | Replaced pickle-based storage with JSON. |
| 2 | Unsafe pickle deserialization | Line 47 | Medium | `pickle.load()` can execute malicious code when loading untrusted data. | Replaced pickle deserialization with `json.load()`. |
| 3 | Shell command injection risk | Line 57 | High | `os.system()` with dynamically constructed input can allow shell command injection. | Removed the unsafe email shell command. |
| 4 | Use of non-cryptographic random | Line 70 | Low | `random.choice()` is unsuitable for security-sensitive randomness. | Removed the random selection and used a deterministic task suggestion. |

## 2. Pylint Issues

| Sl. No. | Issue | Description | Fix Applied |
|---|---|---|---|
| 1 | Missing module docstring | The module did not contain a description of its purpose. | Added a module docstring. |
| 2 | Missing function docstrings | Functions lacked documentation describing their purpose. | Added docstrings to functions. |
| 3 | Invalid function naming | CamelCase function names did not follow Python's snake_case convention. | Renamed functions using snake_case. |
| 4 | Invalid variable naming | Variable names such as `taskId` and `fileName` did not follow snake_case. | Renamed variables to `task_id` and `file_name`. |
| 5 | Dangerous default value | Using `labels=[]` as a default argument can cause a mutable list to be shared across calls. | Changed the default to `None` and initialized the list inside the function. |
| 6 | Inconsistent return statement | `findTask()` did not explicitly return a value when no task matched. | Added `return None` when no match is found. |
| 7 | Unspecified file encoding | Files were opened without explicitly specifying their encoding. | Specified UTF-8 encoding when opening JSON files. |
| 8 | Missing main guard | The main function was executed whenever the module was imported. | Added an `if __name__ == "__main__":` guard. |

## 3. Flake8 Issues

| Sl. No. | Issue | Location | Description | Fix Applied |
|---|---|---|---|---|
| 1 | E225 | Line 12 | Missing whitespace around an operator. | Added the required whitespace. |
| 2 | E303 | Line 40 | Too many blank lines between code blocks. | Removed unnecessary blank lines. |
| 3 | E261 | Line 69 | An inline comment lacked the required spacing before the comment marker. | Corrected the spacing. |
| 4 | E231 | Line 74 | Missing whitespace after a comma. | Added the required whitespace. |

