# cmake-init

Kind of like the cmake equivalent of `cargo init`, will populate the current directory with everything necessary for a minimal CMake C/C++ project. If called like this: `cmake-init c` then it will generate a C project instead. 

It will create a number of files and perform various actions.

- Creates Following
    - `LICENSE` (GPL v3.0)
    - `.gitignore`
    - `.clang-format`
    - `CMakeLists.txt`
    - `build` (bash script)
    - `README.md` 
    - `out/`
    - `src/main.cpp` or `src/main.c`
        Contains a hello world, with the most commonly used headers already included.

- Runs Following
    - `git init`

---



