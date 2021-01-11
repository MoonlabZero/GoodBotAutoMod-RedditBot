import praw
import time
import os

automod = 'AutoModerator'
me = 'GoodBotAutoMod'
sv = 'SaveVideo'


def bot_login():
    print("Logging In...")
    r = praw.Reddit(username = "GoodBotAutoMod",
            password = "",
            client_id = "",
            client_secret = "",
            user_agent = "Wi_Tarrd's Good Bot v0.8")
    print("Logged In!")

    return r

def run_bot(r, comments_replied_to):
    print("Obtaining Comments...")
    for comment in r.subreddit('memes').comments(limit=100):

        if "removed" in comment.body and comment.id not in comments_replied_to and comment.author == automod:
            #pass
            try:
                #print("Found AutoMod Removed " + comment.id)

                #comment.reply("Good Bot. \n\n*I am a bot, and this action was performed automatically. Please contact u\/Wi_Tarrd with issues regarding the bot.*")
                #print("Replied to AutoMod " + comment.id)

                comments_replied_to.append(comment.id)

                with open ("/home/WiTarrd/comments_replied_to.txt", "a") as f:
                    f.write(comment.id + "\n")
            except:
                print("Error")

        elif "u/savevideo" in comment.body and comment.id not in comments_replied_to and comment.author == automod:
            #pass
            try:
                #print("Found Automod else " + comment.id)
                #time.sleep(159.5)

                #comment.reply("Good B0t. \n\n*I am a bot, and this action was performed automatically. Please look at [this FAQ](https://github.com/MoonlabZero/GoodBotAutoMod-RedditBot/wiki) or contact u\/Wi_Tarrd with issues regarding the bot.*")
                #print("Replied to Automod else " + comment.id)

                comments_replied_to.append(comment.id)

                with open ("/home/WiTarrd/comments_replied_to.txt", "a") as f:
                    f.write(comment.id + "\n")
            except:
                print("Error")

        elif "u/savevideo" in comment.body and comment.id not in comments_replied_to and comment.author == sv:
            pass
            try:
                print("Found SaveVideo " + comment.id)
                time.sleep(150)
                comment.reply("Good Bots. \n\n*I am a bot, and this action was performed automatically. Please look at [this FAQ](https://github.com/MoonlabZero/GoodBotAutoMod-RedditBot/wiki/FAQ) or contact u\/Wi_Tarrd with issues regarding the bot.*")
                print("Replied to Automod else " + comment.id)

                comments_replied_to.append(comment.id)

                with open ("/home/WiTarrd/comments_replied_to.txt", "a") as f:
                    f.write(comment.id + "\n")
            except: print("Error")

        elif comment.id not in comments_replied_to and comment.author == automod:
            pass
            try:
                print("Found AutoMod " + comment.id)
                time.sleep(159.5)
                comment.reply("Good Bots. \n\n*I am a bot, and this action was performed automatically. Please look at [this FAQ](https://github.com/MoonlabZero/GoodBotAutoMod-RedditBot/wiki/FAQ) or contact u\/Wi_Tarrd with issues regarding the bot.*")
                print("Replied to Automod else " + comment.id)

                comments_replied_to.append(comment.id)

                with open ("/home/WiTarrd/comments_replied_to.txt", "a") as f:
                    f.write(comment.id + "\n")
            except: print("Error")

        elif "!gb faq" in comment.body and comment.id not in comments_replied_to and comment.author != me:
            try:
                print("Found Summons " + comment.id)
                comment.reply("[Hello.](https://github.com/MoonlabZero/GoodBotAutoMod-RedditBot/wiki/FAQ)")
                print("Replied to Summons " + comment.id)

                comments_replied_to.append(comment.id)

                with open ("/home/WiTarrd/comments_replied_to.txt", "a") as f:
                    f.write(comment.id + "\n")
            except: print("Error")


    #print(comments_replied_to)

    print("Sleeping for 10 Seconds")
    #Sleep for 10 Seconds
    time.sleep(10)

def get_saved_comments():
    if not os.path.isfile("/home/WiTarrd/comments_replied_to.txt"):
        comments_replied_to = []
    else:
        with open("/home/WiTarrd/comments_replied_to.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            comments_replied_to = filter(None, comments_replied_to)

        return comments_replied_to



r = bot_login()
comments_replied_to = []

while True:
    run_bot(r, comments_replied_to)
