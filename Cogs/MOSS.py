# imports Discord 
from discord import app_commands
from discord.ext import commands
from zipfile import ZipFile 
from utils.utils import *
import os

# adds my cog to the bot
async def setup(bot:commands.Bot):
    await bot.add_cog(MOSS(bot))

# constructor method that passes in Cog commands???
class MOSS(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    @app_commands.command(description="This will check if students are cheaters") # they ALL are
    @app_commands.default_permissions(administrator=True)
    async def moss(self, interaction:discord.Interaction):
        """ Run MOSS command
        Allows users to upload a zipfile and run the moss perl script on the discord server remotely.

        Args:
            upload_file (file): similar to course management upload file 
        Outputs:
            MOSS URL
        """
        

        mossuser = interaction.user.id
        print(mossuser)
        mosspath = f"/tmp/{mossuser}"
        if not os.path.exists(mosspath):
            os.mkdir(mosspath)

        # copied and pasted - needs fixed
        await interaction.response.send_message("Please attach a .zip file of all student code!", ephemeral=True)

        # saves file to the name of the .ZIP file that is given by the user
        file = await interaction.client.wait_for('message', check=lambda message: message.author == interaction.user)

        zip_filepath = f"{mosspath}/{file}"
        # if there are more than 0 attachments, the code will continue
        # if it's not, the bot will yell at the user
        while not len(file.attachments) > 0:
            await interaction.followup.send("I need a populated .zip file.")
            file = await interaction.client.wait_for('message', check=lambda message: message.author == interaction.user)

        await file.attachments[0].save(zip_filepath)

        # here I need to unzip the file in zip_filepath
        with ZipFile(zip_filepath, 'r') as code_zip:
            code_zip.extractall(path=zip_filepath)

        # remove the zip
        os.remove(code_zip)

        # rename the run
        run_name = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        os.rename()



