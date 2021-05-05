import discord
import re
import random

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'ODM4MDYzNDA3MjQzNTkxNjgx.YI1pXg.I-LC49DBHDkhB8zycTnt3vU-e_4'

# 接続に必要なオブジェクトを生成
client = discord.Client()import discord
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
    # メッセージ送信者がBotだった 場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if reply == '/neko':
        await message.channel.send("にゃーん")
    #ダイスロール
    
    data = []
    moji = "("
    shounari = reply.find("<")
    dainari = reply.find(">")
    iko = reply.find("=")
    flag = False


    dicea = re.findall("\d+d\d+", reply)

    if re.match("/(\d+d\d+\+)*\d+d\d+ [<,=,>] \d+", reply) or re.match("/(\d+d\d+\+)*\d+d\d+ <= \d+", reply) or re.match("/(\d+d\d+\+)*\d+d\d+ >= \d+", reply):
        hanntei = ""
        flag = True
        if len(dicea) <= 10:
            for ndn in dicea:#複数の振り方に対応
                dicem = re.search("\d+", ndn)
                dicei = int(dicem.group())
                ataim = re.search("d\d+", ndn)
                ataii = int(ataim.group()[1:])
                if dicei < 300:
                    for first in range(dicei):
                        data.append(random.randrange(1,ataii+1,1))
        print(sum(data))
        if shounari > 0:
            if iko > 0:
                if sum(data) <= int(re.search("<= \d+", reply).group()[3:]):
                    print("成功")
                else:
                    print("失敗")
            else:
                if sum(data) < int(re.search("< \d+", reply).group()[2:]):
                    print("成功")
                else:
                    print("失敗")
        elif dainari > 0:
            if iko > 0:
                if sum(data) >= int(re.search(">= \d+", reply).group()[3:]):
                    print("成功")
                else:
                    print("失敗")
            else:
                if sum(data) > int(re.search("> \d+", reply).group()[2:]):
                    print("成功")
                else:
                    print("失敗")
        else:
            if sum(data) == int(re.search("= \d+", reply).group()[2:]):
                print("成功")
            else:
                print("失敗")
    else:
        if re.match("/(\d+d\d+\+)*\d+d\d+", reply):
            flag = True
            if len(dicea) <= 10:
                for ndn in dicea:#複数の振り方に対応
                    dicem = re.search("\d+", ndn)
                    dicei = int(dicem.group())
                    ataim = re.search("d\d+", ndn)
                    ataii = int(ataim.group()[1:])
                    if dicei < 300:
                        for first in range(dicei):
                            data.append(random.randrange(1,ataii+1,1))

        for i in range(len(data)):
            if i != len(data)-1:
                moji += str(data[i]) + " + "
            else:
                moji += str(data[i])
        moji += ")"
    await message.channel.send(str(sum(data))+ " " +moji)
        
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)

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
    if re.match("/(\d+d\d+\+)*\d+d\d+", reply):
        if len(dicea) <= 10:
            for ndn in dicea:#複数の振り方に対応
                dicem = re.search("\d+", ndn)
                dicei = int(dicem.group())
                ataim = re.search("d\d+", ndn)
                ataii = int(ataim.group()[1:])
                if dicei < 300:
                    for first in range(dicei):
                        data.append(random.randrange(1,ataii+1,1))

    for i in range(len(data)):
        if i != len(data)-1:
            moji += str(data[i]) + " + "
        else:
            moji += str(data[i])
    moji += ")"
    await message.channel.send(str(sum(data))+ " " +moji)
        
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
