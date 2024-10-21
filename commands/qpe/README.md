# QPE (Quick Python Expressions)

The concept is pretty simple, quickly evaluate a Python expression, but with
quality of life in regards to how you can invoke it. It's not just Python -c
it's a lot more.

It goes hand in hand with the Fish abbreviation in [qpe.fish](./qpe.fish),
which saves you from having to put your expression in quotes.

I normally just use it as a calculator or base converter..

```sh
$ qpe 'bin(732)'
> 0b1011011100

$ qpe '(2**16) / 2 - 1'
> 32767.0
```

But the thing that makes it special is that every argument will be treated as 
a statement rather than an expression, up until the very last argument, which 
will be treated as an expression and is automatically printed out.

That fact makes it possible to do:

```sh
$ qpe 'import time' 'time.time()'
> 1729485131.4285324
```

Or for instance, defining state..

```sh
$ qpe 'x=34' 'y=35' 'x+y'
> 69
```

Hell you can define entire functions if you really want to.

```sh
$ qpe '
def why_would_you_do_this():
    return "For science!"
' 'why_would_you_do_this()'

> For science!
```

Or base85 encode every single line in a binary file and receive the output
as plaintext lines.. for.. reasons.

```sh
$ qpe 'from base64 import b85encode as b8' \
      'bl=open("file.bin", "rb").read().split(b"\n")' \
      'b"\n".join([b8(x) for x in bl)'
```


