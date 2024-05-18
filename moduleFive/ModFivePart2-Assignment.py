"""
    Input:
        - Total number of books purchased this month
    Output
        - Total points awarded for the books purchased

    book_club_award_program function displays the total
    award points based on the following table,

    | Total Books purchased | Award Points |
    ---------------------------------------
    |         0             |       0      |
    |         2             |       5      |
    |         4             |       15     |
    |         6             |       30     |
    |         8             |       60     |
    ----------------------------------------

"""


def book_club_award_program():

    # Get the total number of books purchased this month as integer and initialize total points
    tot_books_purchased = int(input("\nTotal number of books purchased this month --> "))
    tot_points = 0

    # Assumption has been made a student can purchase books only as 0, 2, 4, 6, 8
    # If the entered value from user is not one of the above value, the program exits
    # after printing appropriate error message
    if (not (tot_books_purchased == 0 or tot_books_purchased == 2 or
             tot_books_purchased == 4 or tot_books_purchased == 6 or
             tot_books_purchased == 8)):
        print("\nError -- Enter either 0, 2, 4, 6, 8 as total books purchased")
        exit(4)

    # Following if loop assigns the total points based on the user input
    if tot_books_purchased == 2:
        tot_points = 5
    elif tot_books_purchased == 4:
        tot_points = 15
    elif tot_books_purchased == 6:
        tot_points = 30
    elif tot_books_purchased == 8:
        tot_points = 60
    else:
        tot_points = 0

    # prints the total points aw
    print('Total points awarded for {} books --> {}'.format(tot_books_purchased, tot_points))


if __name__ == "__main__":
    print()
    print('*' * 65)
    print(' ' * 10 + 'CSU Global Bookstore - Award Points Calculator')
    print('*' * 65)
    book_club_award_program()
