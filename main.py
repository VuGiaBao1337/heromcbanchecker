import requests
import json
import math
import time
from discord_webhook import DiscordWebhook, DiscordEmbed
from bs4 import BeautifulSoup

heromc1 = ""
botstatus = ""

DiscordWebhook(url=f'{botstatus}', embeds=[DiscordEmbed(title='Bot By Gia Bao', color=0xFF0000)]).execute()

time.sleep(2)

DiscordWebhook(url=f'{botstatus}', embeds=[DiscordEmbed(title='Bot Started', color=0xFF0000)]).execute()

time.sleep(1)

DiscordWebhook(url=f'{botstatus}', embeds=[DiscordEmbed(title='Connecting HeroMC.Net', color=0xFF0000)]).execute()

time.sleep(4)

DiscordWebhook(url=f'{botstatus}', embeds=[DiscordEmbed(title='Connected HeroMC.Net', color=0xFF0000)]).execute()

while True:
    with open("data.json") as conf:
        data = json.load(conf)
        heromcbanid = data["heromcbanid"]
        heromcbanidfix = data["heromcbanidfix"]
    heromcbanidfix1 = int(heromcbanidfix)
    heromcbanid1 = int(heromcbanid)

    heromcurl = f'https://id.heromc.net/vi-pham/info.php?type=ban&id={heromcbanid}'
    heromcurlfix = f'https://id.heromc.net/vi-pham/info.php?type=ban&id={heromcbanidfix}'

    try:
        response = requests.get(heromcurl)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            td_tags = soup.find_all('td')
            response1 = requests.get(heromcurlfix)
            if f'#{heromcbanidfix}' in response1.text:
                data['heromcbanid'] = heromcbanidfix1
                data['heromcbanidfix'] = heromcbanidfix1 + 2
                with open('data.json', 'w') as f:
                    json.dump(data, f)
            else:
                for td in td_tags:
                    if td.text == 'Người chơi':
                        user = td.find_next_sibling('td').text.strip()

                for td in td_tags:
                    if td.text == 'Bị phạt bởi':
                        staff = td.find_next_sibling('td').text.strip()

                if "Lỗi: ban không tìm thấy trong cơ sở dữ liệu." in soup.get_text():
                    a = 0
                else:
                    if "Console" in soup.get_text():
                        print("Heromc: Banned By Console")
                        data['heromcbanid'] = heromcbanid1 + 1
                        data['heromcbanidfix'] = heromcbanidfix1 + 1
                        with open('data.json', 'w') as f:
                            json.dump(data, f)
                        heromcserver1 = DiscordWebhook(url=f'{heromc1}', embeds=[DiscordEmbed(title='HeroMC.net', description=f':robot: **AntiCheat banned `{user}` - Banned By `{staff}` - Ban `#{heromcbanid}`!** (<t:{math.floor(time.time())}:R>)', color=0xFFCD00)])
                        heromcserver1.execute()
                    else:
                        print("Heromc: Banned By Staff")
                        data['heromcbanid'] = heromcbanid1 + 1
                        data['heromcbanidfix'] = heromcbanidfix1 + 1
                        with open('data.json', 'w') as f:
                            json.dump(data, f)
                        heromcserver1 = DiscordWebhook(url=f'{heromc1}', embeds=[DiscordEmbed(title='HeroMC.net', description=f':hot_face: **Staff banned `{user}` - Banned By `{staff}` - Ban `#{heromcbanid}`!** (<t:{math.floor(time.time())}:R>)', color=0xFF0000)])
                        heromcserver1.execute()

        
        else:
            print(f'Heromc: Error: {response.status_code}')
            DiscordWebhook(url=f'{botstatus}', embeds=[DiscordEmbed(title=f'Heromc: Error: {response.status_code}', color=0xFF0000)]).execute()

    except requests.exceptions.RequestException as e:
        print('Heromc: Cannot Connect:', e)      
        DiscordWebhook(url=f'{botstatus}', embeds=[DiscordEmbed(title=f'Heromc: Cannot Connect!', color=0xFF0000)]).execute()

######################################################################################################################################

 
