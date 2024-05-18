"""
    'rainfall_metrics' method gets the following inputs from user,
        - Total years for calculating metrics
        - Recorded rainfall of each month of the total years entered above

    Outputs,
        - Total months
        - Total rainfall recorded
        - Average rainfall as 'Total rainfall recorded' divided by 'Total months'
"""


def rainfall_metrics():
    # get the total number of years for which the metrics needs to be calculated
    tot_years = int(input("\nEnter the number of years for calculating rainfall metrics -> "))
    # assumption is curr_year = 2024 so that total number of years(n) is considered as recent past n years
    curr_year = 2024

    # Initializing program variables
    tot_months = 0
    tot_rainfall = 0.00
    avg_rainfall = 0.00

    # Declaring a months list which will be used in the loop while prompting the user
    # to enter rainfall for each month
    months = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]

    # Outerloop - loops through the total number of years
    # Innerloop - loops through the twelve months of a year
    #             calculates the total months and accumulation of rainfall at the end of each loop
    for year in range(1, tot_years + 1):
        print('\nEnter the monthly rainfall for year -> ' + str(curr_year - year) + '\n')
        for index, month in enumerate(months):
            this_month_rainfall = float(input('Enter the average rainfall(inches) of {} month, {} --> '
                                              .format(month, curr_year - year)))
            tot_months += 1
            tot_rainfall += this_month_rainfall

    # Calculating average rainfall as 'Total rainfall recorded' divided by 'Total months'
    avg_rainfall = tot_rainfall / tot_months

    print('\nTotal months                        --> {}'.format(tot_months))
    print('Total rainfall recorded in {} year(s) --> {:.2f} inches'.format(tot_years, tot_rainfall))
    print('Average rainfall in {} year(s)        --> {:.2f} inches'.format(tot_years, avg_rainfall))


if __name__ == "__main__":
    print()
    print('*'*65)
    print(' '*20 + 'Average Rainfall Calculator')
    print('*'*65)
    rainfall_metrics()
