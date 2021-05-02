import discord
import re
import random

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'ODM4MDYzNDA3MjQzNTkxNjgx.YI1pXg.I-LC49DBHDkhB8zycTnt3vU-e_4'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    reply = message.content
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if reply == '/neko':
        await message.channel.send("にゃーん")
    #ダイスロール
    if re.match("/[0-9]d[0-9]+", reply):
        data = []
        moji = "("
        for i in range(int(reply[1])):
            data.append(random.randrange(1,int(reply[3:])+1,1))
            if i < int(reply[1])-1:
                moji += str(data[i]) + " + "
            else:
                moji += str(data[i])
        moji += ")"
        await message.channel.send(str(sum(data))+ " " +moji)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
