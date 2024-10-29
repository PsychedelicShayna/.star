# goimg (Google Images)

Formulates a Google Images search query from the supplied arguments, an dpens
the link in your default browser.

Example
```
$ goimg Linux distro venn diagram
```

Would be the same as heading to https://www.google.com/search?q=goim+Linux+distro+venn+diagram&udm=2 in your default browser.
Python is used to formulate the URL, and then it's just opened via xdg-open.

