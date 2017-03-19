import logging
from typing import List

import asyncio
import websockets

from wcg_server.match import Match
from wcg_server.user import User

log = logging.getLogger(__name__)


class Server(object):
    def __init__(self, address, port):
        self.address = address  # type: str
        self.port = port  # type: int
        self.clients = dict()

    def start(self):
        async def identify(websocket, path):
            await websocket.send("What's your username?")
            username = await websocket.recv()
            print("Created user {}".format(username))
            self.clients[websocket] = username
            await websocket.send("Dank")

        start_server = websockets.serve(identify, self.address, self.port)

        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

    def create_match(self, users: List[User]) -> Match:
        pass
