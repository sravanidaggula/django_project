from django.shortcuts import render
# from django.db import application_testing
from django.http import HttpResponse
from .models import ApplicationTesting
# from django.db import ApplicationTesting
from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
# from .models import Role, RoleCategory
# from .forms import RoleForm
from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
# from accounts.models import Role
from django.contrib.auth. forms import UserCreationForm
from django.contrib.auth import get_user_model
import http,http.client,ssl,json,requests,time
import pymysql
from application.models import gateway_details,gateway

def test(request):
   users = ApplicationTesting.objects.all()
   print(users)
   print(request.method)
   if request.method == 'POST':
      print("ok")
      global username
      username = request.POST['username']
      password = request.POST['password']
      print(username,password)
      for user in users:
         print(user.name)
         print(user.password)
         if user.name == username and user.password==password:
            print("ok Login Success")
            # p = gateway_details(user=username)
            return redirect('testing/')
               
         else:
            print('invalid credentials')
            return redirect('login')
         
   return render(request, "login.html")
def serdrop(request,template = "selection.html"):
   print(request.method)
   if request.method == 'POST':
      print(request.POST.get("form_type"),"formtype")
      if request.POST.get("form_type") == 'formone':
         print("ok")
         global sersel
         sersel = request.POST['server']
         print(sersel,"server")
         conn = http.client.HTTPSConnection("carosag.me", context = ssl._create_unverified_context()) # Login Api Code Starts Here
         conn.request("POST", "/api/api_nwd_token.php?id=vsdf4t34t3tdfsgdfg5645645fgby56y5676655fggr4d5tre4fdg6&key=fdfgfdgfdgfdfgfd345345fghdgfh56ycdsf3rregrhj6geertraa77")
         res = conn.getresponse()
         data = (res.read())
         # print(data,"data")
         # input = "HMWSSB LNS SERVER"
         data_str = data.decode('utf-8')
         string_json = json.loads(data_str)
         for data in string_json['data1']:
               # print(data)
               global website
               sername = data['name']
               accesstoken = data['accesstoken']
               website = data['website']
         #     accesstoken = data['accesstoken']
               print(sername,"name")
               if sername == sersel:
                  break
         if sername == sersel:
            print(accesstoken)
            websel = website
            global bearer, head
            bearer = accesstoken
            head = {
               'Content-type': 'application/json',
               'Accept': 'text/plain',
               "Authorization": 'Bearer ' + bearer
            }
            gatway_info_get = requests.get(website+"/api/gateways?limit=" + "100000",  headers=head)
            # print(gatway_info_get)
            text_datagatway = gatway_info_get.text
            gatwayinfo = json.loads(text_datagatway)
            totalcount = gatwayinfo['totalCount']
            gatway_data = gatwayinfo["result"]
            
            gatway_array = [] # gatwaycation Stored array based on selected org
            for gatway in gatway_data:
               gatway_name = gatway["name"]
               gatway_org_id = gatway["organizationID"]
               gatway_array.append(gatway_name)
               print(gatway_name,"appli_name")
               
            return render(request, 'selection.html',{'sersel':sersel,'gatway_array':gatway_array})
      elif request.POST.get("form_type") == 'formtwo':
         # print("ok")
         gatesel = request.POST['gate']
         # print(gatesel,"gate")
         gatway_info_get = requests.get(website+"/api/gateways?limit=" + "100000",  headers=head)
         # print(gatway_info_get)
         text_datagatway = gatway_info_get.text
         gatwayinfo = json.loads(text_datagatway)
         totalcount = gatwayinfo['totalCount']
         gatway_data = gatwayinfo["result"]
         
         gatway_array = [] # gatwaycation Stored array based on selected org
         for gatway in gatway_data:
            # print(gatway)
            gatway_name = gatway["name"]
            gatway_org_id = gatway["organizationID"]
            gatway_array.append(gatway_name)
            # print(gatway_name,"appli_name")
            if gatesel == gatway_name:
               break
         if gatesel == gatway_name:
               
            loc = gatway['location']
            # print(loc)
            global latitude,longitude
            latitude = loc['latitude']
            longitude = loc['longitude']
            print(latitude,longitude)
            session = requests.Session()
            response = requests.get('http://api.weatherapi.com/v1/current.json?key=5a4594f592a64e8fbc194504221512%20&q='+str(latitude)+"%20"+str(longitude)+'&aqi=yes')
            # print('http://api.weatherapi.com/v1/current.json?key=5a4594f592a64e8fbc194504221512%20&q='+str(latitude)str(longitude)+'&aqi=yes')
            res = (response.content)
            # print(a,"a")
            res_json = json.loads(res)
            # print(b)
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
            # print(res_cur)
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
            # print(res_cur_last_updated_epoch)
            p = gateway_details(user=username,servername=sersel,org_id=gatway_org_id,latitude=latitude, gateway_name=gatway_name, longitude=longitude,loc_name=res_loc_name,loc_region=res_loc_region)
            p.save()
            print("p",p)
            # return redirect('weather/')
            return render(request, 'weather.html',{'gatesel':gatesel,'latitude':latitude,'longitude':longitude,'res_loc_name':res_loc_name,'res_loc_region':res_loc_region,
                              'res_loc_country':res_loc_country,'res_loc_tz_id':res_loc_tz_id,'res_loc_localtime':res_loc_localtime,'res_cur_temp_c':res_cur_temp_c,'res_cur_temp_f':res_cur_temp_f,
                              'res_cur_wind_mph':res_cur_wind_mph,'res_cur_wind_kph':res_cur_wind_kph})
          
        
   return render(request, 'selection.html')

