import asyncio
import websockets
import sys

# start the websocket client
async def start_client():
    async with websockets.connect("ws://localhost:8765") as websocket:
        print("Press Enter to buzz!")
        while True:
            if sys.stdin.readline().strip() == '':
                await websocket.send("buzzz")
                message = await websocket.recv()
                print(message)
                break

# run the client
asyncio.run(start_client())