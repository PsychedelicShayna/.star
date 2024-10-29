# epd (Edit, Pipe, Delete)

Conceptually pretty simple, but incredibly useful. This command creates a temporary file, opens it in your default editor as defined by your EDITOR environment variables (falls back to vim) if the environment variable doesn't eixst. Then, upon saving and quitting, the contents of the file are piped in to the command following epd.


```
  epd (E)dit (P)ipe (D)elete

  Usage: epd [COMMAND]
  
  This script creates a temporary file, opens it with your editor (as defined by the $EDITOR environment variable),
  and then pipes the file's contents to the specified command. After piping the contents, the temporary file is deleted.
  It edits, pipes, deletes.
  
  Example:
    epd hexdump
  
  Options:
     --help    Display this help message and exit. 
```

A visual example of how using `epd` to pipe content to another command can be seen here (formerly called ped):

https://github.com/user-attachments/assets/62b1bea5-709d-4f38-802f-fbc5cb6385e4
