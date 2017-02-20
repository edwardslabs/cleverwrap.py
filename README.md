# CleverWrap.py

A simple python wrapper class to interact with the official [CleverBot API](http://www.cleverbot.com/api).

This package was created to run on python3

# Installing

You can install cleverwrap.py from pypi using: `pip install cleverwrap`

You can also clone this repository and import the library directly.

# Usage

```
>>> from cleverwrap import CleverWrap
>>> cw = CleverWrap("API_KEY")
>>> cw.say("Hello CleverBot.")
"Hello Human."
>>> cw.reset() # resets the conversation ID and conversation state.
```

# License

Copyright 2017 Andrew Edwards using the [MIT License](http://opensource.org/licenses/MIT).

