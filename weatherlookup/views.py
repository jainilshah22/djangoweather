from django.shortcuts import render

def home(request):
     import json
     import requests

     if request.method=="POST":
          zipcode= request.POST['zipcode']
          api_request = requests.get("https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode="+ zipcode + "&date=2024-04-19&distance=25&API_KEY=1F029D15-1628-40AD-B3F5-FC1583F7E047")
          
          try:
               api=json.loads(api_request.content)
          except Exception as e:
               api= "Error...."


          if api[0]['Category']['Name'] == "Good":
               category_description = "(0 - 50) Air Quality is Considered Satisfactory, and air pollution poses little or no risk."
               category_color ="good"

          elif api[0]['Category']['Name'] == "Moderate": 
               category_description = "(51 - 100) Air Quality is aceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are very sensitive to air pollution."
               category_color ="moderate"

          elif api[0]['Category']['Name']== "USG":
               category_description = "(101 - 50) Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and childern are at a greater risk from exposure to ozone, whereas person with heart and lung disease, older adults and childern are at greater risk from the presence of particals in the air"
               category_color ="usg"

          elif api[0]['Category']['Name'] == "Unhealthy": 
               category_description = "(151 -2 00) Everyone may begin to experience health effects; member of sensitive groups may experience more serious health effects."
               category_color ="unhealthy"

          elif api[0]['Category']['Name']== "Very Unhealthy": 
               category_description = "(201 - 300) Heath alert: everyone may experience more serious health effects."
               category_color ="veryunhealthy"

          elif api[0]['Category']['Name']== "Hazardous" :
               category_description = "(301 - 500) Heath warning of emergency conditions.The entire population is more likely to be affected."
               category_color ="hazardous"




          return render(request, 'home.html',{
               'api':api,
               'category_description':category_description, 
               'category_color':category_color  })


     else:
          api_request = requests.get("https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=20002&date=2024-04-19&distance=25&API_KEY=1F029D15-1628-40AD-B3F5-FC1583F7E047")
          
          try:
               api=json.loads(api_request.content)
          except Exception as e:
               api= "Error...."


          if api[0]['Category']['Name'] == "Good":
               category_description = "(0 - 50) Air Quality is Considered Satisfactory, and air pollution poses little or no risk."
               category_color ="good"

          elif api[0]['Category']['Name'] == "Moderate": 
               category_description = "(51 - 100) Air Quality is aceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are very sensitive to air pollution."
               category_color ="moderate"

          elif api[0]['Category']['Name']== "USG":
               category_description = "(101 - 50) Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and childern are at a greater risk from exposure to ozone, whereas person with heart and lung disease, older adults and childern are at greater risk from the presence of particals in the air"
               category_color ="usg"

          elif api[0]['Category']['Name'] == "Unhealthy": 
               category_description = "(151 -2 00) Everyone may begin to experience health effects; member of sensitive groups may experience more serious health effects."
               category_color ="unhealthy"

          elif api[0]['Category']['Name']== "Very Unhealthy": 
               category_description = "(201 - 300) Heath alert: everyone may experience more serious health effects."
               category_color ="veryunhealthy"

          elif api[0]['Category']['Name']== "Hazardous" :
               category_description = "(301 - 500) Heath warning of emergency conditions.The entire population is more likely to be affected."
               category_color ="hazardous"




          return render(request, 'home.html',{
               'api':api,
               'category_description':category_description, 
               'category_color':category_color  })

def about(request):
     return render(request, 'about.html',{})
