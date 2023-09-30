# YouTube Trending List by Region

The following web app accesses YouTube's API to display trending videos by region. As of September, 2023, YouTube does not provide an easy method to view videos trending in different regions. The user must change their regional settings to view the trending list for a specific region. 

This web app was made with the goal of providing accessibility to the user for viewing trending lists by region. The web app currently displays the trending lists in the United States, Greece, and South Korea. However, its functionality can be extended to include other regions.

Flask was used to create the web app and the Python code can be seen in the main.py file. Bootstrap templates were also used to ease the UI design process, and can be viewed in the templates/layout.html file.

# To Run
To run this web app, Python3 must be installed. The following instructions is for a Linux OS, but the process should be similar for Windows, with a few minor changes.

A Python virtual environment is recommended to ensure there are no dependency conflicts.
```
python3 -m venv <environment_name>
```
After activating the environment, use the requirements.txt file to install the necessary dependencies. 
```
source <environment_name>/bin/activate
pip install -r requirements.txt
```
An API key will also be needed to authenticate the service. Instructions on how to create one can be found [here](https://blog.hubspot.com/website/how-to-get-youtube-api-key).
Set the environment variable to load the app, and then run it.
```
export FLASK_APP=main.py
flask run
```
Open a browser and type in the searchbar **localhost:5000** or **127.0.0.1:5000**. The web app will display the trending YouTube videos by region.

A screenshot of the trending videos in the US is displayed below.

![image](https://github.com/n-anna49/regional_youtube_trends_list/assets/105296323/1bbad8c6-296d-4e90-8ba9-a515cc8de706)
