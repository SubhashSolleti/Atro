import discord


def send_message(name_1):
    name = 'member'

    if name == 'member':
        TOKEN = 'MTA3ODczMDEyODk1NzM3ODY0Mg.GKxVSg.A_81vhLOSGnqOd84ChBnSG0Ce9Y0qL_Xs27bRM'
        status = 'member'
        intents = discord.Intents.default()
        client = discord.Client(intents=intents)

        @client.event
        async def on_ready():
            channel = client.get_channel(1078722332446707762)
            await channel.send(f'A lab member has entered the lab: {name_1}')

        client.run(TOKEN)
