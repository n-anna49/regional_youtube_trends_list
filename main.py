import os
import re
from googleapiclient.discovery import build
from flask import Flask, render_template, redirect
app = Flask(__name__) # __name__ is name of module to look for files

api = os.environ.get('YT_API_KEY')
service = build('youtube', 'v3', developerKey=api)

def parse_time(time):
    result = ""
    remove_pad = time.split('T')[1]
    if 'H' in remove_pad:
        result = remove_pad.split('H')[0] + ":"
        remove_pad = remove_pad.split('H')[1]
    if 'M' in remove_pad:
        if (len(remove_pad.split('M')[0]) == 2) or (len(result) < 1):
            result = result + remove_pad.split('M')[0] + ":"
        else:
            result = result + "0" + remove_pad.split('M')[0] + ":"
        remove_pad = remove_pad.split('M')[1]
    if 'S' in remove_pad:
        if len(remove_pad.split('S')[0]) == 2:
            result = result + remove_pad.split('S')[0]
        else:
            result = result + "0" + remove_pad.split('S')[0]
    if len(result) < 3:
        result = result + "s"
    return result

def parse_viewcount(views):
    views = int(views)
    if views > 999999:
        result = str(views // 1000000) + "M"
    elif views > 999:
        result = str(views // 1000) + "k"
    return result


def get_data(idx, region):
    if idx == 1:
        content_request = service.videos().list(part='contentDetails, snippet, statistics',
                                                chart='mostPopular', 
                                                regionCode=region, 
                                                maxResults=32)
        content_response = content_request.execute()
    elif idx == 2:
        content_request = service.videos().list(part='contentDetails, snippet, statistics',
                                                chart='mostPopular', 
                                                regionCode=region, 
                                                maxResults=32,
                                                videoCategoryId=10)
        content_response = content_request.execute()

    data = []
    number = 1
    for item in content_response['items']:
        res = 'maxres'
        id = item['id']
        title = f"#{number} {item['snippet']['title']}"
        num_val = f"#{number}"

        if 'maxres' not in item['snippet']['thumbnails']:
            res = 'standard'

        info = {
            'title': title,
            'url': f'https://www.youtube.com/watch?v={id}',
            'thumbnail': item['snippet']['thumbnails'][res]['url'],
            'channel': item['snippet']['channelTitle'],
            'duration': parse_time(item['contentDetails']['duration']),
            'views': parse_viewcount(item['statistics']['viewCount']),
            'number': num_val
        }
        number += 1
        data.append(info)
    
    return data

@app.route("/")
def home():
    return redirect("/trending/US")

@app.route("/trending/<region>")
def trending(region):
    data = get_data(1, region)
    header = f"Trending - {region}"
    return render_template('layout.html', data=data, header=header)

@app.route("/music/<region>")
def music(region):
    data = get_data(2, region)
    header = f"Trending Music - {region}"
    return render_template('layout.html', data=data, header=header)
    

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
