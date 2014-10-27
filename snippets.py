
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

    return parser


def put(name, snippet, filename):
    "Store a snippet with an associated name in the CSV"
    logging.info("Writing {!r}:{!r} to {!r}".format(name, snippet, filename))
    logging.debug("Opening file")
    with open(filename, "a") as f:
        writer = csv.writer(f)
        logging.debug("Writting snippet to file")
        writer.writerow([name,snippet])
    logging.debug("Write successful")
    return name, snippet

def main():
    "Main function"
    logging.info("Starting Snippets")
    parser = make_parser()
    arguments = parser.parse_args(sys.argv[1:])

if __name__ == "__main__":
    main()




