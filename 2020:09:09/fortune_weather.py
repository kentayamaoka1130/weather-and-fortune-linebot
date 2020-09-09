import requests
from bs4 import BeautifulSoup

def fortune_weather(a) :
    #weather
    def void(a) :
        k = a.span.string
        if k == "%" :
            return a.text
        else :
            return k


    #tenki.jpの目的の地域のページのURL（茨城県つくば市）
    URL = 'https://tenki.jp/forecast/3/11/4020/8220/'

    #HTTPリクエスト
    r1 = requests.get(URL)

    #プロキシ環境下の場合は以下を記述
    """
    proxies = {
        "http":"http://proxy.xxx.xxx.xxx:8080",
        "https":"http://proxy.xxx.xxx.xxx:8080"
    }
    r = requests.get(url, proxies=proxies)
    """

    #HTMLの解析
    bsObj1 = BeautifulSoup(r1.content, "html.parser")

    #今日の天気を取得
    today1 = bsObj1.find(class_="today-weather")
    weather = today1.p.string

    #気温情報のまとまり
    temp=today1.div.find(class_="date-value-wrap")

    #気温の取得
    temp=temp.find_all("dd")
    temp_max = temp[0].span.string #最高気温
    temp_max_diff=temp[1].string #最高気温の前日比
    temp_min = temp[2].span.string #最低気温
    temp_min_diff=temp[3].string #最低気温の前日比

    #降水時間
    raintime = today1.find(class_="precip-table")
    raintime = raintime.find_all("th")
    raintime = raintime[1:5]
    #降水確率
    rainp = today1.find(class_="rain-probability")
    rainp = rainp.find_all("td")

    #今日の日付
    time = today1.find(class_="left-style").text
    time = str(time)[3:]
    #結果の出力
    hizuke = str(time) + "\n"
    tenki = "天気 : " + str(weather) + "\n"
    saikou = "最高気温 : " + str(temp_max) + " " + str(temp_max_diff) + "\n"
    saitei = "最低気温 : " + str(temp_min) + " " + str(temp_min_diff) + "\n"
    zikanrain = ""

    quo = []
    for i in range(0,4) :
        zikanrain = zikanrain + "時間帯 : " + str(raintime[i].string) + "\n" 
        zikanrain = zikanrain + "降水確率 : " + str(void(rainp[i])) + "\n"
        if str(void(rainp[i]))[1] == "%" :
            quo.append(0)
        else :
            if str(void(rainp[i])) == "---" :
                quo.append(0)
            elif int(str(void(rainp[i]))[0:2]) >= 50 :
                quo.append(50)
            elif int(str(void(rainp[i]))[0:2]) >= 30 :
                quo.append(30)
            else :
                quo.append(0)
    if max(quo) >= 50 :
        pt = "今日は洗濯物は干さないほうが良いかも..."
    elif max(quo) >= 30 :
        pt = "洗濯物は自己責任だからね！！！"
    else :
        pt = "洗濯日和だよ〜〜！雨降ったらごめんね！！笑"

    kotae = "【天気予報】" + "\n" + hizuke + tenki + saikou + saitei + zikanrain
    kotae = kotae + "《洗濯情報》" + "\n" + pt
    if a == "no" or a == "NO" or a == "No" :
        return kotae
    else :
    #fortune
        Q = 0
        if a == '1' :
            url = 'https://fortune.yahoo.co.jp/12astro/aries'
        elif a == '2' :
            url = 'https://fortune.yahoo.co.jp/12astro/ariestaurus'
        elif a == '3' :
            url = 'https://fortune.yahoo.co.jp/12astro/gemini'
        elif a == '4' :
            url = 'https://fortune.yahoo.co.jp/12astro/cancer'
        elif a == '5' :
            url = 'https://fortune.yahoo.co.jp/12astro/leo'      
        elif a == '6' :
            url = 'https://fortune.yahoo.co.jp/12astro/virgo'
        elif a == '7' :
            url = 'https://fortune.yahoo.co.jp/12astro/libra'
        elif a == '8' :
            url = 'https://fortune.yahoo.co.jp/12astro/scorpio'
        elif a == '9' :
            url = 'https://fortune.yahoo.co.jp/12astro/sagittarius'
        elif a == '10' :
            url = 'https://fortune.yahoo.co.jp/12astro/capricorn'
        elif a == '11' :
            url = 'https://fortune.yahoo.co.jp/12astro/aquarius'
        elif a == '12' :
            url = 'https://fortune.yahoo.co.jp/12astro/pisces'
        else :
            hitsuzi = "1  : おひつじ座\n"
            ushi = "2  : おうし座\n"
            hutago = "3  : ふたご座\n"
            kani = "4  : かに座\n"
            shishi = "5  : しし座\n"
            otome = "6  : おとめ座\n"
            tenbin = "7  : てんびん座\n"
            sasori = "8  : さそり座\n"
            ite = "9  : いて座\n"
            yagi = "10 : やぎ座\n"
            mizugame = "11 : みずがめ座\n"
            uo = "12 : うお座\n"
            no = "no : 天気予報だけ表示するよ泣\n"
            gaide = "〜正座占いもできるよ〜\n【以下の番号を入力してね！】\n"
            ans = gaide + hitsuzi + ushi + hutago + kani + shishi + otome + tenbin + sasori + ite + yagi + mizugame + uo + no
            Q = 1

        if Q == 0 :
            #HTTPリクエスト
            r = requests.get(url)

            #HTMLの解析
            fortune = BeautifulSoup(r.content, "html.parser")

            #今日の占い
            today = fortune.find(class_="wr mg10t")
            kyou = str(today.p.string)
            kyou = kyou[5:]
            #print(kyou)

            #12正座占い
            otomeza = today.find("table")
            otomeza = str(otomeza.strong.text)
            for t in range(0,len(otomeza)) :
                if otomeza[t] == " " :
                    X = t
                    break
            otome = otomeza[X+1:]
            if otomeza[0:2] == "10" :
                number = otomeza[0:3]
            elif otomeza[0:2] == "11" :
                number = otomeza[0:3]
            elif otomeza[0:2] == "12" :
                number = otomeza[0:3]
            else :
                number = otomeza[0:2]
            otomeza_number = "{} : {}".format(otome,number)
            #print(number)
            #総合運
            unsei = today.find("table")
            unsei = unsei.find_all("td")
            un = unsei[1].find_all("img")
            #print(un)
            #name
            mono = today.find("table")
            mono = mono.find_all("a")
            mono = mono[1:5]

            #評価的な
            lang = fortune.find(class_="wr mg10a")
            lan = lang.dt.string
            lon = lang.dd.string
            lan = "《" + lan + "》" + "\n"
            lon = lon + "\n"
            lan = lan + lon + "\n" + "『おまじない』" + "\n"

            #評価的な2
            lang2 = fortune.find(class_="wr mg15t mg10h mg10b")
            lan2 = lang2.dd.string
            lan = lan + lan2

            ans = ""
            ans = "【あなたの運勢は!?】\n"
            #ans = ans + kyou + "\n"
            ans = ans + otomeza_number + "\n"
            P = 0
            for i in range(0,len(mono)) :
                if str(un[i])[17] == "=" :
                    P = 1
                if P == 0 :
                    if i == 0 :
                        k = str(un[i])
                        k = k[10:18]
                        j = str(mono[i].string)
                        ans = ans + j + " : " + k + "\n"
                    else :    
                        k = str(un[i])
                        j = str(mono[i].string)
                        k = k[10:16]
                        ans = ans + j + " : " + k + "\n"
                else :
                    if i == 0 :
                        k = str(un[i+1])
                        k = k[10:18]
                        j = str(mono[i].string)
                        ans = ans + j + " : " + k + "\n"
                    else :    
                        k = str(un[i+1])
                        j = str(mono[i].string)
                        k = k[10:16]
                        ans = ans + j + " : " + k + "\n"
            ans = kotae + "\n" + "\n" + ans + "\n" + lan
            return ans
        else :
            ans = kotae + "\n" + "\n" + ans + "君の順位は何位かな(@ ^ * ^ @)"
            return ans
