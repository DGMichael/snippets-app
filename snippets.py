
import logging
import csv
import argparse
import sys

#set the log output file and the log level:
logging.basicConfig(filename = "output.log", level=logging.DEBUG)

def make_parser():
    "Construct the command line parser"
    logging.info("Constructing parser")
    description = "Store and retrieve snippets of text"
    parser = argparse.ArgumentParser(description = description)
    subparsers = parser.add_subparsers(dest = "command", help = "Available commands")
    
    #Subparser for the put command
    logging.debug("Constructing put parser")
    put_parser = subparsers.add_parser("put", help = "Store a snippet")
    put_parser.add_argument("name", help = "The name of a snippet")
    put_parser.add_argument("snippet", help = "The snippet text")
    put_parser.add_argument("filename", default = "snippets.csv", nargs = "?", help = "The snippet filename")

    #Subparser for the get command:
    logging.debug("Constructing get parser")
    get_parser = subparsers.add_parser("get", help = "Retrieve a snippet")
    get_parser.add_argument("name", help = "The name of a snippet")
    get_parser.add_argument("filename", default = "snippets.csv", nargs = "?", help = "The snippet filename")

    return parser

def get(name, filename):
    "Print a snippet stored in the csv"
    logging.info("Asked to get {!r} from {!r}".format(name, filename))
    logging.debug("Opening file")
    #Open file, generate reader object:
    with open(filename,'rb') as file_obj:
        reader = csv.reader(file_obj)
        lineDict = {}
        for line in reader:
            key = line[0]
            value = line[1]
            lineDict[key] = value
    #Generate return:
    if name not in lineDict.keys():
        return False
    else:
        return name, lineDict[name]

def put(name, snippet, filename):
    "Store a snippet with an associated name in the CSV"
    logging.info("Writing {!r}:{!r} to {!r}".format(name, snippet, filename))
    logging.debug("Opening file")
    with open(filename, "a") as f:
        writer = csv.writer(f)
        logging.debug("Writting snippet to file")
        writer.writerow([name,snippet])
    logging.debug("Write successful")
    return name , snippet

def main():
    "Main function"
    logging.info("Starting Snippets")
    parser = make_parser()
    arguments = parser.parse_args(sys.argv[1:])
    #Convert parsed args from namespace to dict:
    arguments = vars(arguments)
    command = arguments.pop("command")

    if command == "put":
        name, snippet = put(**arguments)
        print "Stored {!r} as {!r}".format(snippet, name)

    if command == "get":
        get_return = get(**arguments)
        if get_return == False:
            print "Input not found in file"
        else:
            print "The query {!r} returned {!r}".format(get_return[0], get_return[1])

if __name__ == "__main__":
    main()




