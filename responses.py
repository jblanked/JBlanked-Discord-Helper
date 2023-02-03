import random
import re
import string


def get_response(message: str):
    p_message = message.lower()

    if p_message == '!list':
        return "You can say any of these and I will reply: \n" +\
            " \n" +\
            "!x or y       for example: (!pizza or subway) \n" +\
            "-x and y      for example: (-2 and 1) \n" +\
            "+x and y      for example: (+2 and 1) \n" +\
            "*x and y      \n" +\
            " \n" +\
            "roll \n" +\
            "rollabc \n" +\
            " \n" +\
            "whats good \n" +\
            " \n" +\
            "who is the goat, whos the goat, how to be the goat, etc \n" +\
            " \n" +\
            "grand rising, good morning \n" +\
            " \n" +\
            "how do i get vip access, how do i get bot access \n" +\
            " \n" +\
            "what is the 10/90, how to get 10/90, etc \n" +\
            " \n" +\
            "what is the scam bot \n" +\
            " \n" +\
            "how to trade the scam alerts \n" +\
            " \n" +\
            "what is a funded account \n" +\
            " \n" +\
            "what is the 11:15 setup \n" +\
            " \n" +\
            "what is a trading plan"

    if re.search(r"whats good gang|what's good gang|whats up|whats good", p_message):
        return "What's the moves for today?"

    if p_message == 'roll':
        return str(random.choice(string.digits))

    if p_message == 'rollabc':
        return str(random.choice(string.ascii_lowercase))

    if re.search(r"who is the goat|whos the goat|who's the goat|who really is the goat|who's really the goat|who is the g.o.a.t|whos the g.o.a.t", p_message):
        return random.choice(["We are all the GOATS", "YOU are the GOAT", "Keith is the GOAT", "Noah is the GOAT"])

    if re.search(r"how do i become the goat|how can i be the goat|how can i be like you|how to become the goat|how do i be the goat|how to become the g.o.a.t", p_message):
        return random.choice(["Find your inner GOAT and become it", "YOU are the GOAT already family", "By being GOAT'd", "By improving yourself.. its you vs. you"])

    if p_message.startswith("!"):
        strip = p_message[1:].split(" or ")
        return random.choice(strip).capitalize()

    if p_message.startswith("+"):
        strip = p_message[1:].split(" and ")
        return sum([float(x) for x in strip])

    if p_message.startswith("-"):
        strip = p_message[1:].split(" and ")
        strip = [float(x) for x in strip]
        result = strip[0]
        for x in strip[1:]:
            result -= x
        return result

    if p_message.startswith("*"):
        strip = p_message[1:].split(" and ")
        strip = [float(x) for x in strip]
        result = strip[0]
        for x in strip[1:]:
            result *= x
        return result

    if p_message.startswith("!lotsize: "):
        strip = p_message[10:].split(" and ")
        strip = [float(x) for x in strip]
        result = strip[0]
        for x in strip[10:]:
            result *= x
        return result

    if re.search(r'grand rising scamily|great morning|good morning|morning gang', p_message):
        return "Great day!! Let's do it better than yesterday :grinning:"

    if p_message == '!help':
        return '`Not active yet.... but what could I help you with?`'

    if re.search(r"how do i get vip access|how do i get access to vip|where to get vip access|how to get vip access|how get vip access", p_message):
        return "For more info on VIP, click on the vip-access channel :point_right_tone3: https://discord.com/channels/851199573392883772/973354844637245470"

    if re.search(r"how do i get access to bots|bot access|where do i get the bots|how do i get the bots|how do i get the collinator|how do i get the order block beast|how do i get the jblanked juggler|where do i get the collinator|where do i get the order block beast|where do i get the jblanked juggler", p_message):
        return "DM JBlanked or checkout the bot-access channel :point_right_tone3: https://discord.com/channels/851199573392883772/1060289701954719764"

    if re.search(r"when hyenatron|where get hyenatron|what is the hyenatron|whats the hyenatron|how to get the hyenatron|when do we get the hyenatron|when will hyenatron be released|is hyenatron released|where is hyenatron", p_message):
        return "The HYENATRON is a multi-intelligence system with over 12+ profitable strategies. " +\
            " \n" +\
            "It is not released yet!! \n" +\
            " \n" +\
            "Please check out the vip-bot-info channel for more info :point_down_tone4: \n" +\
            "https://discord.com/channels/851199573392883772/1057369178555830383"

    if re.search(r"how do i get a funded account|how to get a funded account|where to get funded account|where do i sign up for a funded account| what is a funded account|how to join the funded account|where to join the funded account|where to join a funded account", p_message):
        return "More info about funded accounts at: \n" +\
            " \n" +\
            "https://myforexfunds.com/accounts/evaluation/ \n" +\
            " \n" +\
            "https://ftmo.com/en/faq/what-is-ftmo/ \n"

    if re.search(r"whats the 11:15|what is the 11:15|what's the 11:15|what is the 11 15 setup|whats the 11 15 setup", p_message):
        return "JBlanked's intraday setup! \n" +\
            " \n" +\
            "JBlanked gets the the strong data news outcome and trades it at the New York Peak"

    if re.search(r"what is 10 90|what the 10 90|what is the 10/90|whats 10/90|whats the 10/90|whats the 1090 setup|what the 90/10|what is ten ninety setup|what is the 10 ninety|what is the ten 90|setup the 10 90|setup the 90 10|where get the 10 90|where get the 90 10 setup|how get the 10 90 setup|about the 10 90 setup|explain the 10 90|settings for the 90 10|settings for the 10 90|question about the 90 10 setup", p_message):
        return "The 10/90 setup is a strategy created by our fellow mentor Keith Sweatte. \n" +\
            " \n" +\
            "It includes the MACD on a RSI window, and the Envelopes on a RSI window. \n" +\
            " \n" +\
            "Set two separate windows of the RSI with these settings:  \n" +\
            "Period = 8 \n" +\
            "Apply to Close \n" +\
            " \n" +\
            "Here are the MACD settings:  \n" +\
            "Fast EMA = 100 \n" +\
            "Slow EMA = 2 \n" +\
            "MACD SMA = 1 \n" +\
            "Applied to Weighted Close (HLCC/4) \n" +\
            "On the MACD's RSI, set the 10 level to 'Sell', and the 90 level to 'Buy' \n" +\
            " \n" +\
            "Here are the Envelopes settings: \n " +\
            "Period = 7 \n" +\
            "Shift = 0 \n" +\
            "Deviation = 0 \n" +\
            "Method = Simple \n" +\
            "Applied to Weighted Close (HLCC/4) \n" +\
            "On the MACD's RSI, set the 10 level to 'Buy', and the 90 level to 'Sell' "

    if re.search(r"whats a trading plan|what is a trading plan|how to make a trading plan|how to create a trading plan|how to select my trading plan|I need to create a trading plan|explain trading plan|creating a trading plan|advice on a trading plan|how to trading plan", p_message):
        return "A trading plan consist of a risk management strategy and psychology. \n" +\
            " \n" +\
            "Risk management involves: lot size/risk, stop loss, take profit, and an entry. \n" +\
            " \n" +\
            "Common stop losses are support/resistance lines, or beginning/ends of FVGs. \n" +\
            "The same can be said about take profits. \n" +\
            " \n" +\
            "Most entries are determined by technical indicators or news analysis. \n" +\
            " \n" +\
            "Psychology consists of greed, fear, and confidence. \n" +\
            "Fear leads to greed and greed leads to an ego. \n" +\
            " \n" +\
            "Confidence from research and experience eases fear and " +\
            "helps keep your emotions in check."
    if re.search(r"what is the scam bot|where to get the scam bot|explain the scam bot|what is scam bot|how to use the scam bot|where is scam bot|where is the scam bot|do we get the scam bot", p_message):
        return "The SCAM Bot currently sends alerts to the scam-alerts channel."
    if re.search(r"how to trade the scam alerts|how to use the scam alerts|explain the scam alerts|trading stategy scam alerts|best use the scam aleets|scam alert trading strategy", p_message):
        return "Best way to trade the SCAM alerts is by checking for two things: \n" +\
            " \n" +\
            "First thing is if it aligns with the intraday news or overall market tone. \n" +\
            "Second thing is to see if it is at a place where " +\
            "the market sold from or bought from before."
