import discord
import os
import random

client = discord.Client()


sad_words = [
    "sad", "depressed", "unhappy", "angry", "miserable", "depressief",
    "ik wil dood"
]

starter_encouragements = [
    "Cheer up!", "Hang in there.", "You are a great person / bot!"
]

hello_statements = [
    "Hallo", "Goedendag", "Fawaka Dushi", "Sup bruh", "Hi", "Fock off, jk"
]

poiesz_statements = [
    "Poiesz is een fantastisch mooie winkel opgericht in het altijd walgelijke Friesland!",
    "Poiesz is een kut winkel opgericht in die homo provincie hiernaast!",
    "Poiesz is kut man!", "Ga leren googlen fso slet"
]

jt_statements = [
    "Ik ben Jan Theo en ik denk dat ik een gangster ben",
    "Ik ben Jan Theo en ik hou van roze! #gay",
    "Ik weet niet wie ik ben, misschien je moeder?",
    "Ik ben je bro of nee toch niet",
    "Kan jij mijn profielfoto zien? Nee? Dan mag ik je niet"
]


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

# quote command
    
#end quote

# Standard text commands
    if message.content.startswith('!commands'):
        await message.channel.send(
            'Dit zijn alle commands die je kan uitvoeren: !hello, !jt, !twss, !msn, !maker, !cytorick, !wappie, !corona, !of, !age, !poiesz, !corona'
        )

    if message.content.startswith('!hello'):
        await message.channel.send(random.choice(hello_statements))

    if message.content.startswith('!jt'):
        await message.channel.send(random.choice(jt_statements))

    if message.content.startswith('!twss'):
        await message.channel.send('That`s what she said!')

    if message.content.startswith('!msn'):
        await message.channel.send('Mooie schoenen, neuken?')

    if message.content.startswith('!maker'):
        await message.channel.send(
            'Ik ben gemaakt door cytorick, een geweldige programmeur!')

    if message.content.startswith('!cytorick'):
        await message.channel.send(
            'Cytorick is een lichtelijk narcistisch persoon!')

    if message.content.startswith('!wappie'):
        await message.channel.send(
            '"Van de honderd lampen in de bovenkamer branden er een paar niet. Niet het meest snuggere type" aldus Miertje'
        )

    if message.content.startswith('!of'):
        await message.channel.send(
            'Ik leef in de cloud en ben niet in staat om een OnlyFans te onderhouden! Dus nee ik heb geen OnlyFans!'
        )

    if message.content.startswith('!age'):
        await message.channel.send(
            'Een leeftijd heb ik niet! Ik ben ontwikkeld op 15-02-2021...')

    if message.content.startswith('!poiesz'):
        await message.channel.send(random.choice(poiesz_statements))

    if message.content.startswith('!corona'):
        await message.channel.send(
            'Pff hier vraag je me wat... Corona is een prima te doen biertje maar is sinds 2020 ook de benaming van een erg besmettelijk virus... Idk waarom je dit niet weet maar ja ik ben maar een bot en ik oordeel niet... :wink: '
        )


# The end

client.run(os.getenv('TOKEN'))
