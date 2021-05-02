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
    dicem = re.search("\d+", reply)
    dicei = int(dicem.group())
    ataim = re.search("d\d+", reply)
    ataii = int(ataim.group()[1:])
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if reply == '/neko':
        await message.channel.send("にゃーん")
    #ダイスロール
    if dicei <= 1000:
        if re.match("/[0-9]+d[0-9]+", reply):
            data = []
            moji = "("
            for i in range(dicei):
                data.append(random.randrange(1,ataii+1,1))
                if i < dicei-1:
                    moji += str(data[i]) + " + "
                else:
                    moji += str(data[i])
            moji += ")"
            await message.channel.send(str(sum(data))+ " " +moji)
    else:
        return

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
