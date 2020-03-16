import requests
from colorama import Fore, Back, Style
from dhooks import Webhook, Embed
session = requests.Session()


headers = {
    'Connection': 'keep-alive',
    'Accept': '*/*',
    'Sec-Fetch-Dest': 'empty',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.nba.com',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://www.nba.com/nets/community/2019-20/allstarawards',
    'Accept-Language': 'en-US,en;q=0.9,ja;q=0.8',
}

data = {
  'candiatename': 'ANDY'
}

entries = "10"

response = requests.post('https://brooklynse.net/bkn/community/2019-20/all-star-awards/processvote.php', headers=headers, data=data)
print(Fore.LIGHTMAGENTA_EX + str(response.status_code))
response2 = requests.post('https://brooklynse.net/bkn/community/2019-20/all-star-awards/processvote.php', headers=headers, data=data)
print(Fore.LIGHTMAGENTA_EX + str(response2.status_code))
response3 = requests.post('https://brooklynse.net/bkn/community/2019-20/all-star-awards/processvote.php', headers=headers, data=data)
print(Fore.LIGHTMAGENTA_EX + str(response3.status_code))
response4 = requests.post('https://brooklynse.net/bkn/community/2019-20/all-star-awards/processvote.php', headers=headers, data=data)
print(Fore.LIGHTMAGENTA_EX + str(response4.status_code))
response5 = requests.post('https://brooklynse.net/bkn/community/2019-20/all-star-awards/processvote.php', headers=headers, data=data)
print(Fore.LIGHTMAGENTA_EX + str(response5.status_code))
response6 = requests.post('https://brooklynse.net/bkn/community/2019-20/all-star-awards/processvote.php', headers=headers, data=data)
print(Fore.LIGHTMAGENTA_EX + str(response6.status_code))
response7 = requests.post('https://brooklynse.net/bkn/community/2019-20/all-star-awards/processvote.php', headers=headers, data=data)
print(Fore.LIGHTMAGENTA_EX + str(response7.status_code))
response8 = requests.post('https://brooklynse.net/bkn/community/2019-20/all-star-awards/processvote.php', headers=headers, data=data)
print(Fore.LIGHTMAGENTA_EX + str(response8.status_code))
response9 = requests.post('https://brooklynse.net/bkn/community/2019-20/all-star-awards/processvote.php', headers=headers, data=data)
print(Fore.LIGHTMAGENTA_EX + str(response9.status_code))
response10 = requests.post('https://brooklynse.net/bkn/community/2019-20/all-star-awards/processvote.php', headers=headers, data=data)
print(Fore.LIGHTMAGENTA_EX + str(response10.status_code))


if response.status_code and response2.status_code and response3.status_code and response4.status_code and response5.status_code and response6.status_code\
        and response7.status_code and response8.status_code and response9.status_code and response10.status_code == 200:
    hook = Webhook('https://discordapp.com/api/webhooks/654913715598000128/vDiFh7YVOqI_sKihPqou_tXa65oWoe6P7kf8zM7x0IrYZSWT_u7R7va9jOM1fGgiESD6')

    embed = Embed(
    description='NBA All-Star Fan Bot :star:',
    color=0x56CDF9,
    timestamp='now'  # sets the timestamp to current time
    )

    embed.set_author(name='Succesful-Entry', url="https://www.nba.com/nets/community/2019-20/allstarawards")
    embed.add_field(name='Candidate', value="Andy", inline=False)
    embed.add_field(name='Entries', value=entries, inline=False)
    embed.set_footer(text='Made by @AioLoop')
    hook.send(embed=embed)
