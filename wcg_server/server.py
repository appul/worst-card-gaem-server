import logging
from typing import List

from wcg_server.match import Match
from wcg_server.user import User

log = logging.getLogger(__name__)


class Server(object):
    def __init__(self):
        pass

    def create_match(self, users: List[User]) -> Match:
        pass
