import logging
from typing import List

from wcg_server.user import User

log = logging.getLogger(__name__)


class Match(object):
    def __init__(self, users: List[User]):
        self.users = users  # type: List[User]
