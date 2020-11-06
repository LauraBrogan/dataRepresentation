import requests
import json


f = open("carviewer2.html", "r")
html = f.read()
#print (html)
apiKey = 'c7adca01d62fd0d9a8bbd07e88724a708a06b17f'
url = 'https://api.html2pdf.app/v1/generate'
data = {'html': html,'apiKey': apiKey}
response = requests.post(url, json=data)
#print (response.status_code)
newFile = open("lab06.02.01.htmlaspdf.pdf", "wb")
newFile.write(response.content)
