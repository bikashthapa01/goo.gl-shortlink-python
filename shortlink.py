import requests,json


def shortIt(url):
	post = 'https://www.googleapis.com/urlshortener/v1/url?key=AIzaSyC1fMUu8Hg47XDDwpqwXAUkdDISLn1nlBM'
	longUrl = {'longUrl':url}
	headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",'content-type':'application/json'}
	shortUrl = requests.post(post,data=json.dumps(longUrl),headers=headers)
	jData =  json.loads(shortUrl.text)
	goUrl = jData.get('id')
	return goUrl


if __name__ == '__main__':
	Url = input("Enter Url:")
	shortUrl = shortIt(Url)
	print(shortUrl)