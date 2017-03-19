import logging
from typing import List

from wcg_server.Player import Player
from wcg_server.user import User

log = logging.getLogger(__name__)


class Match(object):
    def __init__(self, users: List[User]):
        self.players = []  # type: List[Player]

        for user in users:
            self.players.append(Player(user))
