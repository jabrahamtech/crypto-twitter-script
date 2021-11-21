import requests
import json
import time
from datetime import datetime
import math


class bot:
    def __init__(self):
        self.numberOfTweets = 0
        self.latestTweetFromPrevious = ''
        self.fileTypeDict = {}
        self.initializeFileType()
        self.economydict = {"NFT":0, "DEFI":0, "METAVERSE":0, "POLKADOT":0, "Storage":0, "VR/AR":0}
        self.quarter_economydict = {"NFT":0, "DEFI":0, "METAVERSE":0, "POLKADOT":0, "Storage":0, "VR/AR":0}
        self.tokendict = {}
        self.token_15mins_dict = {}
        self.time = datetime.now()
        self.start_time = self.time.strftime("%H:%M:%S")
        

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
        s_time = time.time()
        tweets = self.getTweets()
        #print(tweets)
        
        #print(self.latestTweetFromPrevious)
        for i in range(100):
            #print(tweets['data'][i]['text'])
            #print(i)
            try:
                if tweets['data'][i]['text'] == self.latestTweetFromPrevious: #breaks loop before repeat tweets
                    break
                self.checkTweet(tweets['data'][i]['text'])
            except IndexError:
                pass
        while((time.time() - s_time) <= 180):
            pass

    def checkTweet(self, tweet):
        #print(1)
        #print(tweet.split())
        tweet_list = tweet.split()
        #print(tweet_list)
        for word in tweet_list:
            #print(word)
            if word[0] == '@' or word[0] == '#':
                word = word[1:]
            elif word[0] == '$':
                word = word[1:]
                try:
                    float(word[:-1].replace(',', ''))    
                except ValueError:
                    if word != '': #deal with just $
                        self.tokendict[word.upper()] = self.tokendict.get(word.upper(), 0) +1
                        self.token_15mins_dict[word.upper()] = self.token_15mins_dict.get(word.upper(), 0) +1
                #print(word)
            elif word[0] == '(' and word[len(word)-1] == ')':
                #print('There was a )')
                word = word[1:len(word)-2]
            word.upper()
            economy = self.getFileType(word)
            if economy is not None:
                self.economydict[economy] = self.economydict.get(economy) + 1
                self.quarter_economydict[economy] = self.quarter_economydict.get(economy) + 1
        

    def getFileType(self, word):
        #add some sort of loose string matching
        if word in self.fileTypeDict:
            return self.fileTypeDict[word]
        return None

    def getTweets(self): 
        url = "https://api.twitter.com/2/tweets/search/recent?query=crypto&max_results=100"

        payload={}
        headers = {
        'Authorization': 'insert dev portal code here',
        'Cookie': 'insert cookie from postman here"'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        tweets = json.loads(response.text)

        return tweets

    def print_lists(self):
        print('Top Coins - Since ' + str(self.start_time))

        values = self.economydict.values()
        sum_eco = sum(values)
        economy_dict = self.economydict.copy()
        if sum_eco > 0:
            for key in economy_dict:
                value = economy_dict[key]
                value = (value/sum_eco) * 100
                economy_dict[key] = str(int(value)) + '%'
        print(economy_dict)

        values_token = self.tokendict.values()
        sum_token = sum(values_token)
        token_dict = self.tokendict.copy()
        for key in token_dict:
            value = token_dict[key]
            value = (value/sum_token) * 100
            token_dict[key] = int(value)

        sorted_token_list = sorted(token_dict.items(), key=lambda x: x[1], reverse=True)
        if len(sorted_token_list) >= 20:
            for i in range(20):
                print(str(sorted_token_list[i][0]) + ': ' + str(sorted_token_list[i][1]) + '%')
        print(' ')

    def print_15mins_list(self):
        print('Top Coins - Last 15 minutes')
        print(self.quarter_economydict)     
        sorted_15min_token_list = sorted(self.token_15mins_dict.items(), key=lambda x: x[1], reverse=True)
        if len(sorted_15min_token_list) >= 20:
            for i in range(20):
                print(sorted_15min_token_list[i])
        elif len(sorted_15min_token_list) >= 10:
            for i in range(10):
                print(sorted_15min_token_list[i])
        elif len(sorted_15min_token_list) >= 5:
            for i in range(5):
                print(sorted_15min_token_list[i])
        print(' ')
        self.token_15mins_dict = {}
        self.quarter_economydict = {"NFT":0, "DEFI":0, "METAVERSE":0, "POLKADOT":0, "Storage":0, "VR/AR":0}

if __name__ == '__main__':
    botParser = bot()
    start_time = time.time()
    #while((time.time() - start_time) < 28800):
    while(True):
        current_time = time.time()
        while((time.time() - current_time) < 900):
            #print((time.time() - current_time))
            botParser.loop()
        botParser.print_lists()
        botParser.print_15mins_list()
        #print("--- %s seconds ---" % (time.time() - start_time))
        
