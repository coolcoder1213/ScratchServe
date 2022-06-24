# ScratchServe
Python API Wrapper for scratch.mit.edu

Connect to Scratch API and more!

Fetures:

Simple Cloud Code

Easy to Fetch Data

Scratch Actions

Cloud Requests

Cloud Events

Cloud DB

Encoder and Decoder

And much more!


NOTICE: Knowlage of the Python language is required to use this code.
If any help in needed, you can vist me on Scratch or Replit.




# Installation:

os.system("pip install ScratchServe")

import ScratchServe as scratch

# Create a Connection:

Without Cookie: scratch = scratch.connect("username", "password")

With Cookie: scratch = scratch.connect("session_id") #Returns the data on the login.


# Use Images:

scratch.img_setup("img_location")

img = scratch.img("URL", "Color Type. Example: RGBA, RGB, Hex, Base64, ect.")



# Data

**User:**

user = scratch.connect_user("username")

user.id()

user.status()

user.join_data()

user.message_count()

user.country()

user.about()

user.wiwo()

user.activity()

user.featured_data()

user.project_count()

user.projects()

user.favorite_count()

user.favorites()

user.studio_following_count()

user.studios_following()

user.studios_curating_count()

user.studios_curating()

user.profile_comments(limit=40, offset=0)

user.following_count()

user.following()

user.followers_count()

user.followers()



