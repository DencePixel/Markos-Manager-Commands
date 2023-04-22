class VerificationModal(discord.ui.Modal):
    def __init__(self):
        randomstring = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=5))
        title = f"Verification - String: {randomstring}"
        self.title = title
        self.randomstr = randomstring
        super().__init__(title=title)

    Username = ui.TextInput(label="Gain Access", placeholder="Example: marko!#2543", style=discord.TextStyle.short)
    String = ui.TextInput(label="Random String", placeholder="Enter the string shown in the title", style=discord.TextStyle.short)

    async def on_submit(self, interaction: discord.Interaction):
        username = self.Username.value
        string = self.String.value

        if str(interaction.user) == username:
            if self.randomstr == string:                
                guild = client.get_guild(1035586745472913438)
                member = guild.get_member(interaction.user.id)
                role1 = discord.utils.get(guild.roles, id=1099232855856521247)
                role = discord.utils.get(guild.roles, id=1093999920886857869)
                await member.remove_roles(role)
                await member.add_roles(role1)


                await interaction.response.send_message(content=f"Thank you for verifying {username}!")
            
            else:
                await interaction.response.send_message(f"You have failed verification {interaction.user}. Reason: Incorrect string")



        else:
            await interaction.response.send_message(f"You have failed verification {interaction.user}. Reason: Incorrect username")

        


class Verification(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label=f"Verify Me!", style=discord.ButtonStyle.green)
    async def gray_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(VerificationModal())

@client.tree.command()
async def verify(interaction: discord.Interaction):
    channel = client.get_channel(1096857692431187999)
    guild = client.get_guild(1035586745472913438)
    verifychannel = client.get_channel(1096857704082981045)
    logchannel = client.get_channel(1096841685184557156)


    view2 = Verification()

    await interaction.response.send_message(f"{interaction.user.mention} check your direct messages for verification!")
    await interaction.user.send(f"Please verify {interaction.user.mention}", view=view2)
