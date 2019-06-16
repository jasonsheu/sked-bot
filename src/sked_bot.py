import discord
import datetime

time = datetime.datetime.now()

class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print(self.__dict__.keys())
        print('------')
        await message.channel.send('usage: !sked message time roles')



    async def on_message(self, message):
        # we do not want the bot to reply to itself
        commands = message.content.split()
        print(message)
        if message.author.id != self.user.id:
            print(message.content, message.author)

            print(commands)
        if message.author.id == self.user.id:
            return


        if message.content.startswith('!sked'):

            await message.channel.send('Yes {0.author.mention}?'.format(message))



client = MyClient()
client.run('NTg5NjQyNzIzOTM0NDcwMjA0.XQWpow.jMiLZPd5J5lax6ZkMWHONmTXVhs')
