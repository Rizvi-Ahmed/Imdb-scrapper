import requests

api_url = 'http://www.omdbapi.com/?t='

#print(requests.get(url = 'http://www.omdbapi.com/?t=avengers&apikey=e651170a').content.decode("utf-8"))
def processtitle(apikey: str, title: str):
    searchkey = title.replace(' ' , '+')
    generatedlink = api_url + searchkey +'&type=movie' + '&apikey=' + apikey
    response = requests.get(url = generatedlink).json()
    return response


def gettitleinfo(response : dict):
    info = {}
    info['Title'] = response['Title']
    info['Year'] = response['Year']
    info['Genre'] = response['Genre']
    info['Director'] = response['Director']
    info['Writer'] = response['Writer']
    return info
