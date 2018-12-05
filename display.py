import os
import sys
import time
import music_reports
import print_ascii_art
from prettytable import PrettyTable


def main():
    os.system("clear")
    display_menu()


def display_menu():
    print_ascii_art.print_starting_art()
    loop = True
    while loop is True:
        albums_list = []
        albums_list = music_reports.import_library(albums_list)
        choice = input("""
1: View all imported albums
2: Find albums by genre
3: Find albums from given time range
4: Find shortest/longest album
5: Find albums created by given artist
6: Find album by name
7: Generate full report
8: Add new album
9: Delete album
10: Exit

    What you want to do? """)

        if choice == "1":
            os.system("clear")
            result = music_reports.drawing_table(albums_list)
            print(result)

        elif choice == "2":
            os.system("clear")
            found_albums_by_genre = music_reports.find_by_genre(albums_list)
            print(found_albums_by_genre)

        elif choice == "3":
            loop2 = True
            while loop2 is True:
                os.system("clear")
                search_by_year_option = input("""
1: Search for albums made in given year
2: Search for albums made between years (yyyy-yyyy)

    What you want to do? """)

                if search_by_year_option == "1":
                    os.system("clear")
                    result = music_reports.find_albums_made_in_year(albums_list)
                    print(result)
                    loop2 = False
                elif search_by_year_option == "2":
                    os.system("clear")
                    result = music_reports.find_albums_made_between_years(albums_list)
                    print(result)
                    loop2 = False

                else:
                    os.system("clear")
                    print("Next time please enter '1' or '2'")
                    time.sleep(3)
                    os.system("clear")
                    continue

        elif choice == "4":
            os.system("clear")
            loop3 = True
            while loop3 is True:
                search_shortest_longest_album = input("""
1: Search for longest album
2: Search for shortest album

    What you want to do? """)
                if search_shortest_longest_album == "1":
                    os.system("clear")
                    music_reports.find_longest_album(albums_list)
                    loop3 = False

                elif search_shortest_longest_album == "2":
                    os.system("clear")
                    loop3 = False
                    music_reports.find_shortest_album(albums_list)

                else:
                    print("Next time please enter '1' or '2'")
                    time.sleep(3)
                    os.system("clear")
                    continue

        elif choice == "5":
            os.system("clear")
            found_albums_by_artist = music_reports.find_by_artist(albums_list)
            print(found_albums_by_artist)

        elif choice == "6":
            os.system("clear")
            found_albums_by_name = music_reports.find_by_name(albums_list)
            print(found_albums_by_name)

        elif choice == "7":
            os.system("clear")
            music_reports.find_longest_album(albums_list)
            music_reports.find_shortest_album(albums_list)
            music_reports.youngest_album(albums_list)
            music_reports.oldest_album(albums_list)

        elif choice == "8":
            os.system("clear")
            added_album_output = music_reports.add_album()
            print(added_album_output)

        elif choice == "9":
            os.system("clear")
            result = music_reports.drawing_table(albums_list)
            print(result)

            deleted_album_output = music_reports.delete_album()
            os.system("clear")
            print(deleted_album_output)

        elif choice == "10":
            os.system("clear")
            print_ascii_art.print_ending_art()
            sys.exit("")

        else:
            os.system("clear")
            print("Please enter numbers from 1 to 10: ")


if __name__ == "__main__":
    main()
