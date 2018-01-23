class Response:
    def __init__(self, reply):
        self.cs = reply.get("cs", None)
        self.count = int(reply.get("interaction_count", None))
        self.output = reply.get("output", None)
        self.convo_id = reply.get("conversation_id", None)
        self.history = {key: value for key, value in reply.items() if key.startswith("interaction")}
        self.time_taken = int(reply.get("time_taken", None))
        self.time_elapsed = int(reply.get("time_elapsed", None))
