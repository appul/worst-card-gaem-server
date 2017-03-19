import logging
from typing import List

from wcg_server.deck import Deck

log = logging.getLogger(__name__)


class User(object):
    def __init__(self):
        self.decks = []  # type: List[Deck]
