import requests 
import bs4
import csv

url = "https://yofreesamples.com/courses/free-discounted-udemy-courses-list/"
response = requests.get(url)

soup = bs4.BeautifulSoup(response.text, "html.parser")
lists = soup.find_all('div', 'col-xs-12 col-sm-9')

table = [['課程名稱', '優惠碼', '網址']]

for l in lists:
    table.append([l.p.text.split(": ")[1], l.a.get("href").rsplit('=', 1)[1], l.a.get("href")])

with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(table)