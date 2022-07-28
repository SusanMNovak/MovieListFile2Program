# IS 280 Assignment 7(Part1) – MovieListFile1Program  Susan Novak

# import movie.csv an Excel csv spreadsheet
import csv

# a file in the current directory
FILENAME = "movies.csv"

# obtain and writes movie list to a file
def write_movies(movies):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(movies)

# creates an empty movie list and reads and appends each movie to the list returning list
def read_movies():
    movies = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            movies.append(row)
    return movies

# # list function checks if there are any movies, updates and displays movies
def list_movies(movies):
    for i, movie in enumerate(movies, start=1):
        print(f"{i}. {movie[0]} ({movie[1]})")
    print()

# # add function obtains movie information and adds movie
def add_movie(movies):
    name = input("Name: ")
    year = input("Year: ")
    movie = [name, year]
    movies.append(movie)
    write_movies(movies)
    print(f"{name} was added.\n")

# delete function obtains movie information and deletes movie
def delete_movie(movies):
    index = int(input("Number: "))
    if index < 1 or index > len(movies):
        print("Invalid movie number.\n")
    else:
        movie = movies.pop(index - 1)
        write_movies(movies)
        print(f"{movie[0]} was deleted.\n")

# display_menu function displays displays user commands
def display_menu():
    print("The Movie List program")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print()

# main function creates movie list and calls functions based on user commands
def main():
    display_menu()
    movies = read_movies()
    while True:
        command = input("Command: ")
        if command.lower() == "list":
            list_movies(movies)
        elif command.lower() == "add":
            add_movie(movies)
        elif command.lower() == "del":
            delete_movie(movies)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")


if __name__ == "__main__":
    main()
