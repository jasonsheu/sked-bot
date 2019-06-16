import discord
import time
from datetime import datetime, timedelta

import asyncio

from discord.ext import commands
bot = commands.Bot(command_prefix='!sked ')

class Reminder:
    def __init__(self, message, time):
        self.message = message
        self.time = time

    def __lt__(self, other):
        return self.time < other.time
    def __str__(self):
        return self.message + ' will be pinged at ' + str(self.time)


class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    # for inserting an element in the queue
    def add(self, data):
        self.queue.append(data)

    # for popping an element based on Priority
    def pop(self):
        min = self.queue[0]
        index = 0
        for i in range(len(self.queue)):
            if self.queue[i] < min:
                min = self.queue[i]
                index = i
        del self.queue[index]
        return min


        return item

    def peek(self):
        min = self.queue[0]
        index = 0
        for i in range(len(self.queue)):
            if self.queue[i] < min:
                min = self.queue[i]
                index = i
        return min




pq = PriorityQueue()

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='with your mom'))
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command(name="remind")
async def test(ctx, message, time):
    d = datetime.strptime(time, '%b %d %Y %I:%M%p')
    r = Reminder(message, d)
    pq.add(r)
    print(pq)
    await ctx.send('creating reminder ' + message + ' that will go off at ' + time +' PST')

@bot.command(name="pop")
async def test(ctx):
    print(pq.pop())

async def check_time():
    await bot.wait_until_ready()

    while not bot.is_closed():
        current_time = datetime.now()
        if pq.isEmpty() == False:
            check = pq.peek().time
            if check <= current_time:

                print("MATCH!!!!!!!!!!!!!!!!!!!!!!!!!!")
                pq.pop()
                print(pq)
        await asyncio.sleep(1)


@bot.command(name='lol')
async def ping(ctx):
    await ctx.send('@everyone lol')


@bot.command()
async def info(ctx):
    embed = discord.Embed(title="sked bot", description="Creates convenient reminders for your server!", color=0xeee657)

    # give info about you here
    embed.add_field(name="author: Jason Sheu", value="Burd#9558")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="[Invite link](<https://discordapp.com/api/oauth2/authorize?client_id=589642723934470204&scope=bot>)")

    await ctx.send(embed=embed)

bot.loop.create_task(check_time())
bot.run('NTg5NjQyNzIzOTM0NDcwMjA0.XQWpow.jMiLZPd5J5lax6ZkMWHONmTXVhs')