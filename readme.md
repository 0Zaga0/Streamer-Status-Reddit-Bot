This Reddit bot will check the status of an Azubu or Twitch streamer, and update a subreddit's sidebar to show whether or not the specified streamer is online.

By utilizing subreddit CSS styling, the streamer's status can also be moved to the page's header
<img src="http://i.imgur.com/YVBgMYv.png">

<hr>

You must edit your subreddit's settings and add
> \[\]\(#twitch_offline\)

OR
> \[\]\(#azubu_offline\)

to the sidebar wherever you would like the streamer's status to be displayed.

The *#twitch_offline* and *#azubu_offline* hashes will change to *#twitch_online* and *#azubu_online* hashes respectively, to indictate the status of the stream.  When a streamer is online, the hash will still be at the end of the stream link (e.g. http://www.twitch.tv/TSM_WildTurtle#twitch_online).
