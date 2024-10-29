# xor

I mean, it's xor, what much more is there to say? Well okay it's quite handy. If you give it numbers, it'll just XOR them together nothing fancy.

```
$ xor 8 1 3 

9
```

Though I mainly wanted this so that I could pipe stuff into an xor that will run through every byte and xor it with every number in the order each number was provided.

```
ifconfig | xor 923 23945 1892 > ifconfig.xor
```

For encryption? Hell no. To block highlight stuff in Neovim with virtual edit turned on and be able to `:!xor 34 35` though? That's exactly what I made it for. The easily reversible nature of XOR makes it very convenient for macros where you'd like to filter out characters when performing searches when making recursive macros, and later restoring them.

Or just filling an empty space with a bunch of nonsense to be able to test navigation plugins, or just scramble data around, that sort of stuff.



