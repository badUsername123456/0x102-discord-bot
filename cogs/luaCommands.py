from cache import cacheGet
from discord.ext import commands
from cogs._lua import run
import aiosqlite
from discord import (
    Interaction,
    app_commands,
    Object
)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        LuaCog(bot),
        guilds=[Object(id=cacheGet("id"))]
    )


class LuaCog(commands.Cog):
    def __init__(self: "LuaCog", bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command()
    async def runcommand(self: "LuaCog", ctx: Interaction, name: str = "echo") -> None:
        if not name:
            return await ctx.response.send_message("Please provide a command name.")

        async with aiosqlite.connect("D:\\programing\\0x102-discord-bot\\commands.db") as db:
            async with db.cursor() as curr:
                await curr.execute(f"SELECT code FROM commands WHERE name = \"{name}\"")
                result = await curr.fetchone()
                await run(result[0], ctx)

    @app_commands.command()
    async def inspectcommand(self: "LuaCog", ctx: Interaction, name: str = "echo") -> None:
        async with aiosqlite.connect("D:\\programing\\0x102-discord-bot\\commands.db") as db:
            async with db.cursor() as curr:
                await curr.execute(f"SELECT code FROM commands where name = \"{name}\"")
                result = await curr.fetchall()
                return await ctx.response.send_message(f"```lua\n{result[0][0]}\n```")
