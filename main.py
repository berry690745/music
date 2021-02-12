import discord, youtube_dl

client = discord.Client(intent=discord.Intents.default())

@client.event
async def on_ready():
    print(f"{client.user.name} has been was a login")

@client.event
async def on_message(message):
    if message.content.startswith("/입장"):
        await message.author.voice.channel.connect()

    if message.content.startswith("/퇴장"):
        for vc in client.voice_clients:
            if vc.guild == message.guild:
                voice = vc

        await voice.disconnect()

    if message.content.startswith("/재생"):
        for vc in client.voice_clients:
            if vc.guild == message.guild:
                voice = vc

        url = message.content.split(" ")[1]

        option = {
            'outtmpl' : "file/" + url.split('=')[1] + ".mp3"
        }

        with youtube_dl.YoutubeDL(option) as ytdl:
            ytdl.download([url])
            info = ytdl.extract_info(url, download=False)

            title = info["title"]

        voice.play(discord.FFmpegPCMAudio("file/" + url.split('=')[1] + ".mp3"))
        await message.channel.send(f"{title}을 재생합니다.")

client.run("")