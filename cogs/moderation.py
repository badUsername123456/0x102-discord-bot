from discord.ext import commands
from ._comand_chache import register_commands
from discord import (
    Interaction,
    app_commands,
    Object,
    Member
)


class Moderation(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        register_commands(self)
        self.bot = bot

    @app_commands.command()
    @app_commands.describe(user="The user you want to kick.")
    @app_commands.describe(reason="Why you want to kick the user.")
    async def kick(self, interaction: Interaction, user: Member, *, reason: str = "You  have been naughty") -> None:
        try:
            await user.kick(reason=reason)
            await interaction.response.send_message(f"successfully kicked {user.name} for \"{reason}\"")

        except Exception as e:
            await interaction.response.send_message(f"error: {e}")

    @app_commands.command()
    @app_commands.describe(user="The user you want to ban.")
    @app_commands.describe(reason="Why you want to ban the user.")
    async def ban(self, interaction: Interaction, user: Member, *, reason: str = "you have been naughty"):
        try:
            await user.ban(reason=reason)
            await interaction.response.send_message(f"successfully kicked {user.name} for \"{reason}\"")

        except Exception as e:
            await interaction.response.send_message(f"error: {e}")

    def __cog_docs__(self) -> str:
        return """
        This cog is used to kick and ban users.
        You can use the commands:
            -kick
            -ban
        """


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        Moderation(bot),
        guilds=[Object(id=938541999961833574)]
    )
