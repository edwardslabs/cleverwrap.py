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

class CleverWrap:
    """ A simple wrapper class for the www.cleverbot.com api. """

    url = "https://www.cleverbot.com/getreply"
    
    def __init__(self, api_key, name="CleverBot"):
        """ Initialize the class with an api key and optional name 
        :type name: string
        :type api_key: string
        :type history: dict or maybe a list
        :type convo_id: string
        :type cs: string
        :type count: int
        :type time_elapsed: int
        :type time_taken: int
        :type output: string
        """
        self.name = name
        self.key = api_key
        self.history = {}
        self.convo_id = ""
        self.cs = ""
        self.count = 0
        self.time_elapsed = 0
        self.time_taken = 0
        self.output = ""

    def say(self, text):
        """ 
        Say something to www.cleverbot.com
        :type text: string
        Returns: string
        """

        params = {
            "input": text,
            "key": self.key,
            "cs": self.cs,
            "conversation_id": self.convo_id,
            "wrapper": "CleverWrap.py"
        }

        reply = self._send(params)
        self._process_reply(reply)
        return self.output


    def _send(self, params):
        """
        Make the request to www.cleverbot.com
        :type params: dict
        Returns: dict
        """
        # Get a response
        try:
            r = requests.get(self.url, params=params)
        # catch errors, print then exit.
        except requests.exceptions.RequestException as e:
            print(e)
        return r.json()


    def _process_reply(self, reply):
        """ take the cleverbot.com response and populate properties. """
        self.cs = reply.get("cs", None)
        self.count = reply.get("interaction_count", None)
        self.output = reply.get("output", None)
        self.convo_id = reply.get("conversation_id", None)
        self.history = {key:value for key, value in reply.items() if key.startswith("interaction")}
        self.time_taken = reply.get("time_taken", None)
        self.time_elapsed = reply.get("time_elapsed", None)

    def reset(self):
        """
        Drop values for self.cs and self.conversation_id
        this will start a new conversation with the bot.
        """
        self.cs = ""
        self.convo_id = ""
