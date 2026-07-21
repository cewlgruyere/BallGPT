import discord
from discord import app_commands
from ballsdex.core.bot import BallsDexBot
from discord.ext import commands
import asyncio
import random

answers = ["I like balls", "Definitely", "no", "not cool :(", "hi.. How can i assist you tomorrow?", "balls... mmm balls....", "give me more water for an answer", "buy plus to get this one", "do /admin balls spawn for free bals", "Ok! Added 10 coins to your balance.", "broke ngl.", "no", "didnt ask"]


class ballgpt(discord.ui.LayoutView):
    container1 = discord.ui.Container(
        discord.ui.TextDisplay(content="## BallGPT - The ultimate ball"),
        discord.ui.TextDisplay(content="-# [BallGPT is currently drinking water ples wait](https://github.com/cewlgruyere)"),
        discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.large),
        discord.ui.MediaGallery(
            discord.MediaGalleryItem(
                media="https://i.imgur.com/x2GBeHh.png",
            ),
        ),
    )

class answer(discord.ui.LayoutView):    
    def __init__(self, prompt):
        super().__init__(timeout=60)
        self.prompt = prompt
        self.build()
    
    def build(self):
        container1 = discord.ui.Container(
            discord.ui.TextDisplay(content="## BallGPT - the ballin ball"),
            discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.large),
            discord.ui.TextDisplay(content=f"### Prompt:\n {self.prompt}"),
            discord.ui.Separator(visible=False, spacing=discord.SeparatorSpacing.small),
            discord.ui.TextDisplay(content=f"### Answer:\n{random.choice(answers)}"),
        )
        
        media_gallery1 = discord.ui.MediaGallery(
            discord.MediaGalleryItem(
                media="https://i.imgur.com/cvPHYhW.gif",
            ),
        )

        self.add_item(container1)
        self.add_item(media_gallery1)


class BallGPT(commands.Cog):
    """
    BallGPT, does nothing
    """

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.is_this_true = app_commands.ContextMenu(name="@ballsdex is this true", callback=self.trueorfalse)
        self.bot.tree.add_command(self.is_this_true)

    @commands.hybrid_command()
    @app_commands.command()
    async def ask(self, interaction: discord.Interaction["BallsDexBot"], question: str):
        """
        Ask BallGPT - The ultimate ball

        Parameters
        ----------
        question: str
            The question that BallGPT - the ultimate bll will recieve.
        """

        await interaction.response.defer(thinking=True)

        message = await interaction.followup.send(view=ballgpt())
        await asyncio.sleep(10)
        await message.edit(view=answer(question))
    
    async def trueorfalse(self, interaction: discord.Interaction["BallsDexBot"], message: discord.Message):
        await interaction.response.send_message("I dunno")

