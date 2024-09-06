import asyncio
import websockets

# create an empty list to store clients
clients = []

# initialize fastest_time variable
fastest_time = None

# define a function to handle incoming messages from clients
async def handle_message(websocket, path):
    global clients
    global fastest_time
    message = await websocket.recv()
    if message == "buzzz":
        response_time = asyncio.get_event_loop().time()
        if fastest_time is None:
            await websocket.send('First place!')
            fastest_time = response_time
        else:
            t = round(response_time - fastest_time, 2)
            await websocket.send(f'Response time: {t} sec slower')

# start the websocket server
async def start_server():
    async with websockets.serve(handle_message, "localhost", 8765):
        print("Server is running on localhost:8765")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(start_server())