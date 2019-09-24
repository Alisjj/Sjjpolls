from bs4 import BeautifulSoup
import requests

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=33.94251000000003&lon=-118.40896999999995#.XOnRqlL0nIU')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-body')

items = week.find_all(class_='tombstone-container')

period_names = [item.find(class_='period_name').get_text() for item in items]
short_descriptions = [item.find(class_='short_desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]

print(period_names)
print(short_descriptions)
print(temperatures)


