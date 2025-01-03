from redbot.core import commands

class InstaCog(commands.Cog):

    def __init__(self, bot, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if "https://www.instagram.com/" in message.content:
            converted_link = message.content.replace(
                "https://www.instagram.com/",
                "https://www.instagramez.com/"
            )

            await message.channel.send(f'Yo, you forgot the embed link: {converted_link}')
