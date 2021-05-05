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
    dicea = re.findall("\d+d\d+", reply)
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if reply == '/neko':
        await message.channel.send("にゃーん")
    #ダイスロール
    
    data = []
    moji = "("
    if len(dicea) <= 10:
        for i in dicea: #複数の振り方に対応
            dicem = re.search("\d+", i)
            dicei = int(dicem.group())
            ataim = re.search("d\d+", i)
            ataii = int(ataim.group()[1:])
            if dicei < 300:
                if re.match("/(\d+d\d+\+)*\d+d\d+", reply):

                    for i in range(dicei):
                        data.append(random.randrange(1,ataii+1,1))
                        if i < dicei-1:
                            moji += str(data[i]) + " + "
                        else:
                            moji += str(data[i])
            else:
                return
    moji += ")"
    await message.channel.send(str(sum(data))+ " " +moji)
        
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
