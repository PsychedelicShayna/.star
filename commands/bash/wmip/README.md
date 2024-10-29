# wmip (What's My IP?)

Just curls https://myip.wtf/ to check what your public IP address is.
Available formats: plaintext, json, yaml, xml

```
  echo "Missing output format, provide one."
  echo "Usage: wmip [text|json|yaml|xml]"
```

Example Output (redacted obviously):

```
$ wmip json

{
    "YourFuckingIPAddress": "123.456.789.1",
    "YourFuckingLocation": "Antarctica",
    "YourFuckingHostname": "133.734.356.942-yourisp.toplevel.domain",
    "YourFuckingISP": "ICE",
    "YourFuckingTorExit": true,
    "YourFuckingCity": "Arco",
    "YourFuckingCountry": "Penguin Land",
    "YourFuckingCountryCode": "AUR"
}
```


