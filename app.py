import random
import discord
from discord.ext import commands

# Função


def dice(command):
    hits = 0
    fail = 0
    repeat = 0
    dice_roll = []

    command = command.replace('!roll', '')
    command = command.split('d')
    command[0] = int(command[0])
    command[1] = int(command[1])

    # Loop principal
    while command[0] != 0:
        repeat = 0
        for a in range(0, command[0]):
            random_value = random.randint(1, command[1])
            if random_value % 2 == 0:
                hits += 1
                if random_value == 6:
                    repeat += 1
            else:
                fail += 1
                if random_value == 1:
                    hits -= 1
            dice_roll.append(random_value)
        command[0] = repeat
    return hits, fail, dice_roll


# Condicion
bot = commands.Bot("!")

# Check conection


@bot.event
async def on_ready():
    print(f'Estou conectado como {bot.user}')

# Command dice


@bot.command(name='roll')
async def mandar_oi(ctx, *expression):
    expression = ''.join(expression)
    result = dice(expression)
    await ctx.send(f'Acertos: {result[0]} | Falhas: {result[1]} | Dado: {result[2]}')

bot.run("MTAyMDE2MTQyOTM1OTI5NjUxNA.G8W0qB.Co5EBo1W8FIeXN0us7HGVhU6DlV2n9iMnQjNPg")
