from telethon.sync import TelegramClient, events
from telethon import functions, types
api_id = '29666124'
api_hash = '24b3a73859eb64a6b0074d2e8d2a0ce8'


with TelegramClient('test.session', api_id, api_hash) as client:
 print("Ishladi!")

@client.on(events.NewMessage(pattern=""))
async def inf_online(e):
    await e.message.mark_read()
    
@client.on(events.NewMessage)
async def my_event_handler(event):
    if 'Salom' in event.raw_text:
        await event.reply('Alik, Salom')
     
@client.on(events.NewMessage)
async def my_event_handler(event):
    if 'Zoʻrma' in event.raw_text:
        await event.reply('zoʻr, oʻzingchi')
        
@client.on(events.NewMessage)
async def my_event_handler(event):
    if 'Qalesan' in event.raw_text:
        await event.reply('zoʻr, oʻzingchi')
                
@client.on(events.NewMessage)
async def my_event_handler(event):
    if 'Qalesiz' in event.raw_text:
        await event.reply('zoʻr, oʻzingizchi')
                
@client.on(events.NewMessage)
async def my_event_handler(event):
    if 'Makamma' in event.raw_text:
        await event.reply('Makkamm')
                
@client.on(events.NewMessage)
async def my_event_handler(event):
    if 'Zoʻrma' in event.raw_text:
        await event.reply('zoʻr, oʻzingchi')
                
                                              
client.start()
client.run_until_disconnected()