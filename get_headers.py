import requests


try:
    url = str(input('Enter a url (please specify http or https):  ')).lower()
    response = requests.get(url)
    print("\n", url, "\n")
    print(response, "\n")
    print(response.headers, "\n")
except:
    print("Error")
