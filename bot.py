import requests
import json
import time


class bot:
    def __init__(self):
        self.numberOfTweets = 0
        self.latestTweetFromPrevious = ''
        self.fileTypeDict = {}
        self.initializeFileType()
        self.time_seconds = 0
        self.economydict = {"NFT":0, "DEFI":0, "METAVERSE":0, "POLKADOT":0, "Storage":0, "VR/AR":0}

    def initializeFileType(self):  # Define file types for each file
        self.fileTypeDict["THETA"] = "NFT"
        self.fileTypeDict["XTZ"] = "NFT"
        self.fileTypeDict["CHZ"] = "NFT"
        self.fileTypeDict["ENJ"] = "NFT"
        self.fileTypeDict["ALICE"] = "NFT"

        self.fileTypeDict["AVAX"] = "DEFI"
        self.fileTypeDict["LUNA"] = "DEFI"
        self.fileTypeDict["LINK"] = "DEFI"
        self.fileTypeDict["UNI"] = "DEFI"
        self.fileTypeDict["FTM"] = "DEFI"
        self.fileTypeDict["XTZ"] = "DEFI"
        self.fileTypeDict["GRT"] = "DEFI"
        self.fileTypeDict["CAKE"] = "DEFI"


        self.fileTypeDict["AXS"] = "METAVERSE"
        self.fileTypeDict["MANA"] = "METAVERSE"
        self.fileTypeDict["SAND"] = "METAVERSE"
        self.fileTypeDict["ENJ"] = "METAVERSE"
        self.fileTypeDict["WAXP"] = "METAVERSE"
        self.fileTypeDict["CHR"] = "METAVERSE"
        self.fileTypeDict["CEEK"] = "METAVERSE"


        self.fileTypeDict["KSM"] = "POLKADOT"
        self.fileTypeDict["COMP"] = "POLKADOT"
        self.fileTypeDict["ANKR"] = "POLKADOT"
        self.fileTypeDict["ZRX"] = "POLKADOT"
        self.fileTypeDict["ONT"] = "POLKADOT"
        self.fileTypeDict["MOVR"] = "POLKADOT"

        self.fileTypeDict["FIL"] = "Storage"
        self.fileTypeDict["BTT"] = "Storage"
        self.fileTypeDict["HOT"] = "Storage"
        self.fileTypeDict["AR"] = "Storage"
        self.fileTypeDict["SC"] = "Storage"

        self.fileTypeDict["CEEK"] = "VR/AR"
        self.fileTypeDict["WILD"] = "VR/AR"
        self.fileTypeDict["REVO"] = "VR/AR"


    def loop(self):
        start_time = time.time()
        tweets = self.getTweets()
        #print(tweets)
        
        #print(self.latestTweetFromPrevious)
        for i in range(100):
            #print(tweets['data'][i]['text'])
            #print(i)
            if tweets['data'][i]['text'] == self.latestTweetFromPrevious: #breaks loop before repeat tweets
                break
            self.checkTweet(tweets['data'][i]['text'])

        self.latestTweetFromPrevious = tweets['data'][0]['text']
        print(self.economydict)
        self.time_seconds += 10
        while((time.time() - start_time) <= self.time_seconds):
            pass

    def checkTweet(self, tweet):
        #print(1)
        #print(tweet.split())
        tweet_list = tweet.split()
        #print(tweet_list)
        for word in tweet_list:
            #print(word)
            if word[0] == '$' or word[0] == '@' or word[0] == '#':
                word = word[1:]
                #print(word)
            elif word[0] == '(' and word[-1] == ')':
                word = word[1:-2]
            word.upper()
            economy = self.getFileType(word)
            if economy is not None:
                self.economydict[economy] = self.economydict.get(economy) + 1

    def getFileType(self, word):
        #add some sort of loose string matching
        if word in self.fileTypeDict:
            return self.fileTypeDict[word]
        return None

    def getTweets(self): 
        url = "https://api.twitter.com/2/tweets/search/recent?query=crypto&max_results=100"

        payload={}
        headers = {
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAE6OVwEAAAAAqn%2BjqKjq%2FwEP9%2F2HhoIk4H3x1Lo%3D0EyYvzqBwNvHmzeVSDU7J51smztAumPb1abYCmPvAtqEpKWv6h',
        'Cookie': 'guest_id=v1%3A163714639329327069; personalization_id="v1_nuDZwhk7xtxnh6cwX5/4qg=="'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        tweets = json.loads(response.text)

        return tweets

if __name__ == '__main__':
    botParser = bot()
    start_time = time.time()
    while(True):
        botParser.loop()
        print("--- %s seconds ---" % (time.time() - start_time))