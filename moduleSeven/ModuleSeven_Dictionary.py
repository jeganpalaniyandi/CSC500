def course_details():
    """
    This function will prompt the user for course number
    and on submission, it will print the course number,
    room number, instructor and Meeting time.
    :return:
    """
    # Dictionaries containing course information
    room_dict = {'CSC101': 3004,
                 'CSC102': 4501,
                 'CSC103': 6755,
                 'NET110': 1244,
                 'COM241': 1411
                 }

    instructor_dict = {'CSC101': 'Haynes',
                       'CSC102': 'Alvarado',
                       'CSC103': 'Rich',
                       'NET110': 'Burke',
                       'COM241': 'Lee'
                       }

    meeting_time_dict = {'CSC101': '8:00 a.m.',
                         'CSC102': '9:00 a.m.',
                         'CSC103': '10:00 a.m.',
                         'NET110': '11:00 a.m.',
                         'COM241': '1:00 p.m.'
                         }

    # Get user input for course number
    course_number = input("Enter a course number -->  ")

    # Look up information based on the course number
    if course_number in room_dict:
        room_number = room_dict[course_number]
        instructor = instructor_dict[course_number]
        meeting_time = meeting_time_dict[course_number]

        # Display the information
        print(f"Course: {course_number}")
        print(f"Room Number: {room_number}")
        print(f"Instructor: {instructor}")
        print(f"Meeting Time: {meeting_time}")
    else:
        print(f"Course '{course_number}' not found. Please check the course number.")


if __name__ == "__main__":
    course_details()
