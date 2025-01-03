from .instacog import InstaCog


async def setup(bot):
    await bot.add_cog(InstaCog(bot))
