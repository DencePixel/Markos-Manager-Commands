@client.tree.command()
async def joke(interaction: discord.Interaction):
    response = requests.get('https://official-joke-api.appspot.com/random_joke')
    joke = response.json()
    await interaction.response.send_message(f'{joke["setup"]}\n{joke["punchline"]}')
