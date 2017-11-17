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

current = f'''
sum: {current_summary}
temp: {current_temperature}
feels: {current_apparentTemperature}
humid: {current_humidity}
precipIntens: {current_precipIntensity}
precipProb: {current_precipProbability}
windMPH: {current_windSpeed}
windDir: {current_windGust}
cloud%: {current_cloudCover}
uv: {current_uvIndex}
vis: {current_visibility}
hour: {hourly_summary}
day: {daily_summary}
'''

# Get 24 instances of res['hourly']['data'] starting at 0400, format them, append to msg
def get_hourly(forecast):
	for i in range(len(res['hourly']['data']) - 45):
		hourData = res['hourly']['data'][i]
		unixTime = int(hourData['time'])
		hour_time = datetime.datetime.fromtimestamp (unixTime).strftime('%H:%M:%S %m-%d-%Y')
		hour_apparentTemperature = hourData['apparentTemperature']
		hour_windSpeed = hourData['windSpeed']
		hour_cloudCover = hourData['cloudCover']
		hour_precipIntensity = hourData['precipIntensity']
		hour_humidity = hourData['humidity']

		hourly = f'''
time: {hour_time}
feel: {hour_apparentTemperature}
windMPH: {hour_windSpeed}
cloud%: {hour_cloudCover}
precip: {hour_precipIntensity}
humid: {hour_humidity}
				'''
		forecast.append(hourly)
get_hourly(forecast)

msg = current + ''.join(forecast)
print(msg)

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
