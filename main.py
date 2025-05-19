from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

@app.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket): 
    await websocket.accept()
    try:
        while True:
            message = await websocket.receive_text()
            print(f"{message}   message")
            # Get and update session
            await websocket.send_text(f"You said: hello")
    except WebSocketDisconnect:
        # logMessage("From Here")
        print("Disconnected and cleaned up session.")