# Suggest

This is just a tgpt wrapper that allows you to easily do stuff like

```
suggest copy ./suggest.py to /usr/bin without py extension, and change the owner and group to root with 0755 perms
suggest --using phind --for xonsh enable xonsh vim keybindings --run
```

Usage:

```
Usage: suggest 'prompt' [--using <model>|-m] [--for <shell>|-s] [--run|-r] [--help|-h]
Where model: meta, phind, gpt, claude, mistral
Where shell: anything. Automatically detected if not included.
Run: optional, if supplied the generated shell command will be immediately executed
```
