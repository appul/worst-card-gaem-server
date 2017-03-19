import logging
from typing import List

from wcg_server.card import Card

log = logging.getLogger(__name__)


class Deck(object):
    def __init__(self):
        self.cards = []  # type: List[Card]
