import asyncpg
from discord import Object
from discord.ext import commands
from typing import List, Optional
import utils.settings as settings
import schemas.rpg.db_create as db

class Zury(commands.Bot):
    def __init__(
        self,
        *args,
        initialExtensions: List[str],
        dbPool: asyncpg.Pool,
        testingGuildId: Optional[str] = settings.TEST_GUILD,
        allowedGuild: Optional[str] = [settings.TEST_GUILD],
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.dbPool = dbPool
        self.testingGuildId = testingGuildId
        self.initialExtensions = initialExtensions
        self.allowedGuild = allowedGuild

    async def setup_hook(self) -> None:
        if self.dbPool is None:
            print("Connnection to database failed.")
            return
        else:
            print("Connection to database established")
        #Load commands
        for extension in self.initialExtensions:
            await self.load_extension(extension)
        if self.testingGuildId:
            guild = Object(self.testingGuildId)
            self.tree.copy_global_to(guild=guild)
            await self.tree.sync(guild=guild)
    
    async def create_tables(self) -> None:
        await db.create_dino_datatable(self.dbPool)
        await db.create_dino_capacities_datatable(self.dbPool)
        await db.create_dino_classifications_datatable(self.dbPool)
        await db.create_shiny_essences_datatable(self.dbPool)
        await db.create_player_dino_datatable(self.dbPool)
        await db.create_player_dino_capacities_datatable(self.dbPool)
        await db.create_player_dino_classifications_datatable(self.dbPool)
        await db.create_abilityrolls_datatable(self.dbPool)
        await db.create_abilityrolls_bonuses_datatable(self.dbPool)
        await db.create_player_bonuses_table(self.dbPool)
        
    async def starting_data(self) -> None:
        import schemas.rpg.admin_queries as ra
        #await ra.register_starting_capacities(self.dbPool)
        #await ra.register_starting_classifications(self.dbPool)
        #await ra.register_starting_abilities(self.dbPool)
        #await ra.register_starting_essences(self.dbPool)
