"""
Copyright (C) 23/07/2022 - Han P.B Manseck.

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation files
(the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge,
publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from discord import Interaction, app_commands, Object
from cogs._help_command_setup import record  # type: ignore
from discord.ext import commands  # type: ignore
from datetime import datetime
from random import choice
import discord
import aiohttp


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(UtilsCog(bot), guilds=[Object(id=938541999961833574)])


class UtilsCog(commands.Cog):
    def __init__(self: "UtilsCog", bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @record()
    @app_commands.command(description="Gives a classic 8ball response.")
    async def ball(self: "UtilsCog", ctx: discord.Interaction):
        await ctx.response.send_message(
            choice(
                [
                    # yes responses
                    "my sources say yes",
                    "it is decidedly so",
                    "I think yes",
                    "As I see it, yes.",
                    "It is certain.",
                    "Most likely.",
                    "Outlook good.",
                    "Signs point to yes.",
                    "Without a doubt.",
                    "Yes.",
                    "Yes - definitely.",
                    "You may rely on it.",
                    # no responses
                    "my sources say no",
                    "better not",
                    "Don`t count on it.",
                    "My reply is no.",
                    "My sources say no.",
                    "Outlook not so good.",
                    "Very doubtful.",
                    "nope",
                    "100% no",
                    # uncertain responses
                    "better not tell you now",
                    "reply hazy ask again",
                    "Ask again later.",
                    "Cannot predict now.",
                    "Concentrate and ask again.",
                ]
            )
        )

    @record()
    @app_commands.command(name="inspire", description="sends an inspiring message.")
    async def inspire(self: "UtilsCog", ctx: Interaction):
        quote: str = await self._get_quote()
        await ctx.response.send_message(quote)

    @record()
    @app_commands.command(description="does a coin flip so heads or tails")
    async def coinflip(self: "UtilsCog", ctx: Interaction):
        await ctx.response.send_message(f'you have {choice(["heads", "tails"])}')

    @record()
    @app_commands.command(name="time", description="sends the current time")
    async def time(self: "UtilsCog", ctx: Interaction):
        now = datetime.now()
        dt_string: str = now.strftime("%d/%m/%Y %H:%M:%S")
        await ctx.response.send_message(f"date and time: {dt_string}")

    @record()
    @app_commands.command(name="sus", description="...")
    async def sus(self: "UtilsCog", ctx: Interaction):
        await ctx.response.send_message("ඞ sus")

    async def _get_quote(self: "UtilsCog") -> str:
        self.pass_()
        async with aiohttp.ClientSession() as session:
            response = await session.get("https://zenquotes.io/api/random")

            r: dict = await response.json()
            return f"{r[0]['q']} - {r[0]['a']}"

    @record()
    @app_commands.command(name="enchant", description="you can enchant your text maybe with sharpness?")
    @app_commands.describe(message="The text you want to enchant.")
    async def enchant(self: "UtilsCog", ctx: Interaction, *, message: str):
        """
        :param ctx: The `ctx` peramiter is passed by default by discord.py when executed
        :param message: The `message` peramiter is passed by the user of the command
        :return:
        """
        enchant: str = ""
        for character in message:
            try:
                enchant = (
                    enchant
                    + {
                        " ": " ",
                        "a": "ᔑ",
                        "b": "ʖ",
                        "c": "ᓵ",
                        "d": "↸",
                        "e": "ᒷ",
                        "f": "⎓",
                        "g": "⊣",
                        "h": "⍑",
                        "i": "╎",
                        "j": "⋮",
                        "k": "ꖌ",
                        "l": "ꖎ",
                        "m": "ᒲ",
                        "n": "リ",
                        "o": "𝙹",
                        "p": "!¡",
                        "q": "ᑑ",
                        "r": "∷",
                        "s": "ᓭ",
                        "t": "ℸ",
                        "u": "⚍",
                        "v": "⍊",
                        "w": "∴",
                        "x": " ̇/",
                        "y": "||",
                        "z": "⨅",
                    }[character]
                )

            except KeyError:
                enchant += character

        await ctx.response.send_message(enchant)

    def pass_(self) -> None:
        ...
