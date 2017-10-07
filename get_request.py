import json
import urllib
import urllib2
import re

ACCESS_TOKEN = "AQ1uygz9Qf9F9Kh2Y_scz75wItRnFIDlwlETv6ZDgT-pBKA8FQAAAAA"
BASE_API = "https://api.pinterest.com"
def get_request(path, params = None):
	if params: 
		params.update({'access_token': ACCESS_TOKEN})
	else:
		params = {'access_token': ACCESS_TOKEN}
	print params
	url = "%s%s?%s" % (BASE_API, path, urllib.urlencode(params))
	result = urllib2.urlopen(url)
	response_data = result.read()
	return json.loads(response_data)

def get_next_request(url):
	result = urllib2.urlopen(url)
	response_data = result.read()
	return json.loads(response_data)

def valid(word):
	check = 0
	if len(word) < 2:
		return None
	if len(word) >= 4 and word[:4] == "www.":
		return None
	if len(word) >= 7 and word[:7] == "http://":
		return None
	if len(word) >= 8 and word[:8] == "https://":
		return None 

	if not word[0].isalpha():
		word = word[1:]
	if not word[-1].isalpha():
		word = word[:-1]
	for i in range(len(word)):
		letter = word[i]
		if letter.isalpha():
			check += 1
	if check == len(word):
		return word
	return None

def get_all_pins(b_id):
	path = "/v1/boards/" + str(b_id) + "/pins/"
	board = get_request(path)
	pins = board["data"]
	pins_list = pins
	while len(pins) == 25:
		next_url = board["page"]["next"]
		board = get_next_request(next_url)
		pins = board["data"]
		for pin in pins:
			pins_list.append(pin)
	return pins_list

def top_n_words(board_id, top_N):
	words_dict = {}
	n_words = []
	if top_N == 0:
		return set([])
	pins = get_all_pins(board_id)
	for pin in pins:
		line = re.sub("[^a-zA-Z'-]+", " ", pin["note"]).split(" ")
		for word in line:
			w = valid(word.lower())
			if w != None:
				if w in words_dict:
					words_dict[w] += 1
				else:
					words_dict[w] = 1
	for word in words_dict:
		n_words.append((word, words_dict[word]))

	n_words = sorted(n_words, key = lambda x: x[1], reverse = True)

	if len(n_words) <= top_N:
		i = len(n_words)
	else:
		tie_count = n_words[top_N-1][1]
		i = top_N
		while i < len(n_words):
			if n_words[i][1] == tie_count:
				i += 1
			else:
				break
	return set(n_words[:i])

print top_n_words(785174584973334843, 7)