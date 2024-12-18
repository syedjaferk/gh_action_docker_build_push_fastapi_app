import uuid


class IdGenerator:
    def __init__(self):
        self._random_id = None

    def get_random_id(self):
        self._random_id = uuid.uuid4()
        return self._random_id
