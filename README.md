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


# Cloud Vars:
conn = scratch.connect_cloud("project_id)


conn.set_var("Name", "Value")

conn.get_var("Name")

conn.logs()

conn.delete_var("Name")

conn.create_var("Name", "Value")


# Use Images:

scratch.img_setup("img_location")

img = scratch.img("URL", "Color Type. Example: RGBA, RGB, Hex, Base64, ect.")



# Data:

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






















































































# Scratch Actions:









































































































































































# Cloud Events:







































# Cloud Requests:



























# Cloud DB:












































# Codes:





























# The End
I hope you enjoyed this presentation and found it useful!

Any bugs?

Please report them!

Contact me on Repl or Scratch with the username @coolcoder1213.

https://scratch.mit.edu/users/coolcoder1213/

https://replit.com/@coolcoder1213


