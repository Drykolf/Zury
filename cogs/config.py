from discord.ext import commands

class Config(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('Config cog is ready!')
        
async def setup(bot):
    await bot.add_cog(Config(bot))