import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        print(message.content, message.author)
        if message.author.id == self.user.id:
            return


        if message.content.startswith('!hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))


client = MyClient()
client.run('NTg5NjQyNzIzOTM0NDcwMjA0.XQWpow.jMiLZPd5J5lax6ZkMWHONmTXVhs')
