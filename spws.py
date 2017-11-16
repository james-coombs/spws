import smtplib
import urllib.request
import json
import datetime
import configparser
import json

res = json.load(open('weather.json'))

forecast = []
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
current_precipIntensity = res['currently']['precipIntensity']
current_precipProbability = res['currently']['precipProbability']
hourly_summary = res['hourly']['summary']
daily_summary = res['daily']['summary']

msg = f'''
sum: {current_summary}\n
temp: {current_temperature}\n
feels: {current_apparentTemperature}\n
humid: {current_humidity}\n
precipIntens: {current_precipIntensity}\n
precipProb: {current_precipProbability}\n
windMPH: {current_windSpeed}\n
windDir: {current_windGust}\n
cloud%: {current_cloudCover}\n
uv: {current_uvIndex}\n
vis: {current_visibility}\n
hour: {hourly_summary}\n
day: {daily_summary}
'''
# print(msg)

# Get 24 instances of res['hourly']['data'] starting at 0400, format them, append to msg
def get_hourly(forecast):
	for i in range(0, len(res['hourly']['data']) - 45):
		hourData = res['hourly']['data'][i]
		unixTime = int(hourData['time'])
		hour_time = datetime.datetime.fromtimestamp (unixTime).strftime('%H:%M:%S %m-%d-%Y')
		hour_apparentTemperature = hourData['apparentTemperature']
		hour_windSpeed = hourData['windSpeed']
		hour_cloudCover = hourData['cloudCover']
		hour_precipIntensity = hourData['precipIntensity']
		hour_humidity = hourData['humidity']

		hourly = f'''
time: {hour_time} \n
feel: {hour_apparentTemperature} \n
windMPH: {hour_windSpeed} \n
cloud%: {hour_cloudCover} \n
precip: {hour_precipIntensity} \n
humid: {hour_humidity}
				'''
		forecast.append(hourly)

get_hourly(forecast)

print(forecast)
# def format_time():
# 	for hourData in res['hourly']['data']:
# 		unixTime = int(hourData['time'])
# 		stdTime = datetime.datetime.fromtimestamp (unixTime).strftime('%H:%M:%S %m-%d-%Y')
# 		print(stdTime)
# format_time()

# # create SMTP session
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
