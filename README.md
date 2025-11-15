# personal-assistant-cli
A command-line Personal Assistant application developed in Python.
The tool provides a structured way to manage contacts and notes, offering a set of intuitive commands and color-styled output for improved readability.

## Features

### Contacts Management
- Add contacts with multiple phone numbers.
- Edit, search, and delete phone numbers.
- Store and update email, birthday, and address.
- Find contacts by partial match or pattern.
- Show upcoming birthdays within a number of days.
- List all contacts with color-styled output.

### Notes Management
- Create notes with title, body, and tags.
- Search notes by text or by tags.
- Edit title, body, or tags.
- Sort notes by tags.
- Delete notes.
- Display notes in detailed or preview format.

### CLI and User Experience
- Color styled output (errors, warnings, success messages, sections, parameters).
- Structured, colorized help command for easy navigation.
- Centralized styling system (`ui/output_util.py`).
- Error-handling decorator for consistent exception formatting.
- Persistent storage using repositories (pickle or JSON serializers).
- Autocomplete support

## Python Virtual Environment & PEP8 Linting Setup

This project uses a Python virtual environment (`venv`) and a `Makefile`
to automate common development tasks such as installing dependencies and
checking code style using PEP8 (via `flake8` or `pycodestyle`).

## 🚀 Requirements

-   Python 3.7+
-   Make
    -   macOS/Linux: installed by default\
    -   Windows: install Git Bash or Make for Windows

## 📦 Setup

### 1. Create the virtual environment

``` bash
make venv
```

This creates a virtual environment inside the `.venv/` directory and
installs the PEP8 checker.


### 2.Activating the Virtual Environment Manually

-   macOS/Linux:

    ``` bash
    source .venv/bin/activate
    ```

-   Windows:

    ``` bash
    venv\Scripts\activate
    ```

To deactivate:

``` bash
deactivate
```

### 3. Install dependencies

If your project contains a `requirements.txt` file:

``` bash
make install
```

This installs all required packages into the virtual environment.

## 🧹 Code Style Check (PEP8)

To check the project for PEP8 violations using `flake8`:

``` bash
make lint
```

This scans all Python files in the repository and reports any issues.

## 🧼 Clean Up

To remove the virtual environment:

``` bash
make clean
```

## 📁 Makefile Commands Overview

  -----------------------------------------------------------------------
  Command                                 Description
  --------------------------------------- -------------------------------
  `make venv`                             Create the Python virtual
                                          environment and install flake8

  `make install`                          Install project dependencies

  `make lint`                             Run flake8 for PEP8 code-style
                                          checks

  `make clean`                            Delete the virtual environment

## Start CLI assistant
Run the main command-line interface:
```bash
python main.py
```

## Run interactive demo
Start the demo script to see automated interactions.

During the demo, you can press the **SPACE** key to pause or resume execution:
```bash
python demo.py
```

## 📘 Personal Assistant CLI — Command Reference

This document contains a complete list of available CLI commands for the **Personal Assistant** application.  
Commands are grouped into categories for convenient navigation.

---

### 🟦 General Commands

| Command          | Description                          |
|------------------|--------------------------------------|
| `hello`          | Show greeting message                |
| `help`           | Display a list of available commands |
| `close` / `exit` | Exit the application                 |

---

### 🟩 Contact Commands

#### ➕ Add / Modify Contacts

| Command                                     | Description                                                   |
|---------------------------------------------|---------------------------------------------------------------|
| `add <username> <phone>`                    | Add a new contact or append a phone number to an existing one |
| `change <username> <old_phone> <new_phone>` | Replace an old phone number with a new one                    |
| `set-birthday <username> <DD.MM.YYYY>`      | Assign a birthday date to the contact                         |
| `set-email <username> <email>`              | Set an email for the contact                                  |
| `set-address <username> <address>`          | Set a physical address                                        |

#### 📞 View Contacts

| Command                    | Description                                           |
|----------------------------|-------------------------------------------------------|
| `phone <username>`         | Show all phone numbers assigned to the contact        |
| `all`                      | Display all saved contacts                            |
| `find <search_text>`       | Search for contacts (supports `*` wildcard)           |
| `show-birthday <username>` | Display the contact's birthday                        |
| `birthdays <days>`         | Show contacts with upcoming birthdays within *N* days |

#### ❌ Delete Contact Data

| Command                           | Description                            |
|-----------------------------------|----------------------------------------|
| `delete-phone <username> <phone>` | Remove a phone number from the contact |
| `delete-email <username>`         | Remove the contact's email             |
| `delete-birthday <username>`      | Remove the contact's birthday date     |
| `delete-address <username>`       | Remove the contact's address           |
| `delete-contact <username>`       | Permanently delete the contact         |

---

### 🟨 Notes Commands

#### 📝 Manage Notes

| Command           | Description                         |
|-------------------|-------------------------------------|
| `add-note <note>` | Create a new note and return its ID |
| `note <note-id>`  | Display details of a specific note  |
| `notes`           | Show all notes                      |

#### ✏️ Edit Notes

| Command                                 | Description                         |
|-----------------------------------------|-------------------------------------|
| `edit-note-title <note-id> <new-title>` | Update the note title               |
| `edit-note-body <note-id> <new-body>`   | Update the note body                |
| `edit-note-tags <note-id> <tags>`       | Replace note tags (comma-separated) |

#### 🔍 Search & Sort Notes

| Command                  | Description                   |
|--------------------------|-------------------------------|
| `find-notes <query>`     | Search notes by title or body |
| `find-notes-tags <tags>` | Search notes by tags          |
| `sort-notes-tags <tags>` | Sort notes by specific tags   |

#### 🗑️ Delete Notes

| Command                 | Description                 |
|-------------------------|-----------------------------|
| `delete-note <note-id>` | Permanently remove the note |

---

### ✅ Tip

You can always use: `help` to see all available commands during runtime.


## Usage

Type any command in the prompt:

```
Enter a command:
```

Examples:

```
add John 123456789
change John 123456789 987654321
phone John
all
find Jo
set-birthday John 12.04.1990
birthdays 7
delete-contact John
```

Notes examples:

```
add-note Buy milk
notes
note 1
edit-note-title 1 Updated title
find-notes milk
delete-note 1
```

To exit:
```
exit
```

To view help:
```
help
```

## Color Styling

The project uses `colorama` to highlight:
- Errors in red
- Success messages in green
- Warnings in yellow
- Validation messages in magenta
- Sections and commands in structured, readable formats

Centralized styling is implemented in:

```
ui/output_util.py
```

## Error Handling

All command functions are wrapped with the `input_error` decorator.  
It handles:
- AlreadyExistError
- NotFoundError
- KeyError
- ValueError
- IndexError

Errors are formatted consistently and displayed in color.

## Storage

Contacts and notes are stored using **repositories**.

By default, the data is serialized using **pickle**.  
You can also use the **JSON serializer** if needed.

```
storage/pickle_storage.py
```

Data is saved automatically on exit.

## Autocomplete support
The CLI includes built-in **command autocompletion** to improve the user experience.

When typing a command, you can press **Tab** to automatically complete command names.

## Development Notes

- The application is fully modular.
- Commands are separated from business logic.
- Data validation is implemented at model level.
- Each model provides formatted and color-styled output.
- The help system is generated dynamically and styled for readability.

## Architecture Overview

This project uses a **modular, layered architecture**, inspired by the principles of **Hexagonal Architecture (Ports & Adapters)**.
Each layer has a clear purpose and limited knowledge about other layers, which keeps the codebase maintainable and easy to extend.

### 🧩 Layer Overview
```markdown
core/
  app_context.py  
      Central place for initializing and wiring services, repositories,
      and storage drivers. Works as a lightweight Dependency Injection container.

exceptions/
      Custom exception classes used across the application.

models/
  Domain data models used by services and repositories.
  values/
      Small immutable value objects (Field, Birthday, etc.).
  

repositories/
  Repository layer provides a persistent storage interface.
  Does not know how data is physically saved — only defines operations
  for CRUD-like access.

services/
  Application logic layer. Implements use-cases, validation,
  and orchestrates repositories. Contains no UI or storage code.

storage/
  Low-level infrastructure. Responsible for reading/writing data.
  Implements storage mechanisms (Pickle, JSON, file-based).

ui/
  cli.py
  commands.py
      User interface layer. Parses CLI input, maps commands to service calls,
      and renders output for the user.

tests/
      Unit tests for services, repositories, and commands.
```

### 🏛️ Architectural Principles

- **Separation of Concerns**  
  Each part of the program has a single responsibility:  
  UI handles input/output, Services handle application logic,  
  Repositories define persistence operations, and Storage implements them.

- **Inversion of Dependencies**  
  Services depend on repository *interfaces*, not on specific storage formats.  
  Actual implementations (pickle, JSON, etc.) are injected via `AppContext`.

- **Modularity**  
  Each domain area (contacts, notes) has its own services and repositories,  
  which keeps the code independent and easier to modify.

- **Replaceable Storage**  
  You can switch from Pickle to JSON by swapping the storage adapter  
  without changing business logic or CLI code.

- **Testability**  
  The structure allows testing services with in-memory repositories  
  without touching real files.

### 🔧 How the Layers Interact

UI (commands)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↓  
Services (business/application logic)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↓  
Repositories (abstract data access API)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↓  
Storage (actual file/JSON/pickle implementation)

Each layer only talks to the layer directly below it.

