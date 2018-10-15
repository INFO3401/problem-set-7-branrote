################################################################################
import csv
import string
from collections import Counter
from os import listdir
import os
import glob
import json
import sqlite3
# PART #1
################################################################################
# Worked with Michael and Aaron
def countWordsUnstructured(filename):
    # This function should count the words in an unstructured text document
    # Inputs: A file name (string)
    # Outputs: A dictionary with the counts for each word
    # +1 bonus point for removing punctuation from the wordcounts
    wordCounts = {}

    datafile = open(filename).read()

    data = datafile.split()

    for word in data:
        for mark in string.punctuation:
            word = word.replace(mark, "")
        if word in wordCounts:
            wordCounts[word] = wordCounts[word] + 1
        else:
            wordCounts[word] = 1

    return wordCounts
# Test your part 1 code below.
bush1989 = countWordsUnstructured("./Bush_1989.txt")
print (bush1989)
################################################################################
# PART 2
################################################################################

def generateSimpleCSV(targetfile, wordCounts):
    # This function should transform a dictionary containing word counts to a
    # CSV file. The first row of the CSV should be a header noting:
    # Word, Count
    # Inputs: A word count list and a name for the target file
    # Outputs: A new CSV file named targetfile containing the wordcount data
# Test your part 2 code below
    with open('1989.csv', 'w') as my_file:

        writer = csv.writer(my_file)
        writer.writerow(['Word', 'Count'])
        for key, value in bush1989.items():
            writer.writerow([key,value])

generateSimpleCSV('1989.csv', bush1989)
################################################################################
# PART 3
################################################################################
def countWordsMany(directory):
    # This function should create a dictionary of word count dictionaries
    # The dictionary should have one dictionary per file in the directory
    # Each entry in the dictionary should be a word count dictionary
    # Inputs: A directory containing a set of text files
    # Outputs: A dictionary containing a word count dictionary for each
    #          text file in the directory
    #open the direcory and pull a list of file names
    #create a dictionary to hold our data
    #populate the distionary
    #loop throught the list of files
        #for each file call countWordsUnstructured to get the word counts for that files
        #place the word count dictionary into the empty dictionary
    #return the dictionary
    dictionary = {}
    files = glob.glob(os.path.join(directory, '*.txt'))
    for fle in files:
        dictionary[fle] = countWordsUnstructured(fle)
    return (dictionary)
# Test your part 3 code below
directoryCount = countWordsMany("./state-of-the-union-corpus-1989-2017")
################################################################################
# PART 4
################################################################################
def generateDirectoryCSV(wordCounts, targetfile):
    # This function should create a CSV containing the word counts generated in
    # part 3 with the header:
    # Filename, Word, Count
    # Inputs: A word count dictionary and a name for the target file
    # Outputs: A CSV file named targetfile containing the word count data
    with open ('new.csv', 'w') as new_file:

        writer = csv.writer(new_file)
        writer.writerow(['Filename', 'Word', 'Count'])
        for k, v in directoryCount.items():
            for key,value in v.items():
                writer.writerow([k,key, value])
# Test your part 4 code below
generateDirectoryCSV(directoryCount, 'new.csv')
################################################################################
# PART 5
################################################################################
def generateJSONFile(wordCounts, targetfile):
    # This function should create an containing the word counts generated in
    # part 3. Architect your JSON file such that the hierarchy will allow
    # the user to quickly navigate and compare word counts between files.
    # Inputs: A word count dictionary and a name for the target file
    # Outputs: An JSON file named targetfile containing the word count data
    with open('result.json', 'w') as fp:
        json.dump(directoryCount, fp)
# Test your part 5 code below
generateJSONFile(directoryCount, 'result.json')
################################################################################
# PART 6
################################################################################
def searchCSV(csvfile, word):
    # This function should search a CSV file from part 4 and find the filename
    # with the largest count of a specified word
    # Inputs: A CSV file to search and a word to search for
    # Outputs: The filename containing the highest count of the target word
    return 0
def searchJSON(JSONfile, word):
    # This function should search a JSON file from part 5 and find the filename
    # with the largest count of a specified word
    # Inputs: An JSON file to search and a word to search for
    # Outputs: The filename containing the highest count of the target word
    return 0
# Test your part 6 code to find which file has the highest count of a given word

# +1 bonus point for figuring out how many datapoints you had to process to
# compute this value
