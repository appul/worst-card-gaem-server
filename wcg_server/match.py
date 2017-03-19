import logging
from typing import List

from wcg_server.Player import Player
from wcg_server.user import User

log = logging.getLogger(__name__)


class Match(object):
    def __init__(self, users: List[User]):
        self.player = [Player(user) for user in users]  # type: List[Player]
