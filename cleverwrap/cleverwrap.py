"""
CleverWrap.py

Python wrapper for Cleverbot's API.
http://www.cleverbot.com/api

Copyright 2017 Andrew Edwards

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import requests

from cleverwrap.conversation import Conversation


class CleverWrap:
    """ A simple wrapper class for the www.cleverbot.com api. """

    url = "https://www.cleverbot.com/getreply"

    def __init__(self, api_key, name="CleverBot"):
        """ Initialize the class with an api key and optional name 
        :type api_key: str
        :type name: str
        """
        self.name = name
        self.key = api_key
        self._default_conversation = None

    def new_conversation(self):
        return Conversation(self)

    @property
    def default_conversation(self):
        if self._default_conversation is None:
            self._default_conversation = self.new_conversation()

        return self._default_conversation

    def say(self, text):
        """ 
        Say something to www.cleverbot.com
        :type text: string
        Returns: string
        """

        return self.default_conversation.say(text)

    def _send(self, params):
        """
        Make the request to www.cleverbot.com
        :type params: dict
        Returns: dict
        """
        # Get a response
        try:
            r = requests.get(self.url, params=params)
            r.raise_for_status()
        except requests.exceptions.RequestException as e:
            # catch errors, print then exit.
            print(e)
            raise  # Propagate the exception up the call stack so the calling code can catch it

        return r.json()

    def reset(self):
        """
        Drop values for self.cs and self.conversation_id
        this will start a new conversation with the bot.
        """
        return self.default_conversation.reset()
