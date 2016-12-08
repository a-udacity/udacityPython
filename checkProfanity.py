import urllib


def read_file():
    contents = read_contents_of()
    response = check_profanity(contents)
    print_response(response)


def read_contents_of(file_path="/Users/ahararwala/Downloads/movie_quotes.txt"):
    quotes = open(file_path)
    contents = quotes.read()
    quotes.close()
    return contents


def print_response(response):
    if response == "true":
        print "Alert Profanity found!!!!!"
    else:
        print "All clear."


def check_profanity(any_query):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + any_query)
    response = connection.read()
    connection.close()
    return response


read_file()
