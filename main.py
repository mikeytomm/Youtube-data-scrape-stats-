from youtube_statistics import Youtubestats

# paste the API key generated from google dev
API_KEY = "Please input your API KEY"

# paste the youtube channel id here
channel_id = "UCeG4S2vNfX94c1YeZwB1eXQ"

youtube_data = Youtubestats(API_KEY, channel_id)
youtube_data.get_channel_stats()
youtube_data.dump_data()
