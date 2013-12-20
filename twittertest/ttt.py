import io
import json
import twitter

# XXX: Go to http://twitter.com/apps/new to create an app and get values
# for these credentials that you'll need to provide in place of these
# empty string values that are defined as placeholders.
#
# See https://vimeo.com/79220146 for a short video that steps you
# through this process
#
# See https://dev.twitter.com/docs/auth/oauth for more information 
# on Twitter's OAuth implementation.

CONSUMER_KEY = 'gsCdMBfJSC1HqZknKEtUw'
CONSUMER_SECRET = 'TMpWVl7xLLgVNuyliF3al34IUaI2e4WPjiBkZixkLJU'
OAUTH_TOKEN = '16111879-RtnKBPggXUrdXbG6M2YTlL3GF2eTIv5FlOJIlGjlj'
OAUTH_TOKEN_SECRET = 'Wib14o1g380JI7ZcbSAsjQuxPDnuQ9jqnq6PuDOiJh4nA'

# The keyword query

QUERY = 'bitcoin'

# The file to write output as newline-delimited JSON documents
OUT_FILE = QUERY + ".json"


# Authenticate to Twitter with OAuth

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

# Create a connection to the Streaming API

twitter_stream = twitter.TwitterStream(auth=auth)


print 'Filtering the public timeline for "{0}"'.format(QUERY)

# See https://dev.twitter.com/docs/streaming-apis on keyword parameters

stream = twitter_stream.statuses.filter(track=QUERY)

# Write one tweet per line as a JSON document. 

with io.open(OUT_FILE, 'w', encoding='utf-8', buffering=1) as f:
    for tweet in stream:
        f.write(unicode(u'{0}\n'.format(json.dumps(tweet, ensure_ascii=False))))
        print tweet['text']
