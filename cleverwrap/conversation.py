import requests


class Conversation:
    def __init__(self, api):
        self.api = api
        self.cs = ""
        self.count = 0
        self.output = ""
        self.convo_id = ""
        self.history = {}
        self.time_taken = 0
        self.time_elapsed = 0

    def say(self, text):
        """
        Say something to www.cleverbot.com
        :type text: string
        Returns: string
        """

        params = {
            "input": text,
            "key": self.api.key,
            "cs": self.cs,
            "conversation_id": self.convo_id,
            "wrapper": "CleverWrap.py"
        }

        reply = self.api._send(params)
        self._process_reply(reply)
        return self.output

    def _process_reply(self, reply):
        """ take the cleverbot.com response and populate properties. """
        self.cs = reply.get("cs", None)
        self.count = int(reply.get("interaction_count", None))
        self.output = reply.get("output", None)
        self.convo_id = reply.get("conversation_id", None)
        self.history = {key: value for key, value in reply.items() if key.startswith("interaction")}
        self.time_taken = int(reply.get("time_taken", None))
        self.time_elapsed = int(reply.get("time_elapsed", None))

    def reset(self):
        """
        Drop values for self.cs and self.conversation_id
        this will start a new conversation with the bot.
        """
        self.cs = ""
        self.convo_id = ""
