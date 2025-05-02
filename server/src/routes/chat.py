@chat.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket, token: str = Depends(get_token)):
    await manager.connect(websocket)
    redis_client = await redis.create_connection()
    producer = Producer(redis_client)
    consumer = StreamConsumer(redis_client)

    try:
        while True:
            data = await websocket.receive_text()
            
            # Envia mensagem para o worker processar
            await producer.add_to_stream({"token": token, "message": data}, "message_channel")
            
            # Aguarda resposta
            response = await consumer.consume_stream("response_channel", block=1000)
            
            if response:
                for _, messages in response:
                    for msg_id, msg_data in messages:
                        if msg_data[b'token'].decode() == token:
                            await websocket.send_text(msg_data[b'message'].decode())
                            await consumer.delete_message("response_channel", msg_id)
    
    except WebSocketDisconnect:
        manager.disconnect(websocket)