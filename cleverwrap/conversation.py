from cleverwrap.response import Response


class Conversation:
    def __init__(self, api):
        self.api = api
        self.cs = ""
        self.convo_id = ""

    def say(self, text):
        """
        Say something to www.cleverbot.com
        :type text: string
        Returns: string
        """

        params = {
            "input": text,
            "cs": self.cs,
            "conversation_id": self.convo_id,
        }

        reply = Response(self.api._send(params))
        self.cs = reply.cs
        self.convo_id = reply.convo_id
        return reply.output

    def reset(self):
        """
        Drop values for self.cs and self.conversation_id
        this will start a new conversation with the bot.
        """
        self.cs = ""
        self.convo_id = ""
