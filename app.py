import requests 
from secret import KEY
import csv
import random

def movieGuessGame():
    case = 1
    movie = getMovie()
    win = False
    instructions()
    while(case != 7 and win == False):
        hint(case, movie)
        guess = getUserInput()
        win = isMovie(guess, movie)
        case += 1
    if(win == False):
        print("The movie was '" + movie["Title"] + "'")

def instructions():
    print("Welcome to the MovieGuesser game!")
    print("In this game you will guess the name of a random movie that's given.")
    print("You will have 5 hints and guesses until the right answer will be shown.")
    print("GOOD LUCK!", end = "\n\n")

def getMovie():
    lines = []
    with open('data.csv', "r") as file:
        csvFile = csv.reader(file)
        for x in csvFile:
            lines.append(x)
    length = len(lines)
    rand = random.randint(0,length - 1)
    
    req = requests.get("http://www.omdbapi.com/?apikey={}&t={}&plot=full".format(KEY, lines[rand][0].split("=")[1]))
    return req.json()

def hint(case, movie):
    match case:
        case 1:
            print("This movie was released on " + movie["Released"])
        case 2:
            print("The genre is " + movie["Genre"])
        case 3:
            print("A few of the actors are " + movie["Actors"])
        case 4:
            print("It was released in " + movie["Country"])
        case 5:
            newWord = ""
            for x in movie["Title"]:
                if x.isalpha():
                    newWord += "*"
                else:
                    newWord += x
            print("Here's the movie's title without any letters " + newWord)
        case 6:
            print("Here's some of the plot: " + movie["Plot"][:50] + "...")

def getUserInput():
    guess = input("Type in your guess: ")
    return guess


def isMovie(guess, movie):
    if(guess.lower() == movie["Title"].lower()):
        print("CORRECT! The movie was '" +  movie["Title"] + "' you win!")
        return True
    return False


movieGuessGame()