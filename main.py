import requests,json

latitude = 17.43928
longitude = 78.45168
session = requests.Session()
response = requests.get('http://api.weatherapi.com/v1/current.json?key=5a4594f592a64e8fbc194504221512%20&q='+str(latitude)+"%20"+str(longitude)+'&aqi=yes')
# print('http://api.weatherapi.com/v1/current.json?key=5a4594f592a64e8fbc194504221512%20&q='+str(latitude)str(longitude)+'&aqi=yes')
res = (response.content)
# print(a,"a")
res_json = json.loads(res)
print(res_json,"res_json")
res_loc = res_json['location']
res_loc_name = res_loc['name']
res_loc_region = res_loc['region']
res_loc_country = res_loc['country']
res_loc_lat = res_loc['lat']
res_loc_lon = res_loc['lon']
res_loc_tz_id = res_loc['tz_id']
res_loc_localtime_epoch = res_loc['localtime_epoch']
res_loc_localtime = res_loc['localtime']
# print(res_loc_name)
res_cur =res_json['current']
print(res_cur)
res_cur_last_updated_epoch = res_cur['last_updated_epoch']
res_cur_last_updated = res_cur['last_updated']
res_cur_temp_c = res_cur['temp_c']
res_cur_temp_f = res_cur['temp_f']
res_cur_is_day = res_cur['is_day']
res_cur_wind_mph = res_cur['wind_mph']
res_cur_wind_kph = res_cur['wind_kph']
res_cur_wind_degree = res_cur['wind_degree']
res_cur_wind_dir = res_cur['wind_dir']
res_cur_pressure_mb = res_cur['pressure_mb']
res_cur_pressure_in = res_cur['pressure_in']
res_cur_precip_mm = res_cur['precip_mm']
res_cur_precip_in = res_cur['precip_in']
res_cur_humidity = res_cur['humidity']
res_cur_cloud = res_cur['cloud']
res_cur_feelslike_c = res_cur['feelslike_c']
res_cur_feelslike_f = res_cur['feelslike_f']
res_cur_vis_km = res_cur['vis_km']
res_cur_vis_miles = res_cur['vis_miles']
res_cur_uv = res_cur['uv']
res_cur_gust_mph = res_cur['gust_mph']
res_cur_gust_kph = res_cur['gust_kph']

# print(res_cur_last_updated_epoch)
res_cond =res_cur['condition']
res_cond_text = res_cond['text']
res_cond_icon = res_cond['icon']
res_cond_code = res_cond['code']

res_air_quality = res_cur['air_quality']
res_air_quality_co = res_air_quality['co']
res_air_quality_no2 = res_air_quality['no2']
res_air_quality_o3 = res_air_quality['o3']
res_air_quality_so2 = res_air_quality['so2']
res_air_quality_pm2_5 = res_air_quality['pm2_5']
res_air_quality_pm10 = res_air_quality['pm10']
res_air_quality_us_epa_index = res_air_quality['us-epa-index']
res_air_quality_gb_defra_index = res_air_quality['gb-defra-index']
# print(current)
# wind_mph = b['wind_mph']
# air_quality = b['air_quality']
# condition= app_data['condition']
# print(app_data,current,condition)
# for i in b['location']:
#     c = i['name']
#     print(c)