import requests
import json


class Youtubestats:

	def __init__(self, api_key, channel_id):
		self.api_key = api_key
		self.channel_id = channel_id
		self.channel_stats = None

	def get_channel_stats(self):
		url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={self.channel_id}&key={self.api_key}'

		json_url = requests.get(url)
		data = json.loads(json_url.text)

		try:
			data = data["items"][0]["statistics"]
		except:
			data = None

		self.channel_stats = data
		return data

	def dump_data(self):
		if self.channel_stats is None:
			return

		data_required = "data required"
		

		# generate a json file with all the statistics data of the youtube channel
		file_name = data_required + '.json'
		with open(file_name, 'w') as f:
			json.dump(self.channel_stats, f, indent=10)
		print('Data required has been file dumped')
