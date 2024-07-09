import discord
import random

from discord.ext import commands

from util import getTOKEN
from util import getChannelID
from util import getMenuList

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)


# 특정 채널 ID 설정 (이 ID를 사용하고자 하는 채널의 ID로 변경해야 합니다)
ALLOWED_CHANNEL_ID =  getChannelID() # 여기에 허용할 채널의 ID를 넣으세요
TOKEN = getTOKEN()

# 봇이 준비되었을 때 호출되는 함수
@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'Logged in as {bot.user}!')

# 메뉴추천 명령어 정의
@bot.tree.command(name="메뉴추천", description="추천 메뉴를 제공합니다.")
async def menu_recommendation(interaction: discord.Interaction):
    # 명령어가 사용된 채널이 허용된 채널인지 확인
    if interaction.channel.id != ALLOWED_CHANNEL_ID:
        await interaction.response.send_message("이 채널에서는 이 명령어를 사용할 수 없습니다.", ephemeral=True)
        return

    recommended_menu = random.choice(menu_list)
    await interaction.response.send_message(f"추천 메뉴는 {recommended_menu}입니다.")

# 봇 토큰으로 클라이언트를 실행합니다
menu_list = getMenuList()

bot.run(TOKEN)
