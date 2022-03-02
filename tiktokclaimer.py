import os
from time import sleep


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


try:
    import requests
except:
    print('Please Wait .')
    sleep(1.6)
    clear()
    os.system('pip install requests')
    clear()
    import requests

try:
    import subprocess

    hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
    # print(hwid)
    req = requests.get('https://pastebin.com/AaAa10101').text
    if hwid not in req:
        print('Contact >>> IG @Ajarmah - @_vt.done <<< For Activation ..')
        print('Take A photo Of This And Send It To him :')
        print(hwid)
        with open("AcCode.txt", "a") as xxcc:
            xxcc.write(
                f' Activation Code : {hwid}\n\nSend This To Me To Activate\nInstagram : @Ajarmah - @_vt.done\n\n\n')
        print(f'\nDone Saved Your Activation Code in "AcCode.txt"\n')
        input('Press Enter To Exit')
        exit()
    if hwid in req:
        clear()
        pass
except ModuleNotFoundError:
    print('Please Wait .')
    sleep(1.6)
    clear()
    os.system('pip install subprocess')
    clear()
    import subprocess


try:
    from discord_webhook import DiscordEmbed
    from discord_webhook import DiscordWebhook

except ModuleNotFoundError:
    print('Please Wait .')
    sleep(1.6)
    clear()
    os.system('pip install discord_webhook')
    clear()
    from discord_webhook import DiscordEmbed
    from discord_webhook import DiscordWebhook

try:
    import colorama
except ModuleNotFoundError:
    print('Please Wait .')
    sleep(1.6)
    clear()
    os.system('pip install colorama')
    clear()
    import colorama

try:
    import json
except ModuleNotFoundError:
    print('Please Wait .')
    sleep(1.6)
    clear()
    os.system('pip install json')
    clear()
    import json

try:
    import ctypes
except ModuleNotFoundError:
    print('Please Wait .')
    sleep(1.6)
    clear()
    os.system('pip install ctypes')
    clear()
    import ctypes

try:
    import random
except ModuleNotFoundError:
    print('Please Wait .')
    sleep(1.6)
    clear()
    os.system('pip install random')
    clear()
    import random

try:
    import threading
except ModuleNotFoundError:
    print('Please Wait .')
    sleep(1.6)
    clear()
    os.system('pip install threading')
    clear()
    import threading
try:
    from colorama import Fore
except ModuleNotFoundError:
    print('Please Wait .')
    sleep(1.6)
    clear()
    os.system('pip install colorama')
    clear()
    from colorama import Fore

sss = ctypes.windll.kernel32.SetConsoleTitleW
cmb = ctypes.windll.user32.MessageBoxW
colorama.init(autoreset=True)

sss('Logging In ...')
sleep(2)
sss('Logged ...')
sleep(2)
GREEN = Fore.GREEN
RED = Fore.RED
RESET = Fore.RESET
sss('Tiktok Claimer by @Ajarmah')
sleep(2.5)
Lsessions = []
Lusers = []
Lproxies = []
cuser = []
csess = []
threads = []

prox_type = ['http', 'https', 'socks4']

att, reqs, err = 0, 0, 0

try:
    sett_open = open('settings.txt').read()
except FileNotFoundError:
    print('Please Put Settings File In The Same Folder !')
    input('')
    exit(0)


try :
    sett_file = json.loads(sett_open)
    thr = int(sett_file[0]["Please_Write_The_Informations"]["Threads"])
    sessi_list = sett_file[0]["Please_Write_The_Informations"]["Sessions_List"]
    proxy_list = sett_file[0]["Please_Write_The_Informations"]["Proxies_List"]
    proxy_type = sett_file[0]["Please_Write_The_Informations"]["Proxy_Type"]

    name = sett_file[1]["You_Can_Leave_Them_Empty"]["Your_Name"]
    Dis_Webhook = sett_file[1]["You_Can_Leave_Them_Empty"]["Your_Discord_WebHook"]
    Cus_Bio = sett_file[1]["You_Can_Leave_Them_Empty"]["Bio"]
except:
    cmb(None, f'Error In Settings File ! ', '@Ajarmah TikTok Claimer')
    csess.append('NOSESSLEFT')
    input('')
    exit(0)

try:
    sess_file = open(sessi_list).read().splitlines()
    for session in sess_file:
        Lsessions.append(session)
    if len(Lsessions) == 0:
        print(f'Sessions File Is Empty ! > {sessi_list}')
        input('')
        exit(0)
except FileNotFoundError:
    print('Please Write Sessions File Name Correct In Settings File')
    input('')
    exit(0)


if Dis_Webhook == '':
    Dis_Webhook = 'https://discord.com/api/webhooks/'

if Cus_Bio == '':
    Cus_Bio = 'Claimed by IG - @Ajarmah'

if name == '':
    name = 'Sir'
else:
    name = name


if proxy_list == '':
    print('Please Put Proxy File Name In Settings File ')
    input('')
    exit(0)


elif not proxy_type in prox_type:
    print('Please Write Proxy type Name Correct In Settings File')
    input('')
    exit(0)

print(f'{RED}[{RESET}1{RED}] List\n{RED}[{RESET}2{RED}] Target\n')
mode = int(input('<?> Mode : '))
clear()

if mode==1:
    try:
        users_list = sett_file[0]["Please_Write_The_Informations"]["Users_List"]
    except:
        cmb(None, f'Error In Settings File ! ', '@Ajarmah TikTok Claimer')
        csess.append('NOSESSLEFT')
        input('')
        exit(0)
    print(f"Hi {GREEN}{name}{RESET}... {RED}\nIf The Claimer Does't Run After 10-20 Second,\nCheck Your Settings File , or Check Your Proxies Type .{RESET}")
    sleep(2.5)
    clear()

    try:
        users_file = open(users_list).read().splitlines()
        for user in users_file:
            if user.isdigit() == False:
                Lusers.append(user)
        if len(Lusers) == 0:
            print(f'Users File Is Empty ! > {users_list}')
            input('')
            exit(0)
    except FileNotFoundError:
        print('Please Write Users File Name Correct In Settings File')
        input('')
        exit(0)

    if 'http' in proxy_type or proxy_type == 'https':
        try:
            proxy_file = open(proxy_list).read().splitlines()
            for prox in proxy_file:
                Lproxies.append(prox)
            if len(Lproxies) == 0:
                print(f'Proxies File Is Empty ! > {proxy_list}')
                input('')
                exit(0)
            elif len(Lproxies) >= 1:
                # print(f'{GREEN}[{RESET}+{GREEN}] Successfully Loaded :\n\t{GREEN}[{RESET}{len(Lusers)}{GREEN}] List Count\n\t{GREEN}[{RESET}{len(Lproxies)}{GREEN}] Proxies Count\n\t{GREEN}[{RESET}{len(Lsessions)}{GREEN}] Sessions Count')
                # input('')
                def Claim_ls():
                    global att, reqs, err
                    while True:
                        runn = str(random.choice(Lproxies))
                        ruser = random.choice(Lusers)
                        DWH = DiscordWebhook(
                            url='https://discord.com/api/webhooks/')
                        DWH2 = DiscordWebhook(url=Dis_Webhook)
                        EMK = DiscordEmbed(title=f"Claimed > @{ruser}\n""Requests > {:,}".format(att),
                                           description='Coded by @Ajarmah\n\n@Ajarmah - @_vt.done',
                                           color=14681863)
                        EMK.set_thumbnail(url='https://imgur.com/m6lYzYC.gif')
                        DWH.add_embed(EMK)
                        DWH2.add_embed(EMK)
                        try:
                            rsession = random.choice(Lsessions)
                        except IndexError:
                            if 'NOSESSLEFT' not in csess:
                                if len(Lsessions) == 0:
                                    if 'NOSESSLEFT' not in csess:
                                        cmb(None, f'No Sessions Left Habebi ;-/', '@Ajarmah TikTok Claimer')
                                        csess.append('NOSESSLEFT')
                        try:
                            PROXYY = {
                                'http': 'http://{}'.format(runn),
                                'https': 'https://{}'.format(runn),
                                'http': '{}'.format(runn),
                                'https': '{}'.format(runn)
                            }
                            url = f'https://www.tiktok.com/@{ruser}'
                            url1 = 'https://api16-normal-c-alisg.tiktokv.com/passport/login_name/update/?iid=7060509952591595266&device_id=7054537563859764742&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=230005&version_name=23.0.5&device_platform=android&ab_version=23.0.5&ssmix=a&device_type=SM-N975F&device_brand=samsung&language=en&os_api=25&os_version=7.1.2&openudid=a0fa5ae7590c6576&manifest_version_code=2022300050&resolution=1600*900&dpi=300&update_version_code=2022300050&_rticket=1644335649391&current_region=JO&app_type=normal&sys_region=US&mcc_mnc=41601&timezone_name=America%2FChicago&residence=JO&ts=1644335648&timezone_offset=-21600&build_number=23.0.5&region=US&uoo=0&app_language=en&carrier_region=JO&locale=en&op_region=JO&ac2=wifi&host_abi=x86&cdid=63d7e01e-5508-4742-ad36-df84088dcef8&support_webview=1&okhttp_version=4.1.73.9-tiktok'
                            url2 = 'https://api16-normal-c-alisg.tiktokv.com/aweme/v1/commit/user/?iid=7053806752974882566&device_id=6994798204819621382&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=220804&version_name=22.8.4&device_platform=android&ab_version=22.8.4&ssmix=a&device_type=SM-N975F&device_brand=samsung&language=en&os_api=25&os_version=7.1.2&openudid=c1d415ad940052b3&manifest_version_code=2022208040&resolution=720*1280&dpi=240&update_version_code=2022208040&_rticket=1642346163746&current_region=JO&app_type=normal&sys_region=US&mcc_mnc=41603&timezone_name=Asia%2FShanghai&residence=JO&ts=1642346163&timezone_offset=28800&build_number=22.8.4&region=US&uoo=1&app_language=en&carrier_region=JO&locale=en&op_region=JO&ac2=wifi&host_abi=x86&cdid=b2d439e0-8d34-45ee-b889-3f94c2882af2'

                            headers = {
                                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76'
                            }

                            headers1 = {
                                'accept-encoding': 'gzip',
                                'connection': 'Keep-Alive',
                                'content-length': '61',
                                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                'cookie': f'store-idc=alisg; store-country-code=jo; passport_csrf_token=4f090f6c688d34439023d87c94284d56; passport_csrf_token_default=4f090f6c688d34439023d87c94284d56; d_ticket=1a360b478360784d60e9c19bab2975d299648; multi_sids=7053658438690620417%3A{rsession}; cmpl_token=AgQQAPOlF-RPsLHdTl3tJZ04-3Ma2-5Pf4QuYMIzrw; odin_tt=d62f0efc196a8d93560631a047a87752c12f5ddfe33609a464231b966571be6fb2ff3fe1ba12167eceb59eb2dd3132d2bfec5cbae962019f47d62fa73b1768bed92d4c701d38b567cbf2bb9573a96c20; sid_guard={rsession}%7C1642342749%7C5183999%7CThu%2C+17-Mar-2022+14%3A19%3A08+GMT; uid_tt=ce5c1917610acacc9ac99631c4e012316730e233d63a978a93413f7a09985b49; uid_tt_ss=ce5c1917610acacc9ac99631c4e012316730e233d63a978a93413f7a09985b49; sid_tt={rsession}; ; sessionid_ss={rsession}',
                                'passport-sdk-version': '19',
                                'x-gorgon': '040400d140002934b0b8bc7150ef56d1363224801d3c99ce90c3',
                                'user-agent': 'com.zhiliaoapp.musically/2022208040 (Linux; U; Android 7.1.2; en; SM-N975F; Build/N2G48H;tt-ok/3.10.0.2)'
                            }
                            data_signature = f'signature={Cus_Bio}'
                            data_nickname = f"nickname={name}"
                            data_username = f'login_name={ruser}&page_from=0'
                            req = requests.get(url, headers=headers, proxies=PROXYY).text.split('"preloadList":[]}}')[1].split('"I18n"')[0]
                            att += 1
                            if '{"followerCount":' in req or req==',"UserPage":{"statusCode":10221},' or req==',"UserPage":{"statusCode":10223},' or req==',"UserPage":{"statusCode":10225},' or req==',"UserPage":{"statusCode":10101},':
                                reqs += 1
                            elif req == ',"UserPage":{"statusCode":10202},':
                                try:
                                    req1 = requests.post(url1, headers=headers1, data=data_username, proxies=PROXYY).text
                                    # print(req1)
                                    if ruser not in cuser:
                                        if f'"message":"success"' in req1 or req1 == f'"Login_name":"{ruser}"':
                                            print(
                                                f'\r{GREEN}[{RESET}{ruser}{GREEN}] Done Claimed ;)\n{GREEN}[{RESET}{rsession}{GREEN}] SessionID\n\n',
                                                end='')
                                            requests.post(url2, headers=headers1, data=data_signature).text
                                            requests.post(url2, headers=headers1, data=data_nickname).text
                                            DWH.execute()
                                            DWH2.execute()
                                            with open(f'@{ruser} Info.txt', 'a') as xx:
                                                xx.write(f'Username : {ruser}\nSessionID : {rsession}')
                                            Lsessions.remove(rsession)
                                            cuser.append(ruser)
                                            cmb(None,
                                                f'New Claim > {ruser}  \nAttemps : {"{:,}".format(att)}',
                                                '@Ajarmah TikTok Claimer')

                                    if '"description":"login name can only be updated once within one month."' in req1:
                                        if rsession not in cuser:
                                            print(f'\r{RED}This Session Has 1 month Limit >>> SID : {rsession}\n{ruser}{RESET}\n',end='')
                                            Lsessions.remove(rsession)
                                            cuser.append(rsession)
                                        if len(Lsessions) >= 1:
                                            req = requests.post(url1, headers=headers1, data=data_username, proxies=PROXYY).text
                                            if ruser not in cuser:
                                                if f'"message":"success"' in req or req==f'"Login_name":"{ruser}"':
                                                    print(
                                                        f'\r{GREEN}[{RESET}{ruser}{GREEN}] Done Claimed ;)\n{GREEN}[{RESET}{rsession}{GREEN}] SessionID\n\n',
                                                        end='')
                                                    requests.post(url2, headers=headers1, data=data_signature).text
                                                    requests.post(url2, headers=headers1, data=data_nickname).text
                                                    DWH.execute()
                                                    DWH2.execute()
                                                    with open(f'@{ruser} Info.txt', 'a') as xx:
                                                        xx.write(f'Username : {ruser}\nSessionID : {rsession}')
                                                    Lsessions.remove(rsession)
                                                    cuser.append(ruser)
                                                    cmb(None,
                                                        f'New Claim > {ruser}  \nAttemps : {"{:,}".format(att)}',
                                                        '@Ajarmah TikTok Claimer')


                                    if '"description":"The conversation has expired, please log in again"' in req1:
                                        if rsession not in cuser:
                                            cmb(None, f'This SessionID Has Expired !  \nSid : {rsession}',
                                                '@Ajarmah TikTok Claimer')
                                            Lsessions.remove(rsession)
                                            cuser.append(rsession)

                                    if '"description":"Too many attempts. Try again later."' in req1:
                                        pass

                                except:
                                    pass
                            else:
                                err += 1
                            before = att
                            sleep(1)
                            RS = att - before
                            sss(f'Ok : {"{:,}".format(reqs)}  |  Bad - ErrorProxy : {"{:,}".format(err)}  |  R\S : {"{:,}".format(RS)}  |  SIDs : {len(Lsessions)}')

                        except requests.exceptions.ConnectionError:
                            err +=1
                        except requests.exceptions.ReadTimeout:
                            err +=1
                        except requests.exceptions.ChunkedEncodingError:
                            err +=1
                        except IndexError:
                            pass


                for i in range(thr):
                    thread1 = threading.Thread(target=Claim_ls)
                    thread1.daemon = True
                    thread1.start()
                    threads.append(thread1)
                for thread2 in threads:
                    thread2.join()
        except FileNotFoundError:
            print('Please Write Proxy File Name Correct In Settings File')
            input('')
            exit(0)
    elif proxy_type == 'socks4':
        clear()
        os.system('pip install pysocks')
        clear()
        try:
            proxy_file = open(proxy_list).read().splitlines()
            for prox in proxy_file:
                Lproxies.append(prox)
            if len(Lproxies) == 0:
                print(f'Proxies File Is Empty ! > {proxy_list}')
                input('')
                exit(0)
            elif len(Lproxies) >= 1:
                def Claim_ls():
                    global att, reqs, err
                    while True:
                        runn = str(random.choice(Lproxies))
                        ruser = random.choice(Lusers)
                        DWH = DiscordWebhook(url='https://discord.com/api/webhooks/')
                        DWH2 = DiscordWebhook(url=Dis_Webhook)
                        EMK = DiscordEmbed(title=f"Claimed > @{ruser}\n""Requests > {:,}".format(att),
                                           description='Coded by @Ajarmah\n\n@Ajarmah - @_vt.done',
                                           color=14681863)
                        EMK.set_thumbnail(url='https://imgur.com/m6lYzYC.gif')
                        DWH.add_embed(EMK)
                        DWH2.add_embed(EMK)
                        try:
                            rsession = random.choice(Lsessions)
                        except IndexError:
                            if 'NOSESSLEFT' not in csess:
                                if len(Lsessions) == 0:
                                    if 'NOSESSLEFT' not in csess:
                                        cmb(None, f'No Sessions Left Habebi ;-/', '@Ajarmah TikTok Claimer')
                                        csess.append('NOSESSLEFT')
                        try:
                            PROXYY = {
                                'http': 'socks4://{}'.format(runn),
                                'https': 'socks4://{}'.format(runn)
                            }
                            url = f'https://www.tiktok.com/@{ruser}'
                            url1 = 'https://api16-normal-c-alisg.tiktokv.com/passport/login_name/update/?iid=7060509952591595266&device_id=7054537563859764742&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=230005&version_name=23.0.5&device_platform=android&ab_version=23.0.5&ssmix=a&device_type=SM-N975F&device_brand=samsung&language=en&os_api=25&os_version=7.1.2&openudid=a0fa5ae7590c6576&manifest_version_code=2022300050&resolution=1600*900&dpi=300&update_version_code=2022300050&_rticket=1644335649391&current_region=JO&app_type=normal&sys_region=US&mcc_mnc=41601&timezone_name=America%2FChicago&residence=JO&ts=1644335648&timezone_offset=-21600&build_number=23.0.5&region=US&uoo=0&app_language=en&carrier_region=JO&locale=en&op_region=JO&ac2=wifi&host_abi=x86&cdid=63d7e01e-5508-4742-ad36-df84088dcef8&support_webview=1&okhttp_version=4.1.73.9-tiktok'
                            url2 = 'https://api16-normal-c-alisg.tiktokv.com/aweme/v1/commit/user/?iid=7053806752974882566&device_id=6994798204819621382&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=220804&version_name=22.8.4&device_platform=android&ab_version=22.8.4&ssmix=a&device_type=SM-N975F&device_brand=samsung&language=en&os_api=25&os_version=7.1.2&openudid=c1d415ad940052b3&manifest_version_code=2022208040&resolution=720*1280&dpi=240&update_version_code=2022208040&_rticket=1642346163746&current_region=JO&app_type=normal&sys_region=US&mcc_mnc=41603&timezone_name=Asia%2FShanghai&residence=JO&ts=1642346163&timezone_offset=28800&build_number=22.8.4&region=US&uoo=1&app_language=en&carrier_region=JO&locale=en&op_region=JO&ac2=wifi&host_abi=x86&cdid=b2d439e0-8d34-45ee-b889-3f94c2882af2'

                            headers = {
                                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76'
                            }

                            headers1 = {
                                'accept-encoding': 'gzip',
                                'connection': 'Keep-Alive',
                                'content-length': '61',
                                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                'cookie': f'store-idc=alisg; store-country-code=jo; passport_csrf_token=4f090f6c688d34439023d87c94284d56; passport_csrf_token_default=4f090f6c688d34439023d87c94284d56; d_ticket=1a360b478360784d60e9c19bab2975d299648; multi_sids=7053658438690620417%3A{rsession}; cmpl_token=AgQQAPOlF-RPsLHdTl3tJZ04-3Ma2-5Pf4QuYMIzrw; odin_tt=d62f0efc196a8d93560631a047a87752c12f5ddfe33609a464231b966571be6fb2ff3fe1ba12167eceb59eb2dd3132d2bfec5cbae962019f47d62fa73b1768bed92d4c701d38b567cbf2bb9573a96c20; sid_guard={rsession}%7C1642342749%7C5183999%7CThu%2C+17-Mar-2022+14%3A19%3A08+GMT; uid_tt=ce5c1917610acacc9ac99631c4e012316730e233d63a978a93413f7a09985b49; uid_tt_ss=ce5c1917610acacc9ac99631c4e012316730e233d63a978a93413f7a09985b49; sid_tt={rsession}; ; sessionid_ss={rsession}',
                                'passport-sdk-version': '19',
                                'x-gorgon': '040400d140002934b0b8bc7150ef56d1363224801d3c99ce90c3',
                                'user-agent': 'com.zhiliaoapp.musically/2022208040 (Linux; U; Android 7.1.2; en; SM-N975F; Build/N2G48H;tt-ok/3.10.0.2)'
                            }
                            data_signature = f'signature={Cus_Bio}'
                            data_nickname = f"nickname={name}"
                            data_username = f'login_name={ruser}&page_from=0'
                            req = requests.get(url, headers=headers, proxies=PROXYY).text.split('"preloadList":[]}}')[1].split('"I18n"')[0]
                            # print(req)
                            att += 1
                            if '{"followerCount":' in req or req==',"UserPage":{"statusCode":10221},' or req==',"UserPage":{"statusCode":10223},' or req==',"UserPage":{"statusCode":10225},' or req==',"UserPage":{"statusCode":10101},':
                                reqs += 1
                            elif req == ',"UserPage":{"statusCode":10202},':
                                try:
                                    req1 = requests.post(url1, headers=headers1, data=data_username, proxies=PROXYY).text
                                    # print(req1)
                                    if ruser not in cuser:
                                        if f'"message":"success"' in req1 or req1 == f'"Login_name":"{ruser}"':
                                            print(
                                                f'\r{GREEN}[{RESET}{ruser}{GREEN}] Done Claimed ;)\n{GREEN}[{RESET}{rsession}{GREEN}] SessionID\n\n',
                                                end='')
                                            requests.post(url2, headers=headers1, data=data_signature).text
                                            requests.post(url2, headers=headers1, data=data_nickname).text
                                            DWH.execute()
                                            DWH2.execute()
                                            with open(f'@{ruser} Info.txt', 'a') as xx:
                                                xx.write(f'Username : {ruser}\nSessionID : {rsession}')
                                            Lsessions.remove(rsession)
                                            cuser.append(ruser)
                                            cmb(None,
                                                f'New Claim > {ruser}  \nAttemps : {"{:,}".format(att)}',
                                                '@Ajarmah TikTok Claimer')

                                    if '"description":"login name can only be updated once within one month."' in req1:
                                        if rsession not in cuser:
                                            print(
                                                f'\r{RED}This Session Has 1 month Limit >>> SID : {rsession}\n{ruser}{RESET}\n',
                                                end='')
                                            Lsessions.remove(rsession)
                                            cuser.append(rsession)
                                        if len(Lsessions) >= 1:
                                            req = requests.post(url1, headers=headers1, data=data_username,
                                                                proxies=PROXYY).text
                                            if ruser not in cuser:
                                                if f'"message":"success"' in req or req == f'"Login_name":"{ruser}"':
                                                    print(
                                                        f'\r{GREEN}[{RESET}{ruser}{GREEN}] Done Claimed ;)\n{GREEN}[{RESET}{rsession}{GREEN}] SessionID\n\n',
                                                        end='')
                                                    requests.post(url2, headers=headers1, data=data_signature).text
                                                    requests.post(url2, headers=headers1, data=data_nickname).text
                                                    DWH.execute()
                                                    DWH2.execute()
                                                    with open(f'@{ruser} Info.txt', 'a') as xx:
                                                        xx.write(f'Username : {ruser}\nSessionID : {rsession}')
                                                    Lsessions.remove(rsession)
                                                    cuser.append(ruser)
                                                    cmb(None,
                                                        f'New Claim > {ruser}  \nAttemps : {"{:,}".format(att)}',
                                                        '@Ajarmah TikTok Claimer')

                                    if '"description":"The conversation has expired, please log in again"' in req1:
                                        if rsession not in cuser:
                                            cmb(None, f'This SessionID Has Expired !  \nSid : {rsession}',
                                                '@Ajarmah TikTok Claimer')
                                            Lsessions.remove(rsession)
                                            cuser.append(rsession)

                                    if '"description":"Too many attempts. Try again later."' in req1:
                                        pass

                                except:
                                    pass
                            else:
                                err += 1
                            before = att
                            sleep(1)
                            RS = att - before
                            sss(f'Ok : {"{:,}".format(reqs)}  |  Bad - ErrorProxy : {"{:,}".format(err)}  |  R\S : {"{:,}".format(RS)}  |  SIDs : {len(Lsessions)}')

                        except requests.exceptions.ConnectionError:
                            err +=1
                        except requests.exceptions.ReadTimeout:
                            err +=1
                        except requests.exceptions.ChunkedEncodingError:
                            err +=1
                        except IndexError:
                            pass


                for i in range(thr):
                    thread1 = threading.Thread(target=Claim_ls)
                    thread1.daemon = True
                    thread1.start()
                    threads.append(thread1)
                for thread2 in threads:
                    thread2.join()
        except FileNotFoundError:
            print('Please Write Proxy File Name Correct In Settings File')
            input('')
            exit(0)


elif mode==2:
    target = input('<?> Target : ')
    print(
        f"Hi {GREEN}{name}{RESET}... {RED}\nIf The Claimer Does't Run After 10-20 Second,\nCheck Your Settings File , or Check Your Proxies Type .{RESET}")
    sleep(2.5)
    clear()
    if 'http' in proxy_type or proxy_type == 'https':
        try:
            proxy_file = open(proxy_list).read().splitlines()
            for prox in proxy_file:
                Lproxies.append(prox)
            if len(Lproxies) == 0:
                print(f'Proxies File Is Empty ! > {proxy_list}')
                input('')
                exit(0)
            elif len(Lproxies) >= 1:
                # print(f'{GREEN}[{RESET}+{GREEN}] Successfully Loaded :\n\t{GREEN}[{RESET}{len(Lusers)}{GREEN}] List Count\n\t{GREEN}[{RESET}{len(Lproxies)}{GREEN}] Proxies Count\n\t{GREEN}[{RESET}{len(Lsessions)}{GREEN}] Sessions Count')
                # input('')
                def Claim_us():
                    global att, reqs, err
                    while True:
                        runn = str(random.choice(Lproxies))
                        DWH = DiscordWebhook(url='https://discord.com/api/webhooks/')
                        DWH2 = DiscordWebhook(url=Dis_Webhook)
                        EMK = DiscordEmbed(title=f"Catched > @{target}\n""Requests > {:,}".format(att),
                                           description='Coded by @Ajarmah\n\n@Ajarmah - @_vt.done',
                                           color=14681863)
                        EMK.set_thumbnail(url='https://imgur.com/m6lYzYC.gif')
                        DWH.add_embed(EMK)
                        DWH2.add_embed(EMK)
                        try:
                            rsession = random.choice(Lsessions)
                        except IndexError:
                            threading.Lock()
                            pass
                        try:
                            PROXYY = {
                                'http': 'http://{}'.format(runn),
                                'https': 'https://{}'.format(runn),
                                'http': '{}'.format(runn),
                                'https': '{}'.format(runn)
                            }
                            url = f'https://www.tiktok.com/@{target}'
                            url1 = 'https://api16-normal-c-alisg.tiktokv.com/passport/login_name/update/?iid=7060509952591595266&device_id=7054537563859764742&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=230005&version_name=23.0.5&device_platform=android&ab_version=23.0.5&ssmix=a&device_type=SM-N975F&device_brand=samsung&language=en&os_api=25&os_version=7.1.2&openudid=a0fa5ae7590c6576&manifest_version_code=2022300050&resolution=1600*900&dpi=300&update_version_code=2022300050&_rticket=1644335649391&current_region=JO&app_type=normal&sys_region=US&mcc_mnc=41601&timezone_name=America%2FChicago&residence=JO&ts=1644335648&timezone_offset=-21600&build_number=23.0.5&region=US&uoo=0&app_language=en&carrier_region=JO&locale=en&op_region=JO&ac2=wifi&host_abi=x86&cdid=63d7e01e-5508-4742-ad36-df84088dcef8&support_webview=1&okhttp_version=4.1.73.9-tiktok'
                            url2 = 'https://api16-normal-c-alisg.tiktokv.com/aweme/v1/commit/user/?iid=7053806752974882566&device_id=6994798204819621382&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=220804&version_name=22.8.4&device_platform=android&ab_version=22.8.4&ssmix=a&device_type=SM-N975F&device_brand=samsung&language=en&os_api=25&os_version=7.1.2&openudid=c1d415ad940052b3&manifest_version_code=2022208040&resolution=720*1280&dpi=240&update_version_code=2022208040&_rticket=1642346163746&current_region=JO&app_type=normal&sys_region=US&mcc_mnc=41603&timezone_name=Asia%2FShanghai&residence=JO&ts=1642346163&timezone_offset=28800&build_number=22.8.4&region=US&uoo=1&app_language=en&carrier_region=JO&locale=en&op_region=JO&ac2=wifi&host_abi=x86&cdid=b2d439e0-8d34-45ee-b889-3f94c2882af2'

                            headers = {
                                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76'
                            }

                            headers1 = {
                                'accept-encoding': 'gzip',
                                'connection': 'Keep-Alive',
                                'content-length': '61',
                                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                'cookie': f'store-idc=alisg; store-country-code=jo; passport_csrf_token=4f090f6c688d34439023d87c94284d56; passport_csrf_token_default=4f090f6c688d34439023d87c94284d56; d_ticket=1a360b478360784d60e9c19bab2975d299648; multi_sids=7053658438690620417%3A{rsession}; cmpl_token=AgQQAPOlF-RPsLHdTl3tJZ04-3Ma2-5Pf4QuYMIzrw; odin_tt=d62f0efc196a8d93560631a047a87752c12f5ddfe33609a464231b966571be6fb2ff3fe1ba12167eceb59eb2dd3132d2bfec5cbae962019f47d62fa73b1768bed92d4c701d38b567cbf2bb9573a96c20; sid_guard={rsession}%7C1642342749%7C5183999%7CThu%2C+17-Mar-2022+14%3A19%3A08+GMT; uid_tt=ce5c1917610acacc9ac99631c4e012316730e233d63a978a93413f7a09985b49; uid_tt_ss=ce5c1917610acacc9ac99631c4e012316730e233d63a978a93413f7a09985b49; sid_tt={rsession}; ; sessionid_ss={rsession}',
                                'passport-sdk-version': '19',
                                'x-gorgon': '040400d140002934b0b8bc7150ef56d1363224801d3c99ce90c3',
                                'user-agent': 'com.zhiliaoapp.musically/2022208040 (Linux; U; Android 7.1.2; en; SM-N975F; Build/N2G48H;tt-ok/3.10.0.2)'
                            }
                            data_signature = f'signature={Cus_Bio}'
                            data_nickname = f"nickname={name}"
                            data_username = f'login_name={target}&page_from=0'
                            req = \
                            requests.get(url, headers=headers, proxies=PROXYY).text.split('"preloadList":[]}}')[1].split(
                                '"I18n"')[0]
                            # print(req)
                            att += 1
                            if '{"followerCount":' in req or req == ',"UserPage":{"statusCode":10221},' or req == ',"UserPage":{"statusCode":10223},' or req == ',"UserPage":{"statusCode":10225},' or req == ',"UserPage":{"statusCode":10101},':
                                reqs += 1
                            elif req == ',"UserPage":{"statusCode":10202},':
                                try:
                                    req1 = requests.post(url1, headers=headers1, data=data_username,
                                                         proxies=PROXYY).text
                                    print(req1)
                                    # print(req1)
                                    if target not in cuser:
                                        if f'"message":"success"' in req1 or req1 == f'"Login_name":"{target}"':
                                            print(
                                                f'\r{RED}[{RESET}{target}{RED}] Catched ;)\n{RED}[{RESET}{rsession}{RED}] SessionID\n\n',
                                                end='')
                                            requests.post(url2, headers=headers1, data=data_signature).text
                                            requests.post(url2, headers=headers1, data=data_nickname).text
                                            DWH.execute()
                                            DWH2.execute()
                                            with open(f'@{target} Info.txt', 'a') as xx:
                                                xx.write(f'Username : {target}\nSessionID : {rsession}')
                                            Lsessions.remove(rsession)
                                            cuser.append(target)
                                            cmb(None,
                                                f'Catched > {target}  \nAttemps : {"{:,}".format(att)}',
                                                '@Ajarmah TikTok Claimer')

                                    if '"description":"login name can only be updated once within one month."' in req1:
                                        if rsession not in cuser:
                                            print(f'\r{RED}This Session Has 1 month Limit >>> SID : {rsession}{RESET}',
                                                  end='')
                                            Lsessions.remove(rsession)
                                            cuser.append(rsession)

                                    if '"description":"The conversation has expired, please log in again"' in req1:
                                        if rsession not in cuser:
                                            cmb(None, f'This SessionID Has Expired !  \nSid : {rsession}',
                                                '@Ajarmah TikTok Claimer')
                                            Lsessions.remove(rsession)
                                            cuser.append(rsession)

                                    if '"description":"Too many attempts. Try again later."' in req1:
                                        pass

                                except:
                                    pass
                            else:
                                err += 1
                            before = att
                            sleep(1)
                            RS = att - before
                            sss(f'Ok : {"{:,}".format(reqs)}  |  Bad - ErrorProxy : {"{:,}".format(err)}  |  R\S : {"{:,}".format(RS)}  |  SIDs : {len(Lsessions)}')

                        except requests.exceptions.ConnectionError:
                            err +=1
                        except requests.exceptions.ReadTimeout:
                            err +=1
                        except requests.exceptions.ChunkedEncodingError:
                            err +=1
                        except IndexError:
                            pass


                for i in range(thr):
                    thread1 = threading.Thread(target=Claim_us)
                    thread1.daemon = True
                    thread1.start()
                    threads.append(thread1)
                for thread2 in threads:
                    thread2.join()



        except FileNotFoundError:
            print('Please Write Proxy File Name Correct In Settings File')
            input('')
            exit(0)
    elif proxy_type == 'socks4':
        try:
            proxy_file = open(proxy_list).read().splitlines()
            for prox in proxy_file:
                Lproxies.append(prox)
            if len(Lproxies) == 0:
                print(f'Proxies File Is Empty ! > {proxy_list}')
                input('')
                exit(0)
            elif len(Lproxies) >= 1:
                # print(f'{GREEN}[{RESET}+{GREEN}] Successfully Loaded :\n\t{GREEN}[{RESET}{len(Lusers)}{GREEN}] List Count\n\t{GREEN}[{RESET}{len(Lproxies)}{GREEN}] Proxies Count\n\t{GREEN}[{RESET}{len(Lsessions)}{GREEN}] Sessions Count')
                # input('')
                def Claim_us():
                    global att, reqs, err
                    while True:
                        runn = str(random.choice(Lproxies))
                        DWH = DiscordWebhook(url='https://discord.com/api/webhooks/')
                        DWH2 = DiscordWebhook(url=Dis_Webhook)
                        EMK = DiscordEmbed(title=f"Catched > @{target}\n""Requests > {:,}".format(att),
                                           description='Coded by @Ajarmah\n\n@Ajarmah - @_vt.done',
                                           color=14681863)
                        EMK.set_thumbnail(url='https://imgur.com/m6lYzYC.gif')
                        DWH.add_embed(EMK)
                        DWH2.add_embed(EMK)
                        try:
                            rsession = random.choice(Lsessions)
                        except IndexError:
                            threading.Lock()
                            pass
                        try:
                            PROXYY = {
                                'http': 'socks4://{}'.format(runn),
                                'https': 'socks4://{}'.format(runn)
                            }
                            url = f'https://www.tiktok.com/@{target}'
                            url1 = 'https://api16-normal-c-alisg.tiktokv.com/passport/login_name/update/?iid=7060509952591595266&device_id=7054537563859764742&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=230005&version_name=23.0.5&device_platform=android&ab_version=23.0.5&ssmix=a&device_type=SM-N975F&device_brand=samsung&language=en&os_api=25&os_version=7.1.2&openudid=a0fa5ae7590c6576&manifest_version_code=2022300050&resolution=1600*900&dpi=300&update_version_code=2022300050&_rticket=1644335649391&current_region=JO&app_type=normal&sys_region=US&mcc_mnc=41601&timezone_name=America%2FChicago&residence=JO&ts=1644335648&timezone_offset=-21600&build_number=23.0.5&region=US&uoo=0&app_language=en&carrier_region=JO&locale=en&op_region=JO&ac2=wifi&host_abi=x86&cdid=63d7e01e-5508-4742-ad36-df84088dcef8&support_webview=1&okhttp_version=4.1.73.9-tiktok'
                            url2 = 'https://api16-normal-c-alisg.tiktokv.com/aweme/v1/commit/user/?iid=7053806752974882566&device_id=6994798204819621382&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=220804&version_name=22.8.4&device_platform=android&ab_version=22.8.4&ssmix=a&device_type=SM-N975F&device_brand=samsung&language=en&os_api=25&os_version=7.1.2&openudid=c1d415ad940052b3&manifest_version_code=2022208040&resolution=720*1280&dpi=240&update_version_code=2022208040&_rticket=1642346163746&current_region=JO&app_type=normal&sys_region=US&mcc_mnc=41603&timezone_name=Asia%2FShanghai&residence=JO&ts=1642346163&timezone_offset=28800&build_number=22.8.4&region=US&uoo=1&app_language=en&carrier_region=JO&locale=en&op_region=JO&ac2=wifi&host_abi=x86&cdid=b2d439e0-8d34-45ee-b889-3f94c2882af2'

                            headers = {
                                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76'
                            }

                            headers1 = {
                                'accept-encoding': 'gzip',
                                'connection': 'Keep-Alive',
                                'content-length': '61',
                                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                'cookie': f'store-idc=alisg; store-country-code=jo; passport_csrf_token=4f090f6c688d34439023d87c94284d56; passport_csrf_token_default=4f090f6c688d34439023d87c94284d56; d_ticket=1a360b478360784d60e9c19bab2975d299648; multi_sids=7053658438690620417%3A{rsession}; cmpl_token=AgQQAPOlF-RPsLHdTl3tJZ04-3Ma2-5Pf4QuYMIzrw; odin_tt=d62f0efc196a8d93560631a047a87752c12f5ddfe33609a464231b966571be6fb2ff3fe1ba12167eceb59eb2dd3132d2bfec5cbae962019f47d62fa73b1768bed92d4c701d38b567cbf2bb9573a96c20; sid_guard={rsession}%7C1642342749%7C5183999%7CThu%2C+17-Mar-2022+14%3A19%3A08+GMT; uid_tt=ce5c1917610acacc9ac99631c4e012316730e233d63a978a93413f7a09985b49; uid_tt_ss=ce5c1917610acacc9ac99631c4e012316730e233d63a978a93413f7a09985b49; sid_tt={rsession}; ; sessionid_ss={rsession}',
                                'passport-sdk-version': '19',
                                'x-gorgon': '040400d140002934b0b8bc7150ef56d1363224801d3c99ce90c3',
                                'user-agent': 'com.zhiliaoapp.musically/2022208040 (Linux; U; Android 7.1.2; en; SM-N975F; Build/N2G48H;tt-ok/3.10.0.2)'
                            }
                            data_signature = f'signature={Cus_Bio}'
                            data_nickname = f"nickname={name}"
                            data_username = f'login_name={target}&page_from=0'
                            req = \
                            requests.get(url, headers=headers, proxies=PROXYY).text.split('"preloadList":[]}}')[1].split(
                                '"I18n"')[0]
                            # print(req)
                            att += 1
                            if '{"followerCount":' in req or req == ',"UserPage":{"statusCode":10221},' or req == ',"UserPage":{"statusCode":10223},' or req == ',"UserPage":{"statusCode":10225},' or req == ',"UserPage":{"statusCode":10101},':
                                reqs += 1
                            elif req == ',"UserPage":{"statusCode":10202},':
                                try:
                                    req1 = requests.post(url1, headers=headers1, data=data_username,
                                                         proxies=PROXYY).text
                                    # print(req1)
                                    if target not in cuser:
                                        if f'"message":"success"' in req1 or req1 == f'"Login_name":"{target}"':
                                            print(
                                                f'\r{RED}[{RESET}{target}{RED}] Catched ;)\n{RED}[{RESET}{rsession}{RED}] SessionID\n\n',
                                                end='')
                                            requests.post(url2, headers=headers1, data=data_signature).text
                                            requests.post(url2, headers=headers1, data=data_nickname).text
                                            DWH.execute()
                                            DWH2.execute()
                                            with open(f'@{target} Info.txt', 'a') as xx:
                                                xx.write(f'Username : {target}\nSessionID : {rsession}')
                                            Lsessions.remove(rsession)
                                            cuser.append(target)
                                            cmb(None,
                                                f'Catched > {target}  \nAttemps : {"{:,}".format(att)}',
                                                '@Ajarmah TikTok Claimer')

                                    if '"description":"login name can only be updated once within one month."' in req1:
                                        if rsession not in cuser:
                                            print(f'\r{RED}This Session Has 1 month Limit >>> SID : {rsession}{RESET}',
                                                  end='')
                                            Lsessions.remove(rsession)
                                            cuser.append(rsession)

                                    if '"description":"The conversation has expired, please log in again"' in req1:
                                        if rsession not in cuser:
                                            cmb(None, f'This SessionID Has Expired !  \nSid : {rsession}',
                                                '@Ajarmah TikTok Claimer')
                                            Lsessions.remove(rsession)
                                            cuser.append(rsession)

                                    if '"description":"Too many attempts. Try again later."' in req1:
                                        pass

                                except:
                                    pass
                            else:
                                err += 1
                            before = att
                            sleep(1)
                            RS = att - before
                            sss(f'Ok : {"{:,}".format(reqs)}  |  Bad - ErrorProxy : {"{:,}".format(err)}  |  R\S : {"{:,}".format(RS)}  |  SIDs : {len(Lsessions)}')

                        except requests.exceptions.ConnectionError:
                            err +=1
                        except requests.exceptions.ReadTimeout:
                            err +=1
                        except requests.exceptions.ChunkedEncodingError:
                            err +=1
                        except IndexError:
                            err +=1


                for i in range(thr):
                    thread1 = threading.Thread(target=Claim_us)
                    thread1.daemon = True
                    thread1.start()
                    threads.append(thread1)
                for thread2 in threads:
                    thread2.join()

        except FileNotFoundError:
            print('Please Write Proxy File Name Correct In Settings File')
            input('')
            exit(0)

else:
    print(f'\n\t{RED} Please Choose !!!!')
    input('')
    exit(0)
    hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
    req = requests.get('https://pastebin.com/AaAa10101').text
    if hwid not in req:
        print('Contact >>> IG @Ajarmah - @_vt.done <<< For Activation ..')
        print('Take A photo Of This And Send It To him :')
        print(hwid)
        with open("AcCode.txt", "a") as xxcc:
            xxcc.write(
                f' Activation Code : {hwid}\n\nSend This To Me To Activate\nInstagram : @Ajarmah - @_vt.done\n\n\n')
        print(f'\nDone Saved Your Activation Code in "AcCode.txt"\n')
        input('Press Enter To Exit')
        exit()
    if hwid in req:
        clear()
        pass




try:
    from discord_webhook import DiscordEmbed
    from discord_webhook import DiscordWebhook

except ModuleNotFoundError:
    print('Please Wait .')
    sleep(1.6)
    clear()
    os.system('pip install discord_webhook')
    clear()
    from discord_webhook import DiscordEmbed
    from discord_webhook import DiscordWebhook

try:
    import colorama
except ModuleNotFoundError:
    print('Please Wait .')
    sleep(1.6)
    clear()
    os.system('pip install colorama')
    clear()
    import colorama

try:
    import json
except ModuleNotFoundError:
    print('Please Wait .')
    sleep(1.6)
    clear()
    os.system('pip install json')
    clear()
    import json

try:
    import ctypes
except ModuleNotFoundError:
    print('Please Wait .')
    sleep(1.6)
    clear()
    os.system('pip install ctypes')
    clear()
    import ctypes

try:
    import random
except ModuleNotFoundError:
    print('Please Wait .')
    sleep(1.6)
    clear()
    os.system('pip install random')
    clear()
    import random

try:
    import threading
except ModuleNotFoundError:
    print('Please Wait .')
    sleep(1.6)
    clear()
    os.system('pip install threading')
    clear()
    import threading
try:
    from colorama import Fore
except ModuleNotFoundError:
    print('Please Wait .')
    sleep(1.6)
    clear()
    os.system('pip install colorama')
    clear()
    from colorama import Fore

sss = ctypes.windll.kernel32.SetConsoleTitleW
cmb = ctypes.windll.user32.MessageBoxW
colorama.init(autoreset=True)

sss('Logging In ...')
sleep(2)
sss('Logged ...')
sleep(2)
GREEN = Fore.GREEN
RED = Fore.RED
RESET = Fore.RESET
sss('Tiktok Claimer by @Ajarmah')
sleep(2.5)
Lsessions = []
Lusers = []
Lproxies = []
cuser = []
csess = []
threads = []

prox_type = ['http', 'https', 'socks4']

att, reqs, err = 0, 0, 0

try:
    sett_open = open('settings.txt').read()
except FileNotFoundError:
    print('Please Put Settings File In The Same Folder !')
    input('')
    exit(0)


try :
    sett_file = json.loads(sett_open)
    thr = int(sett_file[0]["Please_Write_The_Informations"]["Threads"])
    sessi_list = sett_file[0]["Please_Write_The_Informations"]["Sessions_List"]
    proxy_list = sett_file[0]["Please_Write_The_Informations"]["Proxies_List"]
    proxy_type = sett_file[0]["Please_Write_The_Informations"]["Proxy_Type"]

    name = sett_file[1]["You_Can_Leave_Them_Empty"]["Your_Name"]
    Dis_Webhook = sett_file[1]["You_Can_Leave_Them_Empty"]["Your_Discord_WebHook"]
    Cus_Bio = sett_file[1]["You_Can_Leave_Them_Empty"]["Bio"]
except:
    cmb(None, f'Error In Settings File ! ', '@Ajarmah TikTok Claimer')
    csess.append('NOSESSLEFT')
    input('')
    exit(0)

try:
    sess_file = open(sessi_list).read().splitlines()
    for session in sess_file:
        Lsessions.append(session)
    if len(Lsessions) == 0:
        print(f'Sessions File Is Empty ! > {sessi_list}')
        input('')
        exit(0)
except FileNotFoundError:
    print('Please Write Sessions File Name Correct In Settings File')
    input('')
    exit(0)


if Dis_Webhook == '':
    Dis_Webhook = 'https://discord.com/api/webhooks/'

if Cus_Bio == '':
    Cus_Bio = 'Claimed by IG - @Ajarmah'

if name == '':
    name = 'Sir'
else:
    name = name


if proxy_list == '':
    print('Please Put Proxy File Name In Settings File ')
    input('')
    exit(0)


elif not proxy_type in prox_type:
    print('Please Write Proxy type Name Correct In Settings File')
    input('')
    exit(0)

print(f'{RED}[{RESET}1{RED}] List\n{RED}[{RESET}2{RED}] Target\n')
mode = int(input('<?> Mode : '))
clear()

if mode==1:
    try:
        users_list = sett_file[0]["Please_Write_The_Informations"]["Users_List"]
    except:
        cmb(None, f'Error In Settings File ! ', '@Ajarmah TikTok Claimer')
        csess.append('NOSESSLEFT')
        input('')
        exit(0)
    print(f"Hi {GREEN}{name}{RESET}... {RED}\nIf The Claimer Does't Run After 10-20 Second,\nCheck Your Settings File , or Check Your Proxies Type .{RESET}")
    sleep(2.5)
    clear()

    try:
        users_file = open(users_list).read().splitlines()
        for user in users_file:
            if user.isdigit() == False:
                Lusers.append(user)
        if len(Lusers) == 0:
            print(f'Users File Is Empty ! > {users_list}')
            input('')
            exit(0)
    except FileNotFoundError:
        print('Please Write Users File Name Correct In Settings File')
        input('')
        exit(0)

    if 'http' in proxy_type or proxy_type == 'https':
        try:
            proxy_file = open(proxy_list).read().splitlines()
            for prox in proxy_file:
                Lproxies.append(prox)
            if len(Lproxies) == 0:
                print(f'Proxies File Is Empty ! > {proxy_list}')
                input('')
                exit(0)
            elif len(Lproxies) >= 1:
                # print(f'{GREEN}[{RESET}+{GREEN}] Successfully Loaded :\n\t{GREEN}[{RESET}{len(Lusers)}{GREEN}] List Count\n\t{GREEN}[{RESET}{len(Lproxies)}{GREEN}] Proxies Count\n\t{GREEN}[{RESET}{len(Lsessions)}{GREEN}] Sessions Count')
                # input('')
                def Claim_ls():
                    global att, reqs, err
                    while True:
                        runn = str(random.choice(Lproxies))
                        ruser = random.choice(Lusers)
                        DWH = DiscordWebhook(
                            url='https://discord.com/api/webhooks/')
                        DWH2 = DiscordWebhook(url=Dis_Webhook)
                        EMK = DiscordEmbed(title=f"Claimed > @{ruser}\n""Requests > {:,}".format(att),
                                           description='Coded by @Ajarmah\n\n@Ajarmah - @_vt.done',
                                           color=14681863)
                        EMK.set_thumbnail(url='https://imgur.com/m6lYzYC.gif')
                        DWH.add_embed(EMK)
                        DWH2.add_embed(EMK)
                        try:
                            rsession = random.choice(Lsessions)
                        except IndexError:
                            if 'NOSESSLEFT' not in csess:
                                if len(Lsessions) == 0:
                                    if 'NOSESSLEFT' not in csess:
                                        cmb(None, f'No Sessions Left Habebi ;-/', '@Ajarmah TikTok Claimer')
                                        csess.append('NOSESSLEFT')
                        try:
                            PROXYY = {
                                'http': 'http://{}'.format(runn),
                                'https': 'https://{}'.format(runn),
                                'http': '{}'.format(runn),
                                'https': '{}'.format(runn)
                            }
                            url = f'https://www.tiktok.com/@{ruser}'
                            url1 = 'https://api16-normal-c-alisg.tiktokv.com/passport/login_name/update/?iid=7060509952591595266&device_id=7054537563859764742&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=230005&version_name=23.0.5&device_platform=android&ab_version=23.0.5&ssmix=a&device_type=SM-N975F&device_brand=samsung&language=en&os_api=25&os_version=7.1.2&openudid=a0fa5ae7590c6576&manifest_version_code=2022300050&resolution=1600*900&dpi=300&update_version_code=2022300050&_rticket=1644335649391&current_region=JO&app_type=normal&sys_region=US&mcc_mnc=41601&timezone_name=America%2FChicago&residence=JO&ts=1644335648&timezone_offset=-21600&build_number=23.0.5&region=US&uoo=0&app_language=en&carrier_region=JO&locale=en&op_region=JO&ac2=wifi&host_abi=x86&cdid=63d7e01e-5508-4742-ad36-df84088dcef8&support_webview=1&okhttp_version=4.1.73.9-tiktok'
                            url2 = 'https://api16-normal-c-alisg.tiktokv.com/aweme/v1/commit/user/?iid=7053806752974882566&device_id=6994798204819621382&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=220804&version_name=22.8.4&device_platform=android&ab_version=22.8.4&ssmix=a&device_type=SM-N975F&device_brand=samsung&language=en&os_api=25&os_version=7.1.2&openudid=c1d415ad940052b3&manifest_version_code=2022208040&resolution=720*1280&dpi=240&update_version_code=2022208040&_rticket=1642346163746&current_region=JO&app_type=normal&sys_region=US&mcc_mnc=41603&timezone_name=Asia%2FShanghai&residence=JO&ts=1642346163&timezone_offset=28800&build_number=22.8.4&region=US&uoo=1&app_language=en&carrier_region=JO&locale=en&op_region=JO&ac2=wifi&host_abi=x86&cdid=b2d439e0-8d34-45ee-b889-3f94c2882af2'

                            headers = {
                                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76'
                            }

                            headers1 = {
                                'accept-encoding': 'gzip',
                                'connection': 'Keep-Alive',
                                'content-length': '61',
                                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                'cookie': f'store-idc=alisg; store-country-code=jo; passport_csrf_token=4f090f6c688d34439023d87c94284d56; passport_csrf_token_default=4f090f6c688d34439023d87c94284d56; d_ticket=1a360b478360784d60e9c19bab2975d299648; multi_sids=7053658438690620417%3A{rsession}; cmpl_token=AgQQAPOlF-RPsLHdTl3tJZ04-3Ma2-5Pf4QuYMIzrw; odin_tt=d62f0efc196a8d93560631a047a87752c12f5ddfe33609a464231b966571be6fb2ff3fe1ba12167eceb59eb2dd3132d2bfec5cbae962019f47d62fa73b1768bed92d4c701d38b567cbf2bb9573a96c20; sid_guard={rsession}%7C1642342749%7C5183999%7CThu%2C+17-Mar-2022+14%3A19%3A08+GMT; uid_tt=ce5c1917610acacc9ac99631c4e012316730e233d63a978a93413f7a09985b49; uid_tt_ss=ce5c1917610acacc9ac99631c4e012316730e233d63a978a93413f7a09985b49; sid_tt={rsession}; ; sessionid_ss={rsession}',
                                'passport-sdk-version': '19',
                                'x-gorgon': '040400d140002934b0b8bc7150ef56d1363224801d3c99ce90c3',
                                'user-agent': 'com.zhiliaoapp.musically/2022208040 (Linux; U; Android 7.1.2; en; SM-N975F; Build/N2G48H;tt-ok/3.10.0.2)'
                            }
                            data_signature = f'signature={Cus_Bio}'
                            data_nickname = f"nickname={name}"
                            data_username = f'login_name={ruser}&page_from=0'
                            req = requests.get(url, headers=headers, proxies=PROXYY).text.split('"preloadList":[]}}')[1].split('"I18n"')[0]
                            att += 1
                            if '{"followerCount":' in req or req==',"UserPage":{"statusCode":10221},' or req==',"UserPage":{"statusCode":10223},' or req==',"UserPage":{"statusCode":10225},' or req==',"UserPage":{"statusCode":10101},':
                                reqs += 1
                            elif req == ',"UserPage":{"statusCode":10202},':
                                try:
                                    req1 = requests.post(url1, headers=headers1, data=data_username, proxies=PROXYY).text
                                    # print(req1)
                                    if ruser not in cuser:
                                        if f'"message":"success"' in req1 or req1 == f'"Login_name":"{ruser}"':
                                            print(
                                                f'\r{GREEN}[{RESET}{ruser}{GREEN}] Done Claimed ;)\n{GREEN}[{RESET}{rsession}{GREEN}] SessionID\n\n',
                                                end='')
                                            requests.post(url2, headers=headers1, data=data_signature).text
                                            requests.post(url2, headers=headers1, data=data_nickname).text
                                            DWH.execute()
                                            DWH2.execute()
                                            with open(f'@{ruser} Info.txt', 'a') as xx:
                                                xx.write(f'Username : {ruser}\nSessionID : {rsession}')
                                            Lsessions.remove(rsession)
                                            cuser.append(ruser)
                                            cmb(None,
                                                f'New Claim > {ruser}  \nAttemps : {"{:,}".format(att)}',
                                                '@Ajarmah TikTok Claimer')

                                    if '"description":"login name can only be updated once within one month."' in req1:
                                        if rsession not in cuser:
                                            print(f'\r{RED}This Session Has 1 month Limit >>> SID : {rsession}\n{ruser}{RESET}\n',end='')
                                            Lsessions.remove(rsession)
                                            cuser.append(rsession)
                                        if len(Lsessions) >= 1:
                                            req = requests.post(url1, headers=headers1, data=data_username, proxies=PROXYY).text
                                            if ruser not in cuser:
                                                if f'"message":"success"' in req or req==f'"Login_name":"{ruser}"':
                                                    print(
                                                        f'\r{GREEN}[{RESET}{ruser}{GREEN}] Done Claimed ;)\n{GREEN}[{RESET}{rsession}{GREEN}] SessionID\n\n',
                                                        end='')
                                                    requests.post(url2, headers=headers1, data=data_signature).text
                                                    requests.post(url2, headers=headers1, data=data_nickname).text
                                                    DWH.execute()
                                                    DWH2.execute()
                                                    with open(f'@{ruser} Info.txt', 'a') as xx:
                                                        xx.write(f'Username : {ruser}\nSessionID : {rsession}')
                                                    Lsessions.remove(rsession)
                                                    cuser.append(ruser)
                                                    cmb(None,
                                                        f'New Claim > {ruser}  \nAttemps : {"{:,}".format(att)}',
                                                        '@Ajarmah TikTok Claimer')


                                    if '"description":"The conversation has expired, please log in again"' in req1:
                                        if rsession not in cuser:
                                            cmb(None, f'This SessionID Has Expired !  \nSid : {rsession}',
                                                '@Ajarmah TikTok Claimer')
                                            Lsessions.remove(rsession)
                                            cuser.append(rsession)

                                    if '"description":"Too many attempts. Try again later."' in req1:
                                        pass

                                except:
                                    pass
                            else:
                                err += 1
                            before = att
                            sleep(1)
                            RS = att - before
                            sss(f'Ok : {"{:,}".format(reqs)}  |  Bad - ErrorProxy : {"{:,}".format(err)}  |  R\S : {"{:,}".format(RS)}  |  SIDs : {len(Lsessions)}')

                        except requests.exceptions.ConnectionError:
                            err +=1
                        except requests.exceptions.ReadTimeout:
                            err +=1
                        except requests.exceptions.ChunkedEncodingError:
                            err +=1
                        except IndexError:
                            pass


                for i in range(thr):
                    thread1 = threading.Thread(target=Claim_ls)
                    thread1.daemon = True
                    thread1.start()
                    threads.append(thread1)
                for thread2 in threads:
                    thread2.join()
        except FileNotFoundError:
            print('Please Write Proxy File Name Correct In Settings File')
            input('')
            exit(0)
    elif proxy_type == 'socks4':
        clear()
        os.system('pip install pysocks')
        clear()
        try:
            proxy_file = open(proxy_list).read().splitlines()
            for prox in proxy_file:
                Lproxies.append(prox)
            if len(Lproxies) == 0:
                print(f'Proxies File Is Empty ! > {proxy_list}')
                input('')
                exit(0)
            elif len(Lproxies) >= 1:
                def Claim_ls():
                    global att, reqs, err
                    while True:
                        runn = str(random.choice(Lproxies))
                        ruser = random.choice(Lusers)
                        DWH = DiscordWebhook(url='https://discord.com/api/webhooks/')
                        DWH2 = DiscordWebhook(url=Dis_Webhook)
                        EMK = DiscordEmbed(title=f"Claimed > @{ruser}\n""Requests > {:,}".format(att),
                                           description='Coded by @Ajarmah\n\n@Ajarmah - @_vt.done',
                                           color=14681863)
                        EMK.set_thumbnail(url='https://imgur.com/m6lYzYC.gif')
                        DWH.add_embed(EMK)
                        DWH2.add_embed(EMK)
                        try:
                            rsession = random.choice(Lsessions)
                        except IndexError:
                            if 'NOSESSLEFT' not in csess:
                                if len(Lsessions) == 0:
                                    if 'NOSESSLEFT' not in csess:
                                        cmb(None, f'No Sessions Left Habebi ;-/', '@Ajarmah TikTok Claimer')
                                        csess.append('NOSESSLEFT')
                        try:
                            PROXYY = {
                                'http': 'socks4://{}'.format(runn),
                                'https': 'socks4://{}'.format(runn)
                            }
                            url = f'https://www.tiktok.com/@{ruser}'
                            url1 = 'https://api16-normal-c-alisg.tiktokv.com/passport/login_name/update/?iid=7060509952591595266&device_id=7054537563859764742&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=230005&version_name=23.0.5&device_platform=android&ab_version=23.0.5&ssmix=a&device_type=SM-N975F&device_brand=samsung&language=en&os_api=25&os_version=7.1.2&openudid=a0fa5ae7590c6576&manifest_version_code=2022300050&resolution=1600*900&dpi=300&update_version_code=2022300050&_rticket=1644335649391&current_region=JO&app_type=normal&sys_region=US&mcc_mnc=41601&timezone_name=America%2FChicago&residence=JO&ts=1644335648&timezone_offset=-21600&build_number=23.0.5&region=US&uoo=0&app_language=en&carrier_region=JO&locale=en&op_region=JO&ac2=wifi&host_abi=x86&cdid=63d7e01e-5508-4742-ad36-df84088dcef8&support_webview=1&okhttp_version=4.1.73.9-tiktok'
                            url2 = 'https://api16-normal-c-alisg.tiktokv.com/aweme/v1/commit/user/?iid=7053806752974882566&device_id=6994798204819621382&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=220804&version_name=22.8.4&device_platform=android&ab_version=22.8.4&ssmix=a&device_type=SM-N975F&device_brand=samsung&language=en&os_api=25&os_version=7.1.2&openudid=c1d415ad940052b3&manifest_version_code=2022208040&resolution=720*1280&dpi=240&update_version_code=2022208040&_rticket=1642346163746&current_region=JO&app_type=normal&sys_region=US&mcc_mnc=41603&timezone_name=Asia%2FShanghai&residence=JO&ts=1642346163&timezone_offset=28800&build_number=22.8.4&region=US&uoo=1&app_language=en&carrier_region=JO&locale=en&op_region=JO&ac2=wifi&host_abi=x86&cdid=b2d439e0-8d34-45ee-b889-3f94c2882af2'

                            headers = {
                                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76'
                            }

                            headers1 = {
                                'accept-encoding': 'gzip',
                                'connection': 'Keep-Alive',
                                'content-length': '61',
                                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                'cookie': f'store-idc=alisg; store-country-code=jo; passport_csrf_token=4f090f6c688d34439023d87c94284d56; passport_csrf_token_default=4f090f6c688d34439023d87c94284d56; d_ticket=1a360b478360784d60e9c19bab2975d299648; multi_sids=7053658438690620417%3A{rsession}; cmpl_token=AgQQAPOlF-RPsLHdTl3tJZ04-3Ma2-5Pf4QuYMIzrw; odin_tt=d62f0efc196a8d93560631a047a87752c12f5ddfe33609a464231b966571be6fb2ff3fe1ba12167eceb59eb2dd3132d2bfec5cbae962019f47d62fa73b1768bed92d4c701d38b567cbf2bb9573a96c20; sid_guard={rsession}%7C1642342749%7C5183999%7CThu%2C+17-Mar-2022+14%3A19%3A08+GMT; uid_tt=ce5c1917610acacc9ac99631c4e012316730e233d63a978a93413f7a09985b49; uid_tt_ss=ce5c1917610acacc9ac99631c4e012316730e233d63a978a93413f7a09985b49; sid_tt={rsession}; ; sessionid_ss={rsession}',
                                'passport-sdk-version': '19',
                                'x-gorgon': '040400d140002934b0b8bc7150ef56d1363224801d3c99ce90c3',
                                'user-agent': 'com.zhiliaoapp.musically/2022208040 (Linux; U; Android 7.1.2; en; SM-N975F; Build/N2G48H;tt-ok/3.10.0.2)'
                            }
                            data_signature = f'signature={Cus_Bio}'
                            data_nickname = f"nickname={name}"
                            data_username = f'login_name={ruser}&page_from=0'
                            req = requests.get(url, headers=headers, proxies=PROXYY).text.split('"preloadList":[]}}')[1].split('"I18n"')[0]
                            # print(req)
                            att += 1
                            if '{"followerCount":' in req or req==',"UserPage":{"statusCode":10221},' or req==',"UserPage":{"statusCode":10223},' or req==',"UserPage":{"statusCode":10225},' or req==',"UserPage":{"statusCode":10101},':
                                reqs += 1
                            elif req == ',"UserPage":{"statusCode":10202},':
                                try:
                                    req1 = requests.post(url1, headers=headers1, data=data_username, proxies=PROXYY).text
                                    # print(req1)
                                    if ruser not in cuser:
                                        if f'"message":"success"' in req1 or req1 == f'"Login_name":"{ruser}"':
                                            print(
                                                f'\r{GREEN}[{RESET}{ruser}{GREEN}] Done Claimed ;)\n{GREEN}[{RESET}{rsession}{GREEN}] SessionID\n\n',
                                                end='')
                                            requests.post(url2, headers=headers1, data=data_signature).text
                                            requests.post(url2, headers=headers1, data=data_nickname).text
                                            DWH.execute()
                                            DWH2.execute()
                                            with open(f'@{ruser} Info.txt', 'a') as xx:
                                                xx.write(f'Username : {ruser}\nSessionID : {rsession}')
                                            Lsessions.remove(rsession)
                                            cuser.append(ruser)
                                            cmb(None,
                                                f'New Claim > {ruser}  \nAttemps : {"{:,}".format(att)}',
                                                '@Ajarmah TikTok Claimer')

                                    if '"description":"login name can only be updated once within one month."' in req1:
                                        if rsession not in cuser:
                                            print(
                                                f'\r{RED}This Session Has 1 month Limit >>> SID : {rsession}\n{ruser}{RESET}\n',
                                                end='')
                                            Lsessions.remove(rsession)
                                            cuser.append(rsession)
                                        if len(Lsessions) >= 1:
                                            req = requests.post(url1, headers=headers1, data=data_username,
                                                                proxies=PROXYY).text
                                            if ruser not in cuser:
                                                if f'"message":"success"' in req or req == f'"Login_name":"{ruser}"':
                                                    print(
                                                        f'\r{GREEN}[{RESET}{ruser}{GREEN}] Done Claimed ;)\n{GREEN}[{RESET}{rsession}{GREEN}] SessionID\n\n',
                                                        end='')
                                                    requests.post(url2, headers=headers1, data=data_signature).text
                                                    requests.post(url2, headers=headers1, data=data_nickname).text
                                                    DWH.execute()
                                                    DWH2.execute()
                                                    with open(f'@{ruser} Info.txt', 'a') as xx:
                                                        xx.write(f'Username : {ruser}\nSessionID : {rsession}')
                                                    Lsessions.remove(rsession)
                                                    cuser.append(ruser)
                                                    cmb(None,
                                                        f'New Claim > {ruser}  \nAttemps : {"{:,}".format(att)}',
                                                        '@Ajarmah TikTok Claimer')

                                    if '"description":"The conversation has expired, please log in again"' in req1:
                                        if rsession not in cuser:
                                            cmb(None, f'This SessionID Has Expired !  \nSid : {rsession}',
                                                '@Ajarmah TikTok Claimer')
                                            Lsessions.remove(rsession)
                                            cuser.append(rsession)

                                    if '"description":"Too many attempts. Try again later."' in req1:
                                        pass

                                except:
                                    pass
                            else:
                                err += 1
                            before = att
                            sleep(1)
                            RS = att - before
                            sss(f'Ok : {"{:,}".format(reqs)}  |  Bad - ErrorProxy : {"{:,}".format(err)}  |  R\S : {"{:,}".format(RS)}  |  SIDs : {len(Lsessions)}')

                        except requests.exceptions.ConnectionError:
                            err +=1
                        except requests.exceptions.ReadTimeout:
                            err +=1
                        except requests.exceptions.ChunkedEncodingError:
                            err +=1
                        except IndexError:
                            pass


                for i in range(thr):
                    thread1 = threading.Thread(target=Claim_ls)
                    thread1.daemon = True
                    thread1.start()
                    threads.append(thread1)
                for thread2 in threads:
                    thread2.join()
        except FileNotFoundError:
            print('Please Write Proxy File Name Correct In Settings File')
            input('')
            exit(0)


elif mode==2:
    target = input('<?> Target : ')
    print(
        f"Hi {GREEN}{name}{RESET}... {RED}\nIf The Claimer Does't Run After 10-20 Second,\nCheck Your Settings File , or Check Your Proxies Type .{RESET}")
    sleep(2.5)
    clear()
    if 'http' in proxy_type or proxy_type == 'https':
        try:
            proxy_file = open(proxy_list).read().splitlines()
            for prox in proxy_file:
                Lproxies.append(prox)
            if len(Lproxies) == 0:
                print(f'Proxies File Is Empty ! > {proxy_list}')
                input('')
                exit(0)
            elif len(Lproxies) >= 1:
                # print(f'{GREEN}[{RESET}+{GREEN}] Successfully Loaded :\n\t{GREEN}[{RESET}{len(Lusers)}{GREEN}] List Count\n\t{GREEN}[{RESET}{len(Lproxies)}{GREEN}] Proxies Count\n\t{GREEN}[{RESET}{len(Lsessions)}{GREEN}] Sessions Count')
                # input('')
                def Claim_us():
                    global att, reqs, err
                    while True:
                        runn = str(random.choice(Lproxies))
                        DWH = DiscordWebhook(url='https://discord.com/api/webhooks/')
                        DWH2 = DiscordWebhook(url=Dis_Webhook)
                        EMK = DiscordEmbed(title=f"Catched > @{target}\n""Requests > {:,}".format(att),
                                           description='Coded by @Ajarmah\n\n@Ajarmah - @_vt.done',
                                           color=14681863)
                        EMK.set_thumbnail(url='https://imgur.com/m6lYzYC.gif')
                        DWH.add_embed(EMK)
                        DWH2.add_embed(EMK)
                        try:
                            rsession = random.choice(Lsessions)
                        except IndexError:
                            threading.Lock()
                            pass
                        try:
                            PROXYY = {
                                'http': 'http://{}'.format(runn),
                                'https': 'https://{}'.format(runn),
                                'http': '{}'.format(runn),
                                'https': '{}'.format(runn)
                            }
                            url = f'https://www.tiktok.com/@{target}'
                            url1 = 'https://api16-normal-c-alisg.tiktokv.com/passport/login_name/update/?iid=7060509952591595266&device_id=7054537563859764742&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=230005&version_name=23.0.5&device_platform=android&ab_version=23.0.5&ssmix=a&device_type=SM-N975F&device_brand=samsung&language=en&os_api=25&os_version=7.1.2&openudid=a0fa5ae7590c6576&manifest_version_code=2022300050&resolution=1600*900&dpi=300&update_version_code=2022300050&_rticket=1644335649391&current_region=JO&app_type=normal&sys_region=US&mcc_mnc=41601&timezone_name=America%2FChicago&residence=JO&ts=1644335648&timezone_offset=-21600&build_number=23.0.5&region=US&uoo=0&app_language=en&carrier_region=JO&locale=en&op_region=JO&ac2=wifi&host_abi=x86&cdid=63d7e01e-5508-4742-ad36-df84088dcef8&support_webview=1&okhttp_version=4.1.73.9-tiktok'
                            url2 = 'https://api16-normal-c-alisg.tiktokv.com/aweme/v1/commit/user/?iid=7053806752974882566&device_id=6994798204819621382&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=220804&version_name=22.8.4&device_platform=android&ab_version=22.8.4&ssmix=a&device_type=SM-N975F&device_brand=samsung&language=en&os_api=25&os_version=7.1.2&openudid=c1d415ad940052b3&manifest_version_code=2022208040&resolution=720*1280&dpi=240&update_version_code=2022208040&_rticket=1642346163746&current_region=JO&app_type=normal&sys_region=US&mcc_mnc=41603&timezone_name=Asia%2FShanghai&residence=JO&ts=1642346163&timezone_offset=28800&build_number=22.8.4&region=US&uoo=1&app_language=en&carrier_region=JO&locale=en&op_region=JO&ac2=wifi&host_abi=x86&cdid=b2d439e0-8d34-45ee-b889-3f94c2882af2'

                            headers = {
                                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76'
                            }

                            headers1 = {
                                'accept-encoding': 'gzip',
                                'connection': 'Keep-Alive',
                                'content-length': '61',
                                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                'cookie': f'store-idc=alisg; store-country-code=jo; passport_csrf_token=4f090f6c688d34439023d87c94284d56; passport_csrf_token_default=4f090f6c688d34439023d87c94284d56; d_ticket=1a360b478360784d60e9c19bab2975d299648; multi_sids=7053658438690620417%3A{rsession}; cmpl_token=AgQQAPOlF-RPsLHdTl3tJZ04-3Ma2-5Pf4QuYMIzrw; odin_tt=d62f0efc196a8d93560631a047a87752c12f5ddfe33609a464231b966571be6fb2ff3fe1ba12167eceb59eb2dd3132d2bfec5cbae962019f47d62fa73b1768bed92d4c701d38b567cbf2bb9573a96c20; sid_guard={rsession}%7C1642342749%7C5183999%7CThu%2C+17-Mar-2022+14%3A19%3A08+GMT; uid_tt=ce5c1917610acacc9ac99631c4e012316730e233d63a978a93413f7a09985b49; uid_tt_ss=ce5c1917610acacc9ac99631c4e012316730e233d63a978a93413f7a09985b49; sid_tt={rsession}; ; sessionid_ss={rsession}',
                                'passport-sdk-version': '19',
                                'x-gorgon': '040400d140002934b0b8bc7150ef56d1363224801d3c99ce90c3',
                                'user-agent': 'com.zhiliaoapp.musically/2022208040 (Linux; U; Android 7.1.2; en; SM-N975F; Build/N2G48H;tt-ok/3.10.0.2)'
                            }
                            data_signature = f'signature={Cus_Bio}'
                            data_nickname = f"nickname={name}"
                            data_username = f'login_name={target}&page_from=0'
                            req = \
                            requests.get(url, headers=headers, proxies=PROXYY).text.split('"preloadList":[]}}')[1].split(
                                '"I18n"')[0]
                            # print(req)
                            att += 1
                            if '{"followerCount":' in req or req == ',"UserPage":{"statusCode":10221},' or req == ',"UserPage":{"statusCode":10223},' or req == ',"UserPage":{"statusCode":10225},' or req == ',"UserPage":{"statusCode":10101},':
                                reqs += 1
                            elif req == ',"UserPage":{"statusCode":10202},':
                                try:
                                    req1 = requests.post(url1, headers=headers1, data=data_username,
                                                         proxies=PROXYY).text
                                    print(req1)
                                    # print(req1)
                                    if target not in cuser:
                                        if f'"message":"success"' in req1 or req1 == f'"Login_name":"{target}"':
                                            print(
                                                f'\r{RED}[{RESET}{target}{RED}] Catched ;)\n{RED}[{RESET}{rsession}{RED}] SessionID\n\n',
                                                end='')
                                            requests.post(url2, headers=headers1, data=data_signature).text
                                            requests.post(url2, headers=headers1, data=data_nickname).text
                                            DWH.execute()
                                            DWH2.execute()
                                            with open(f'@{target} Info.txt', 'a') as xx:
                                                xx.write(f'Username : {target}\nSessionID : {rsession}')
                                            Lsessions.remove(rsession)
                                            cuser.append(target)
                                            cmb(None,
                                                f'Catched > {target}  \nAttemps : {"{:,}".format(att)}',
                                                '@Ajarmah TikTok Claimer')

                                    if '"description":"login name can only be updated once within one month."' in req1:
                                        if rsession not in cuser:
                                            print(f'\r{RED}This Session Has 1 month Limit >>> SID : {rsession}{RESET}',
                                                  end='')
                                            Lsessions.remove(rsession)
                                            cuser.append(rsession)

                                    if '"description":"The conversation has expired, please log in again"' in req1:
                                        if rsession not in cuser:
                                            cmb(None, f'This SessionID Has Expired !  \nSid : {rsession}',
                                                '@Ajarmah TikTok Claimer')
                                            Lsessions.remove(rsession)
                                            cuser.append(rsession)

                                    if '"description":"Too many attempts. Try again later."' in req1:
                                        pass

                                except:
                                    pass
                            else:
                                err += 1
                            before = att
                            sleep(1)
                            RS = att - before
                            sss(f'Ok : {"{:,}".format(reqs)}  |  Bad - ErrorProxy : {"{:,}".format(err)}  |  R\S : {"{:,}".format(RS)}  |  SIDs : {len(Lsessions)}')

                        except requests.exceptions.ConnectionError:
                            err +=1
                        except requests.exceptions.ReadTimeout:
                            err +=1
                        except requests.exceptions.ChunkedEncodingError:
                            err +=1
                        except IndexError:
                            pass


                for i in range(thr):
                    thread1 = threading.Thread(target=Claim_us)
                    thread1.daemon = True
                    thread1.start()
                    threads.append(thread1)
                for thread2 in threads:
                    thread2.join()



        except FileNotFoundError:
            print('Please Write Proxy File Name Correct In Settings File')
            input('')
            exit(0)
    elif proxy_type == 'socks4':
        try:
            proxy_file = open(proxy_list).read().splitlines()
            for prox in proxy_file:
                Lproxies.append(prox)
            if len(Lproxies) == 0:
                print(f'Proxies File Is Empty ! > {proxy_list}')
                input('')
                exit(0)
            elif len(Lproxies) >= 1:
                # print(f'{GREEN}[{RESET}+{GREEN}] Successfully Loaded :\n\t{GREEN}[{RESET}{len(Lusers)}{GREEN}] List Count\n\t{GREEN}[{RESET}{len(Lproxies)}{GREEN}] Proxies Count\n\t{GREEN}[{RESET}{len(Lsessions)}{GREEN}] Sessions Count')
                # input('')
                def Claim_us():
                    global att, reqs, err
                    while True:
                        runn = str(random.choice(Lproxies))
                        DWH = DiscordWebhook(url='https://discord.com/api/webhooks/')
                        DWH2 = DiscordWebhook(url=Dis_Webhook)
                        EMK = DiscordEmbed(title=f"Catched > @{target}\n""Requests > {:,}".format(att),
                                           description='Coded by @Ajarmah\n\n@Ajarmah - @_vt.done',
                                           color=14681863)
                        EMK.set_thumbnail(url='https://imgur.com/m6lYzYC.gif')
                        DWH.add_embed(EMK)
                        DWH2.add_embed(EMK)
                        try:
                            rsession = random.choice(Lsessions)
                        except IndexError:
                            threading.Lock()
                            pass
                        try:
                            PROXYY = {
                                'http': 'socks4://{}'.format(runn),
                                'https': 'socks4://{}'.format(runn)
                            }
                            url = f'https://www.tiktok.com/@{target}'
                            url1 = 'https://api16-normal-c-alisg.tiktokv.com/passport/login_name/update/?iid=7060509952591595266&device_id=7054537563859764742&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=230005&version_name=23.0.5&device_platform=android&ab_version=23.0.5&ssmix=a&device_type=SM-N975F&device_brand=samsung&language=en&os_api=25&os_version=7.1.2&openudid=a0fa5ae7590c6576&manifest_version_code=2022300050&resolution=1600*900&dpi=300&update_version_code=2022300050&_rticket=1644335649391&current_region=JO&app_type=normal&sys_region=US&mcc_mnc=41601&timezone_name=America%2FChicago&residence=JO&ts=1644335648&timezone_offset=-21600&build_number=23.0.5&region=US&uoo=0&app_language=en&carrier_region=JO&locale=en&op_region=JO&ac2=wifi&host_abi=x86&cdid=63d7e01e-5508-4742-ad36-df84088dcef8&support_webview=1&okhttp_version=4.1.73.9-tiktok'
                            url2 = 'https://api16-normal-c-alisg.tiktokv.com/aweme/v1/commit/user/?iid=7053806752974882566&device_id=6994798204819621382&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=220804&version_name=22.8.4&device_platform=android&ab_version=22.8.4&ssmix=a&device_type=SM-N975F&device_brand=samsung&language=en&os_api=25&os_version=7.1.2&openudid=c1d415ad940052b3&manifest_version_code=2022208040&resolution=720*1280&dpi=240&update_version_code=2022208040&_rticket=1642346163746&current_region=JO&app_type=normal&sys_region=US&mcc_mnc=41603&timezone_name=Asia%2FShanghai&residence=JO&ts=1642346163&timezone_offset=28800&build_number=22.8.4&region=US&uoo=1&app_language=en&carrier_region=JO&locale=en&op_region=JO&ac2=wifi&host_abi=x86&cdid=b2d439e0-8d34-45ee-b889-3f94c2882af2'

                            headers = {
                                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76'
                            }

                            headers1 = {
                                'accept-encoding': 'gzip',
                                'connection': 'Keep-Alive',
                                'content-length': '61',
                                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                'cookie': f'store-idc=alisg; store-country-code=jo; passport_csrf_token=4f090f6c688d34439023d87c94284d56; passport_csrf_token_default=4f090f6c688d34439023d87c94284d56; d_ticket=1a360b478360784d60e9c19bab2975d299648; multi_sids=7053658438690620417%3A{rsession}; cmpl_token=AgQQAPOlF-RPsLHdTl3tJZ04-3Ma2-5Pf4QuYMIzrw; odin_tt=d62f0efc196a8d93560631a047a87752c12f5ddfe33609a464231b966571be6fb2ff3fe1ba12167eceb59eb2dd3132d2bfec5cbae962019f47d62fa73b1768bed92d4c701d38b567cbf2bb9573a96c20; sid_guard={rsession}%7C1642342749%7C5183999%7CThu%2C+17-Mar-2022+14%3A19%3A08+GMT; uid_tt=ce5c1917610acacc9ac99631c4e012316730e233d63a978a93413f7a09985b49; uid_tt_ss=ce5c1917610acacc9ac99631c4e012316730e233d63a978a93413f7a09985b49; sid_tt={rsession}; ; sessionid_ss={rsession}',
                                'passport-sdk-version': '19',
                                'x-gorgon': '040400d140002934b0b8bc7150ef56d1363224801d3c99ce90c3',
                                'user-agent': 'com.zhiliaoapp.musically/2022208040 (Linux; U; Android 7.1.2; en; SM-N975F; Build/N2G48H;tt-ok/3.10.0.2)'
                            }
                            data_signature = f'signature={Cus_Bio}'
                            data_nickname = f"nickname={name}"
                            data_username = f'login_name={target}&page_from=0'
                            req = \
                            requests.get(url, headers=headers, proxies=PROXYY).text.split('"preloadList":[]}}')[1].split(
                                '"I18n"')[0]
                            # print(req)
                            att += 1
                            if '{"followerCount":' in req or req == ',"UserPage":{"statusCode":10221},' or req == ',"UserPage":{"statusCode":10223},' or req == ',"UserPage":{"statusCode":10225},' or req == ',"UserPage":{"statusCode":10101},':
                                reqs += 1
                            elif req == ',"UserPage":{"statusCode":10202},':
                                try:
                                    req1 = requests.post(url1, headers=headers1, data=data_username,
                                                         proxies=PROXYY).text
                                    # print(req1)
                                    if target not in cuser:
                                        if f'"message":"success"' in req1 or req1 == f'"Login_name":"{target}"':
                                            print(
                                                f'\r{RED}[{RESET}{target}{RED}] Catched ;)\n{RED}[{RESET}{rsession}{RED}] SessionID\n\n',
                                                end='')
                                            requests.post(url2, headers=headers1, data=data_signature).text
                                            requests.post(url2, headers=headers1, data=data_nickname).text
                                            DWH.execute()
                                            DWH2.execute()
                                            with open(f'@{target} Info.txt', 'a') as xx:
                                                xx.write(f'Username : {target}\nSessionID : {rsession}')
                                            Lsessions.remove(rsession)
                                            cuser.append(target)
                                            cmb(None,
                                                f'Catched > {target}  \nAttemps : {"{:,}".format(att)}',
                                                '@Ajarmah TikTok Claimer')

                                    if '"description":"login name can only be updated once within one month."' in req1:
                                        if rsession not in cuser:
                                            print(f'\r{RED}This Session Has 1 month Limit >>> SID : {rsession}{RESET}',
                                                  end='')
                                            Lsessions.remove(rsession)
                                            cuser.append(rsession)

                                    if '"description":"The conversation has expired, please log in again"' in req1:
                                        if rsession not in cuser:
                                            cmb(None, f'This SessionID Has Expired !  \nSid : {rsession}',
                                                '@Ajarmah TikTok Claimer')
                                            Lsessions.remove(rsession)
                                            cuser.append(rsession)

                                    if '"description":"Too many attempts. Try again later."' in req1:
                                        pass

                                except:
                                    pass
                            else:
                                err += 1
                            before = att
                            sleep(1)
                            RS = att - before
                            sss(f'Ok : {"{:,}".format(reqs)}  |  Bad - ErrorProxy : {"{:,}".format(err)}  |  R\S : {"{:,}".format(RS)}  |  SIDs : {len(Lsessions)}')

                        except requests.exceptions.ConnectionError:
                            err +=1
                        except requests.exceptions.ReadTimeout:
                            err +=1
                        except requests.exceptions.ChunkedEncodingError:
                            err +=1
                        except IndexError:
                            err +=1


                for i in range(thr):
                    thread1 = threading.Thread(target=Claim_us)
                    thread1.daemon = True
                    thread1.start()
                    threads.append(thread1)
                for thread2 in threads:
                    thread2.join()

        except FileNotFoundError:
            print('Please Write Proxy File Name Correct In Settings File')
            input('')
            exit(0)

else:
    print(f'\n\t{RED} Please Choose !!!!')
    input('')
    exit(0)
