import pyrogram
from pyrogram import Filters, Client
from pyrogram.errors import FloodWait
import time
from pyrogram.errors import RPCError
import random


api_id = 1548292
api_hash = dd0af014e72d55fba13efbdc4507434f

app = Client("ishai", api_id, api_hash)

from_channel = -1001311939725
to_channel = -1001375861296

def from_channel_check(c, m):
    if m.forward_from_chat.id and m.forward_from_chat.id == from_channel:
        return True
    else:
        return False


@app.on_message(Filters.create(from_channel_check))
def forward(c, m):
    try:
        m.forward(to_channel)
    except FloodWait as e:
        sleep(e.x)
        m.forward(to_channel)


app.run()