import asyncio
import ezgmail,os
from ezgmail import init
import time
from telethon import TelegramClient

api_id='your api'
api_hash='your api hash'

client=TelegramClient('sessions',api_id,api_hash,)

async def getmassage():
    await client.start()
    massage = await client.get_messages('channel_example',limit=1)
    
    message= massage[0].text
    return message

message= asyncio.run(getmassage())

os.chdir('credentieals json location here(gmail api) ')

ezgmail.init()

ezgmail.send(f'EXAMPLE@gmail.com','new massages',message)


print('Sending the massage...')
time.sleep(3)
print('Massage sent.')