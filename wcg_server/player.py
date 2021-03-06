import logging

from wcg_server.deck import Deck
from wcg_server.user import User

log = logging.getLogger(__name__)


class Player(object):
    def __init__(self, user: User):
        self.user = user  # type: User
        self.deck = None  # type: Deck
