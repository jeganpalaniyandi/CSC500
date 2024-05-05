def calculate_hour_of_alarm(curr_hour, hours_from_now):

    alarm_hour = (curr_hour + hours_from_now) % 24
    print(f'\nHour in a 24 hour clock when the alarm goes off --> {alarm_hour}')

    # After meridiem or post meridiem
    meridiem = ''
    if alarm_hour > 12:
        meridiem = 'PM'
    else:
        meridiem = 'AM'

    print(f'\nHour in a 12 hour clock when the alarm goes off --> {alarm_hour % 12} {meridiem}')


if __name__ == "__main__":
    print()
    print('*' * 65)
    print(' ' * 14 + 'MODULE THREE ASSIGNMENT - PART TWO')
    print(' ' * 17 + '(ALARM TIME HOUR CALCULATOR)')
    print('*' * 65)

    current_hour = int(input('\nEnter valid current hour --> '))

    if 0 <= current_hour <= 24:
        print('Thank you for entering a valid hour. Calculating the alarm go off hour...')
    else:
        print('Not a valid hour, please re-run the progr am and enter a valid hour.')
        exit(4)

    alarm_hours_from_now = int(input('\nEnter the hours from now for your alarm to go off --> '))

    calculate_hour_of_alarm(current_hour, alarm_hours_from_now)
