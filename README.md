# Lockdown Gifs

## Table of Contents

* [Overview](#overview)
* [Tech Stack](#tech-stack)
* [Features](#features)
* [Setup/Installation](#setup)
* [About the Developer](#developer)
 

## <a name="overview"></a>Overview
Beginning March 19, 2020, the state of California was ordered to stay at home on lockdown
until further notice due to Coronavirus. I decided to create a simple app that showed only 
coronavirus and lockdown related gifs for my own entertainment while sheltering in place.
This went hand in hand with my first project <a href="https://www.cocktailparty.fun/" target="_blank">Cocktail Party </a>. Since I can't go out for drinks and entertainment anymore, I've made a couple of sites that allowed me to still do both in the comfort of my own home!


## <a name="tech-stack"></a>Tech Stack
__Front End:__ HTML5, Jinja2, Bootstrap, CSS<br>
__Back End:__ Python, Flask<br>
__APIs:__ Giphy
<br/>

## <a name="features"></a>Features

Click left or right to scroll through Covid-19 lockdown related gifs:
<br><br>

<p align="center">
<img src="/static/videos/lockdown.gif">
<br/><br/>
 </p>


## <a name="setup"></a>Setup/Installation

### Prerequisites:

- Python3

### Run Lockdown Gifs on your local computer:

Clone repository:
```
$ git clone https://github.com/kqlam21/lockdown_gif.git
```
<br>

Create and activate a virtual environment inside your cocktail_party directory:
```
$ virtualenv env
$ source env/bin/activate
```
<br>

Install dependencies:
```
$ pip3 install -r requirements.txt
```
<br>

Get an API key from Giphy and save into a secrets.sh file as:
```
export GIPHY_KEY="3u0gEa5TJ6xjOFPbFBOsAVz3jOtOBj2d"
```
Make sure to include this file in your .gitignore
<br>

Execute your shell script: 
```
$ source secrets.sh
```
<br>

Run the app from the command line:
```
$ python3 server.py
```
<br>

Visit localhost:5000 on your browser to start clicking!
<br><br>

## <a name="developer"></a>About the Developer

Accountant-turned-developer, Kerry is a curious, collaborative problem solver always in pursuit of the most thoughtful and efficient solutions. 

Learn more about Kerry on her <a href="https://www.linkedin.com/in/kerrylam/" target="_blank">LinkedIn.</a>
