import sys
import wolframalpha

def main(messaging_text):
    client = wolframalpha.Client("V63VYX-EX865W38Y4")
    res = client.query(messaging_text)

    #count=0
    #for pod in res.pods:
        #if(count>=1):
            #break
    try:
        return next(res.results).text
    except StopIteration:
        print ("No results")



