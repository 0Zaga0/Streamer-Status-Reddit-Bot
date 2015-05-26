This Reddit bot will check the status of Azubu/Twitch streamers, and update a subreddit's sidebar to show whether or not the  streamers are online.

By utilizing subreddit CSS, the streamers' statuses can also be moved to the subreddit's header
<img src="http://i.imgur.com/YVBgMYv.png">

<hr>

You must edit your subreddit's settings and add
> \[\]\(#twitch_<streamer name>_offline\)

OR
> \[\]\(#azubu_<streamer name>_offline\)

to the sidebar wherever you would like the streamer's status to be displayed.  Don't forget to replace <streamer name> with the name of the streamer you would like status updates for.  Also, Azubu is case senstitive when it comes to looking up names, so make sure that your capitalization is correct.

The *#twitch_<streamer name>_offline* and *#azubu_<streamer name>_offline* hashes will change to *#twitch_<streamer name>_online* and *#azubu_<streamer name>_online* hashes respectively, to indictate the status of the stream.  When a streamer is online, the hash will be at the end of the stream link (e.g. http://www.twitch.tv/TSM_WildTurtle#twitch_online).
