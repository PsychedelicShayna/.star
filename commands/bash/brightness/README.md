# brightness

A convenient way to change the brightness of your monitors through xrandr.

## Usage

```
Usage: brightness [BRIGHTNESS] [DISPLAY...]
       brightness [COMMAND]

Commands:
  list, -l, --list          List available displays.
  help, -h, --help          Show this help message.

If BRIGHTNESS is provided, the brightness value is set for all displays by default.
If specific DISPLAY arguments are provided, brightness is only set for those displays.
```

## Examples:

```
$ brightness 1.2 DP-4 HDMI-0

Set brightness to 1.2 for DP-4
Set brightness to 1.2 for HDMI-0
```

```
$ brightness -l

Available displays:
DP-4
HDMI-0
HDMI-1
```

