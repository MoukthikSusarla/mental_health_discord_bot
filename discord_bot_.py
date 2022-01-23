from discord.ext import commands
import requests
import json 
import random
from dotenv import load_dotenv
load_dotenv 





bot=commands.Bot(command_prefix="$")
motivate_words=['motivate','inspire','feeling lazy','lazy','tired']
sad_words=['sad','depressed','fucked up','angry','miserable','depressing','lonely','alone','anxious']
encouraging_words=['Cheer up mate!','Hang in there.','This too shall pass!','You are the best sweetheart!']
trigger_words=['dead','die','suicide','kms','kill',"hadn't been born",'if i see you again','better off dead','no way out','better off without me']


def get_quote():
    response=requests.get("https://zenquotes.io/api/random")
    json_data=json.loads(response.text)
    quote=json_data[0]['q']+ " -"+json_data[0]['a']
    return (quote)

@bot.event
async def on_ready():
    print(f'{bot.user} has succesfully logged in!')



@bot.event
async def on_message(message):
    if message.author==bot.user:
        return

    if message.content.lower() in ('hi','hello','hey'):
        await message.channel.send(f'Hey! {message.author}, hope you are doing well!')

    if message.content.lower() in ('bye','gtg','goodbye'):
        await message.channel.send(f'See you soon {message.author}! Take care.')

    if any(word in message.content.lower() for word in motivate_words):
        quote=get_quote()
        await message.channel.send(quote)


    if any(word in message.content.lower() for word in sad_words):
        await message.channel.send(random.choice(encouraging_words))
        quote=get_quote()
        await message.channel.send(quote)

    if any(word in message.content.lower() for word in trigger_words):
        await message.channel.send(random.choice(encouraging_words))
        await message.channel.send("Your life is invaluable, please do not take any hasty decison")
        await message.channel.send("Think about your loved ones!")
        await message.channel.send("Please give a call at '1800-5990019' or '112'")

        
        await message.channel.send(quote)

    
    await bot.process_commands(message)



@bot.command()
async def cube(ctx,arg):
    print(arg)
    await ctx.send(int(arg)**3)

bot.run(config.TOKEN)

    
