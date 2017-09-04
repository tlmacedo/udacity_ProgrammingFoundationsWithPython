import urllib.parse
import urllib.request


def read_text():
    quotes = open(
        '/Volumes/100GB-Sistemas/udacity/ProgrammingFoundationsWithPython/Lesson5_Profanity Editor/movie_quotes.txt')
    contents_of_file = quotes.read()
    # print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)


def check_profanity(text_to_check):
    parametro = urllib.parse.urlencode([('q', text_to_check)])
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?" + parametro)
    output = str(connection.read())
    connection.close()

    if "true" in str(output):
        print("contém palavra imprópria!")
    elif "false" in str(output):
        print("verificação OK!!!")
    else:
        print("Could not scan the document properly")

    print(str(output))


read_text()
