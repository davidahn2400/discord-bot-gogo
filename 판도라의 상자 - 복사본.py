import discord #discord 불러오기
from discord.ext import commands  #dicord.ext에서 commands 불러오기
from youtube_dl import YoutubeDL #youtube_dl에서 YoutubeDL 불러오기
import bs4 #bs4 불러오기
from selenium import webdriver #selenium에서 webdriver 불러오기
from selenium.webdriver.chrome.options import Options #selenium.webdriver.chrome.options에서 Options 불러오기
from discord.utils import get #discord.utils에서 get 불러오기
from discord import FFmpegPCMAudio #discord에서 FFmpegPCMAudio 불러오기
import asyncio #asyncio 불러오기
import youtube_dl #youtube_dl 불러오기

intent = discord.Intents.default() #discord.Intents.default() 포함시키기
intent.message_content = True #포함시킨 컨텐츠가 사실일 경우에
bot = commands.Bot(command_prefix="!", intents = intent) #봇을 시작하는 명령어를 '!'로 지정

@bot.event
async def on_ready(): #비동기함수 async로 on_ready 상태 정의
    print("We have logged in as {0.user}".format(bot))

@bot.command()
async def play(ctx, url): #비동기함수 async로 play 상태와 ctx, url 변수 지정 후 정의
    channel = ctx.author.voice.channel #channel 지정
    if bot.voice_clients == []: #if문 지정
        await channel.connect() #비동기함수가 원치않는 결과에 접근하는것을 방지하고자 awiat 지정
    await ctx.send("connected to the voice channel, " + str(bot.voice_clients[0].channel)) #voice 채널에 사람이 입장한게 사실일 때 텍스트 보냄

    ydl_opts = {'format': 'bestaudio'} #ydl_opts format 을 사용했는데 이게 뭔지는 아직도 모르겠음
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'} #ffmpeg 옵션 상세 설정
    with youtube_dl.YoutubeDL(ydl_opts) as ydl: #youtube_dl과 연동
        info = ydl.extract_info(url, download=False)#??
        URL = info['formats'][0]['url']#??
    voice = bot.voice_clients[0] #채널안에 사람이 입장해있을 때
    voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS)) #입력한 URL 링크를 설정된 ffmpeg 옵션대로 재생

@bot.command()
async def leave(ctx): #비동기함수 async로 leave 상태와 ctx 변수 지정 후 정의
    await bot.voice_clients[0].disconnect() #채널안에 사람이 없을 경우 disconnect 설정



bot.run('아잇! 어! 푸르르!')