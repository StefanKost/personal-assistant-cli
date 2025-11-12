import shlex
from typing import Dict, List, Tuple, Callable
from core.app_context import AppContext
from ui.error_util import input_error


# ---------- CONTACT COMMANDS ----------

def add_contact(args, ctx: AppContext):
    if len(args) < 2:
        raise ValueError("add command requires 2 arguments: username and phone")

    ctx.contacts.add_contact(args[0], args[1])


def set_email(args, ctx: AppContext):
    if len(args) < 2:
        raise ValueError("set-email command requires 2 arguments: username and email")

    ctx.contacts.set_email(args[0], args[1])


def set_birthday(args, ctx: AppContext):
    if len(args) < 2:
        raise ValueError("set-birthday command requires 2 arguments: username and birthday")

    ctx.contacts.set_birthday(args[0], args[1])


def set_address(args, ctx: AppContext):
    if len(args) < 2:
        raise ValueError("set-address command requires 2 arguments: username and address")

    ctx.contacts.set_address(args[0], args[1])


# ---------- NOTE COMMANDS ----------

def add_note(args, ctx: AppContext):
    if len(args) < 1:
        raise ValueError("add note command requires 1 argument: note info")

    print('Not implemented yet')

    # ctx.notes.add()


# ---------- SYSTEM COMMANDS ----------

def help_command(args, ctx: AppContext):
    print("Welcome to the personal assistant tool!\n"
          "Available commands:\n"
          "  hello                                     - Show greeting\n"
          "  help                                      - Show possible commands\n"
          "  add <username> <phone>                    - Add new contact with phone or add phone to existing contact\n"
          "  change <username> <old_phone> <new_phone> - Update contact's phone\n"
          "  phone <username>                          - Show contact's phone number(s)\n"
          "  all                                       - Show all contacts\n"
          "  set-birthday <username> <DD.MM.YYYY>      - Set birthday to contact\n"
          "  show-birthday <username>                  - Show contact's birthday\n"
          "  birthdays                                 - Show upcoming birthdays within next week\n"
          "  set-email <username> <email>              - Set email to contact\n"
          "  set-address <username> <address>          - Set address to contact\n"
          "  add-note <note>                           - Add note\n"
          "  close, exit                               - Exit the bot\n")


def exit_command(ctx: AppContext):
    # TODO: save records before close
    # ctx.contacts.save()
    # ctx.notes.save()
    return "exit"


def parse_input(user_input: str) -> Tuple[str, List[str]]:
    args = shlex.split(user_input)
    if not args:
        return "", []
    command = args[0].lower()
    return command, args[1:]


commands: Dict[str, Callable[[List[str], AppContext], str]] = {
    "hello": lambda args, ctx: "How can I help you?",
    "add": add_contact,
    "set-email": set_email,
    "set-birthday": set_birthday,
    "set-address": set_address,
    "add-note": add_note,
    "help": help_command,
}


@input_error
def handle_command(user_input: str, ctx: AppContext) -> str:
    command, args = parse_input(user_input)

    match command:
        case "close" | "exit":
            return exit_command(ctx)
        case cmd if cmd in commands:
            return commands[cmd](args, ctx)
        case _:
            available = ', '.join(sorted(commands.keys()) + ['close', 'exit'])
            return f"Invalid command. Available commands: {available}"
