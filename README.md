# Reddit API (PRAW)

This python script is using the Reddit API (PRAW) in order to obtain the historical best 100 posts from the "/mechanicalkeyboards" subrreddit.

In this case, the obtained information for each post is:

* title: Retrieves the post's title.
* Score: This is the popularity score of the post. 
* id: An internal id that Reddit assigns to each post.
* comm_num: Retrieves the number of comments of each post.
* created: Retrieves the date in which each post was created. 
* body: Retrieves the body of each post. In this case is empty because the original posters don't write a body in their posts in this subrreddit.

The result is exported into a CSV file for easier manipulation. Other export formats can be HTML or a data frame, you could even send the results to your own database directly from python. The options are limitless. 

## Preview

![Preview](https://github.com/rmaciasc/api-connection/blob/master/praw.jpg)
