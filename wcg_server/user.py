import logging
from typing import List

from wcg_server.deck import Deck

log = logging.getLogger(__name__)


class User(object):
    def __init__(self, username):
        self.username = username  # type: str
        self.decks = []  # type: List[Deck]
