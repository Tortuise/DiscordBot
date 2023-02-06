import discord
from discord.ext import commands

class buttonCancel(discord.ui.Button):
    def __init__(self):
        super().__init__(label="Cancel", style=discord.ButtonStyle.danger)

    async def callback(self, interaction: discord.Interaction):
        assert self.view is not None
        view: musicDropdownView = self.view

        view.stop()

class musicDropdownView(discord.ui.View):
    def __init__(self, options):
        self.index = -1
        super().__init__()

        self.add_item(musicDropdown(options))
        self.add_item(buttonCancel())

class musicDropdown(discord.ui.Select):
    def __init__(self, options):
        super().__init__(placeholder='Pick an audio file', min_values=1, max_values=1, options=options)
        
    async def callback(self, interaction: discord.Interaction):
        assert self.view is not None
        view: musicDropdownView = self.view

        view.index = int(interaction.data['values'][0][:1]) - 1
        view.stop()
    