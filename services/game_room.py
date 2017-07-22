from models.game_room import GameRoom


class GameRoomService:

    _rooms = {}

    def __init__(self):
        pass

    def create_room(self, id, creator, password=None):
        game_room = GameRoom(id)

        self._rooms[id] = game_room

        return game_room

    def get_rooms(self):
        return self._rooms
