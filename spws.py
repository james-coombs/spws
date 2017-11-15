import smtplib
import urllib.request
import json
import datetime
import configparser
import json

res = json.load(open('weather.json'))

# config = configparser.ConfigParser()
# confFile = 'creds_spws.ini'
# config = configparser.ConfigParser()
# config.read(confFile)
# dsKey = config['dark_sky']['key']

# # make req
# url = f'https://api.darksky.net/forecast/{dsKey}/42.3555,-71.0594'
# req = urllib.request.Request(url)

# # parse res
# req = urllib.request.urlopen(req).read()
# res = json.loads(req.decode('utf-8'))

# res data
current_time = datetime.datetime.fromtimestamp (res['currently']['time']).strftime('%H:%M:%S %m-%d-%Y')
current_summary = res['currently']['summary']
current_temperature = res['currently']['temperature']
current_apparentTemperature = res['currently']['apparentTemperature']
current_humidity = res['currently']['humidity']
current_windSpeed = res['currently']['windSpeed']
current_windGust = res['currently']['windGust']
current_cloudCover = res['currently']['cloudCover']
current_uvIndex = res['currently']['uvIndex']
current_visibility = res['currently']['visibility']
hourly_summary = res['hourly']['summary']
daily_summary = res['daily']['summary']

# format
msg = f'''
Summary: {current_summary}\n
Temp: {current_temperature}\n
Feels: {current_apparentTemperature}\n
Humidity: {current_humidity}\n
Wind MPH: {current_windSpeed}\n
Wind Dir: {current_windGust}\n
Cloud %: {current_cloudCover}\n
UVI: {current_uvIndex}\n
Vis: {current_visibility}\n
Hourly: {hourly_summary}\n
Daily: {daily_summary}
'''
# print(msg)

# create SMTP session
# server = smtplib.SMTP('smtp.gmail.com', 587)
# # server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

# fromAddr = f'{config[mail][fromAddr]}'
# toAddr = f'{config[mail][toAddr]}'
# # message to be sent
# body = msg

# # start TLS for security
# server.ehlo()
# server.starttls()

# # auth
# server.login(f'{config[mail][fromAddr]}', f'{config[mail][login]}')
# # send
# server.sendmail(fromAddr, toAddr, body)
# # terminate session
# server.quit()
