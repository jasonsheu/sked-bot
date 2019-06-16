import discord
import datetime

time = datetime.datetime.now()
reminders = []


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print(self.__dict__.keys())
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!sked'):
            # commands = message.content.split()
            # r = Reminder(commands[1], commands[2])
            # print(r.message, r.time)
            await message.channel.send('Yes {0.author.mention}?'.format(message))



client = MyClient()
client.run('NTg5NjQyNzIzOTM0NDcwMjA0.XQWpow.jMiLZPd5J5lax6ZkMWHONmTXVhs')