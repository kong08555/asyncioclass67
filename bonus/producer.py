from aiokafka import AIOKafkaProducer
import asyncio

async def send_messages():
    producer = AIOKafkaProducer(
        bootstrap_servers='172.16.46.107:9092')
    await producer.start()
    try:
        while True:
            await producer.send_and_wait("my_topic", b"hello! from apache kafka1!")
            print("send : hello! from apache kafka!")
            await asyncio.sleep(3)
    finally:
        await producer.stop()


asyncio.run(send_messages())
