#!/usr/bin/env python3 

# This is a wrapper around tgpt's -s argument that generates shell commands.
# This allows for a more convenient method of invoking that functionality.


import subprocess, os, sys
from enum import Enum

class Model(Enum):
    '''
    Each enum member is a tuple of the provider and model name, and the name
    of the enum member is an abbreviation that is provided as an argument by
    the user. The argument is resolved to the corresponding enum variant.
    '''

    meta = ("duckduckgo", "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo")
    phind = ("phind", "phind")
    gpt = ("duckduckgo", "gpt-4o-mini")
    claude = ("duckduckgo", "claude-3-haiku-20240307")
    mistral = ("duckduckgo", "mistralai/Mixtral-8x7B-Instruct-v0.1")

def determine_shell() -> str:
    '''
    Determines the shell used to invoke the script.
    Does not check environment variables, but what the parent process
    of the Python3 process is, as a bash shell started in a fish shell
    would still inherit the environment variables of the fish shell,
    including the $SHELL variable; bash would be recognized as fish.
    '''
    
    # Check parent of the python3 process
    parent = subprocess.run(["ps", "-p", str(os.getppid()), "-o", "comm="], stdout=subprocess.PIPE, text=True).stdout.strip()

    return parent

def make_preprompt(shell: str) -> str:
    '''
    Generates the appropriate pre-prompt message for the user's shell.
    '''
    return f"You generate commands for the {shell} shell, on an Arch Linux system."

def generate_command(model: Model, prompt: str, shell: str, force: bool = False) -> str:
    '''
    Generates the command to pass to the tgpt script.
    '''
    provider, model_name = model.value
    preprompt: str = make_preprompt(shell)
    force: str = "-y" if force else ""
    return f"tgpt -s {force} --preprompt '{preprompt}' --provider '{provider}' --model '{model_name}' '{prompt}'"

def print_usage() -> None:
    print("Usage: suggest 'prompt' [--using <model>] [--for <shell>] [--run] [--helpp|-h]")
    print("Where model: meta, phind, gpt, claude, mistral")
    print("Where shell: anything. Automatically detected if not included.")
    print("Run: optional, if supplied the generated shell command will be immediately executed")

def main():
    args = sys.argv[1:]

    if len(args) == 0:
        print_usage()
        exit(1)

    model: Model | None = None
    shell: str | None = None
    force: bool | None = None
    prompt: list[str] = []

    skip = 0
    print(",".join(args))

    for i, arg in enumerate(args):
        if skip > 0:
            skip -= 1
            continue

        narg = args[i + 1] if i + 1 < len(args) else None

        if (arg in ("--using", "-m")) and model is None and narg is not None and model is None:
            model = Model[narg]
            skip += 1
            continue

        elif (arg in ('--for', '-s')) and narg is not None and shell is None:
            shell = narg
            skip += 1
            continue

        if arg in ("--help", "-h"):
            print_usage()
            exit(0)
        elif (arg in ("--run", "-r")) and force is None and narg is None:
            force = True
        else:
            prompt.append(arg)

    if model is None:
        model = Model.meta

    if force is None:
        force = False

    if shell is None:
        shell = determine_shell()

    prompt_str: str = " ".join(prompt)

    command = generate_command(model, prompt_str, shell, force)
    print(command)
    os.system(command)

if __name__ == '__main__':
    main()
