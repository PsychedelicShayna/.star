# mapan

A simple program to map arbitrary bytes coming from stdin to your choice of alphanumeric character sets. I mainly created this as a form of  generating data in Neovim to operateo n. You can use the mnemonic "sulane1234" to easily remember what charsets ycu can enable.

```
Usage: mapan [<charset-chars>|--help(-h)]

Examples: ..command | mapan nl1
          ..command | mapan u134
          ..command | mapan s
          ..command | mapan a

Charset Characters:
    e   | Everything
    --------------------------------------
    a   | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    u   | ABCDEFGHIJKLMNOPQRSTUVWXYZ
    l   | abcdefghijklmnopqrstuvwxyz
    --------------------------------------
    n   | 0123456789
    --------------------------------------
    s   | !"#$%&'()*+,-./:;<=>?@[\]^_`{{|}}~
    --------------------------------------
    1   | !"#$%&'()*+,-.     
    2   | :;<=>?@    
    3   | \][^_`    
    4   | }}|{{~

```

Example:

```
readf /dev/urandom -n 1000 | mapan 43
```


