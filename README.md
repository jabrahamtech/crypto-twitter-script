# Twitter Crypto Trends Script

## Description

Script which finds daily crypto twitter trends

Two list are printed out every 15 minutes to CLI

First list - Set of ecosystems and the percentage at which they have been mentioned against one another since the script started + List of top 20 mentioned tickers and their percentage at which they have been mentioned.

Second list - Same lists at above but for 15 minute interval with number of tweets in the time period

This script uses ~10% of tweets as a sample size due to twitters developer portal api only allowing 500,000 tweet requests per month. This also requires the script to only be run 8 hours a day. Twitter peak hours are between 3am - 9am NZDT which is also when crypto activity surges. 

## Installation

Sign up for developer portal and get api bearer token.
Install the latest version of python 3.

### Postman
Replace python request in script with code snippet that can be generated in postman for python.
Create a get request using the same request in the script and add your authorization token, then go to code snippet select python- requests and paste the code into the bot. 

## Startup
type this in CLI

```shell
$ venv\Scripts\activate
$ python bot.py
```

This script is a POC and I take no responsibility for any finacial decisions made using this script.


