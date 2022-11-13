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
If any help in needed, you can vist me on Scratch or Replit or even here on Github.




# Installation:

os.system("pip install ScratchServe")

import ScratchServe as scratch

# Create a Connection:
This feature is used to log-in.

**Without Cookie:**
scratch = scratch.connect("username", "password")

**With Cookie(this can be found in your browsers cookie or using the session_id attribute):** 
 
 scratch = scratch.connect("session_id") 

Attributes:

scratch.session

scratch.xtoken

scratch.email

scratch.status

# Cloud Vars:
This feature is used to interact with cloud vars.

conn = scratch.connect_cloud("project_id)


conn.set_var("Name", "Value")

conn.get_var("Name")

conn.logs()

conn.delete_var("Name")

conn.create_var("Name", "Value")


# Use Images:
This feature is used to retrieve images.

img = scratch.img("URL", "Color Type. Example: RGBA, RGB, Hex, Base64, ect.")



# Data:
This feature is used to get data.

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

user.stats()

user.ranks()

user.followers_over_time()

**Project**










































































































































































































































# Scratch Actions:
This feature is used to set data on Scratch.









































































































































































# Cloud Events:
This is used to respod to cloud var changes.







































# Cloud Requests:



























# Cloud DB:
This feature is used to create a DB for your Scratch project.


scratch.db("project id")

scratch.dbstart()

scratch.dbstop()




# Codes:
This feature is used to encode and decode text. The Scratch version is available on my profile.
https://scratch.mit.edu/projects/686710217/

**Example:**

var_name = scratch.encode("text")

var_name = scratch.decode("text")

var_name = scratch.encode_list("text)

var_name = scratch.decode_list("text")



Make sure to use it properly or else it will return an error. There is no point in encoding text before setting a cloud var because it is built into the function.



# The End
I hope you enjoyed this presentation and found it useful!

Any bugs?

Please report them!

Contact me on Repl or Scratch, or even here with the username @coolcoder1213.

https://scratch.mit.edu/users/coolcoder1213/

https://replit.com/@coolcoder1213

https://github.com/coolcoder1213


**Credits:**
A big thanks to @ScratchTheCoder12345, @Air_heads, @TheCloudDev, @Sid72020123, and many others for teaching me Python.
@NFlex23 for Aviate.
@DatOneLefty for ScratchDB.
And almost everything else done by @coolcoder1213.
