import requests

def search_api(self, query):
 url = "https://cheapest-gpt-4-turbo-gpt-4-vision-chatgpt-openai-ai-api.p.rapidapi.com/v1/chat/completions"

 payload = {
	"messages": [
		{
			"role": "user",
			"content":{"query":query}
		}
	],
	"model": "gpt-4-turbo-preview",
	"max_tokens": 200,
	"temperature": 0.9
}
 headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "d19ccafbf7mshb20cf6f021509cfp1dc5d8jsn37542c4371bf",
	"X-RapidAPI-Host": "cheapest-gpt-4-turbo-gpt-4-vision-chatgpt-openai-ai-api.p.rapidapi.com"
  }
 response = requests.post(url, json=payload, headers=headers)
 return response.json()['response']