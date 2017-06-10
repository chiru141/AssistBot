import sys
import wolframalpha

def main(messaging_text):
    client = wolframalpha.Client("V63VYX-EX865W38Y4")
    res = client.query(messaging_text)

    try:
        return next(res.results).text
    except StopIteration:
            print ("No results")
    except AttributeError:
            return "I have no answer"
		




