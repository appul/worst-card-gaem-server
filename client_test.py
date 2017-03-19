#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import websockets

async def hello():
    async with websockets.connect('ws://localhost:8765') as websocket:
        while True:
            message = await websocket.recv()
            print(message)
            response = input()
            await websocket.send(response)


asyncio.get_event_loop().run_until_complete(hello())
