# Make executable

## Overview

This is a simple Sublime Text 3 package that adds a hotkey and command to set the executable bit on the current file.

## Usage

The hotkey defaults to <kbd>Alt</kbd> + <kbd>Shift</kbd> + <kbd>X</kbd>. Use the `make_file_executable` command in your key bindings to customize it, e.g.:


```json
[
    { 
      "keys": ["alt+shift+x"], "command": "make_file_executable"
    }
]
```

In addition to the hotkey, you can access the plugin via the command palette (command: *Make file executable*).

## License

This plugin is licensed under the [GNU GPLv3](http://www.gnu.de/documents/gpl-3.0.en.html). A copy of the license is included in the LICENSE file that accompanies this README.

*Copyright 2014 Glutanimate*.