from aiokafka import AIOKafkaProducer
import asyncio

async def send_messages():
    producer = AIOKafkaProducer(
        bootstrap_servers='192.168.128.29:9092')
    await producer.start()
    try:
        while True:
            await producer.send_and_wait("my_topic", b"hello! from 192.168.128.136!")
            print("send : hello! from 192.168.128.136!")
            await asyncio.sleep(3)
    finally:
        await producer.stop()


asyncio.run(send_messages())
