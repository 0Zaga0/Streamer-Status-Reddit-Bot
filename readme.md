This Reddit bot will check the status of Azubu/Twitch streamers, and update a subreddit's sidebar to show whether or not the  streamers are online.

By utilizing subreddit CSS, the streamers' statuses can also be moved to the subreddit's header
<img src="http://i.imgur.com/YVBgMYv.png">

<hr>

You must edit your subreddit's settings and add
> \[\]\(#\<streamer name>_twitch_offline\)

OR
> \[\]\(#\<streamer name>_azubu_offline\)

to the sidebar wherever you would like the streamer's status to be displayed.  Don't forget to replace <streamer name> with the name of the streamer you would like status updates for.  Also, Azubu is case senstitive when it comes to looking up names, so make sure that your capitalization is correct.

The *#\<streamer name>_twitch_offline* and *#\<streamer name>_azubu_offline* hashes will change to *#\<streamer name>_twitch_online* and *#\<streamer name>_azubu_online* hashes respectively, to indictate the status of the stream.  When a streamer is online, the hash will be at the end of the stream link (e.g. http://www.twitch.tv/TSM_WildTurtle#TSM_WildTurtle_twitch_online).
