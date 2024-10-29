# tmpcode

A temporary coding environment manager, that can create new language specific temporary coding environments in your `/tmp` folder before opening your editor in said directory. It can manage several directories at a time, and let you pick from them, or defaults to the last one that was used if no arguments are provided. All the setup for that particular language is done autoamtically, e.g. Python sets up a virtual environment and sources it for you, and automatically deactivates when leaving the editor. Every language has its own setup, so not every language is supported, only the ones I tend to  use. Some involve fewer steps.


Just making a new Rust environment...

```
tmpcode new rust
```

Isn't far from just doing `cargo new` in your `/tmp` folder, minus the fact that you can manage several of them, but for other languages, setup might be more complicated. 

This script's purpose is to generalize that process, where you're writing something in some language which has some project structure, and you just wanna quickly hop in, test something, hop out, but also not lose the code entirely upon leaving, letting you decide when to purge, or have it get purged on reboot.

```
tmpcode new cpp
```

Would be complicated, but thankfully I already made [cmake-init](../cmake-init/) so C/C++ projects are easy to set up.

I'd like to add as many language project setups as I can in the future, though there are only a few supported ones at the moment.

- Python
- Rust
- C/C++
- Lua
- Fish

I'd love to add

- Haskell
- Assembly
- OCaml
- Zig
- Go
- Elixir/Gleam/Erlang (BEAM VM)
- Java/Kotlin/Scala/Clojre (basically any project using a JVM language that generates directory spaghetti)
- .. more

Although I feel like this is beyond the scope of a Bash script and would be much more useful as a proper CLI utility.
