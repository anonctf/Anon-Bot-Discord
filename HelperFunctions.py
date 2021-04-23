import discord

# Quotes dictionary
quotes = {
    "anonbot": [
        "*ahem* How can help you?",
        "Very carefully, next question.",
        "Try HARDER.",
        "\\*Morpheus\\*: Red or Blue pill?",
        "The Matrix is real.",
        "I'm gonna make him an offer he can't refuse.",
        "I’ll be back.",
        "Frankly, my dear, I don't give a damn.",
        "Why so serious?",
        "Riddikulus.",
    ]
}

# Output for !help
HELP_DICT = {
    "!help": "Returns this message.",
    "!hello": "Returns Hello, <user>!",
    "!xkcd": "Returns a random xkcd comic from the official xkcd API",
    "!numfact": "Returns a fact about a number, use '!help numfact' for more info",
    "!ab": "Send random anon-bot quotes.",
}

# Output for !help <command>
CMD_DICT = {
    "!numfact <arg1> [arg2]": """
    <arg1> Options are listed below
        date : "Returns a history fact happened on a random date. [arg2 - month/day (eg. 7/29)]"
        year : "Returns a history fact happened on a random year. [arg2 - year (eg. 1700)"
        math : "Returns a random fact about a number. [arg2 - positive integer]
        """
}

# Embeds the help message accordingly to the supplied arguments
def HELP(cmd=''):
    if cmd == '':
        e = discord.Embed(title="Help Commands:", color=0x5ea340)
        for key, val in HELP_DICT.items():
            e.add_field(name=key, value=val, inline=False)
    else:
        e = discord.Embed(title=f"{cmd} command:", color=0x7ea340)
        cmd_keys = CMD_DICT.keys()
        for k in cmd_keys:
            if cmd in k:
                key = k
                val = CMD_DICT[key]
        e.add_field(name=k, value=val, inline=False)
        
    return e
