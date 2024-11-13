import asyncio
import ezgmail,os
from ezgmail import init
import time
from telethon import TelegramClient

api_id='your api'
api_hash='your api hash'
massage_='massage.txt'
client=TelegramClient('sessions',api_id,api_hash,)

with open(massage_,'a')as file:
    last_massage_=set(line.strip()for line in file)
    

async def getmassage():
    await client.start()
    massage = await client.get_messages('channel_example',limit=1)
    
    message= massage[0].text
    if massage not in last_massage_:
        return message
    elif massage in last_massage_ :
        feedback=input('massage already sent, if you want to bypass that type BYPASS')
        if feedback == 'BYPASS':
            return massage

message= asyncio.run(getmassage())

os.chdir('credentieals json location here(gmail api) ')

ezgmail.init()

ezgmail.send(f'EXAMPLE@gmail.com','new massages',message)

with open(massage_,'a') as file:
    file.write(message)

print('Sending the massage...')
time.sleep(3)
print('Massage sent.')
