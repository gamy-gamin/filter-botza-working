class script(object):


    START_MSG = """ <b>Hi {}

You can call this as an Auto Filter Bot if you like :D

This is Version 2 of Auto Filter Bot

Bot gives button link to files in connected channels on query !

No need to add filters for your files or movies from now on!

For more click <i>help</i></b>"""


    HELP_MSG = """<b>How to use the bot??</b>

<i>
* Add bot to your group with admin rights.

* Add bot to channels which you want to link with <b>all admin rights</b>!
</i>


<b>Bot Commands - Works in Group only</b>
(You need to be a Auth User in order to use these commands)

* <code>/add channelid</code>  -  Links channel to your group.
or
* <code>/add @channelusername</code> - Links channel to your group.

<i>NOTE : You can get your channel ID from @ChannelidHEXbot </i>


* <code>/del channelid</code>  -  Delinks channel from group
or
* <code>/del @channelusername</code>  -  Delinks channel from group

<i>NOTE : You can get connected channel details by <code>/filterstats</code> </i>


* <code>/delall</code>  -  Removes all connected channels and filters from group!

<i>Note : Dont add command delete bots in group! Otherwise, delall command wont work</i>


* <code>/filterstats</code>  -  Check connected channels and number of filters.



No need add each filter again!
Bot will automatically search for your files and give links to that!


<b>© @TroJanzHEX</b>"""


    ABOUT_MSG = """⭕️<b>My Name : Auto Filter Bot V2</b>
    
⭕️<b>Creater :</b> @TroJanzHEX

⭕️<b>Language :</b> <code>Python3</code>

⭕️<b>Library :</b> <a href='https://docs.pyrogram.org/'>Pyrogram 1.0.7</a> 

⭕️<b>Tutorial Video :</b> <a href='https://youtu.be/KQVYQAOsFYY'>Video Link</a> 

"""
    
    USER_INCORRECT = """😊<b>එහෙමද... එහෙනම් හරි නම Group එකට දාන්න. මම Link එකක් දෙන්නම්....</b>"""
    ADMIN_MENTION = """😥 මම Adminව Mention කළා. එයා Online ආව ගමන් Link එකක් දෙයි...
#Request_Movie 
"""
    FOR_FORIGHN = """📌<b>The movie you want has not yet been added to my DB.\nPlease wait until the admin comes online.</b> \nWhen he/she comes online he/she gives a link❗️\n#Request_Movie #Foreign"""
    TEXT_AFTER_DONE = """<b>Admin ඔයාට Film එක දාල තියෙන්නෙ. ඔයාගෙ Msg එකට ආව Reply බලන්න</b>\n#Done"""
