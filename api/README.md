# alu-back-end / api

Python scripts that gather data from the
[JSONPlaceholder REST API](https://jsonplaceholder.typicode.com) and export
employee TODO list information.

## Requirements

- Python 3
- `requests` module (`pip install requests`)
- Code follows PEP8 (`pycodestyle`)

## Files

| File | Description |
|------|-------------|
| `0-gather_data_from_an_API.py` | Prints an employee's TODO list progress for a given employee ID. |
| `1-export_to_CSV.py` | Exports all of an employee's tasks to `USER_ID.csv`. |
| `2-export_to_JSON.py` | Exports all of an employee's tasks to `USER_ID.json`. |
| `3-dictionary_of_list_of_dictionaries.py` | Exports all tasks of all employees to `todo_all_employees.json`. |

## Usage

```bash
python3 0-gather_data_from_an_API.py 2
```
```
Employee Ervin Howell is done with tasks(8/20):
	 distinctio vitae autem nihil ut molestias quo
	 ...
```

```bash
python3 1-export_to_CSV.py 2          # creates 2.csv
python3 2-export_to_JSON.py 2         # creates 2.json
python3 3-dictionary_of_list_of_dictionaries.py   # creates todo_all_employees.json
```

### Output formats

**CSV** (`USER_ID.csv`):
```
"2","Antonette","False","suscipit repellat esse quibusdam voluptatem incidunt"
```

**JSON** (`USER_ID.json`):
```json
{"2": [{"task": "...", "completed": false, "username": "Antonette"}]}
```

**JSON, all employees** (`todo_all_employees.json`):
```json
{"1": [{"username": "Bret", "task": "...", "completed": false}], "2": [...]}
```

## Author

sanol-1
