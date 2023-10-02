import time
import pandas as pd
import numpy as np

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

months = ['January', 'February', 'March', 'April', 'May', 'June', 'All']

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
        'Saturday', 'Sunday', 'All']



def get_filters():
    """
    Asks the user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of the week to filter by, or "all" to apply no day filter
    """
    print("Hello! Let's explore some US bikeshare data!")

    # Get user input for the city (Chicago, New York City, Washington)
    city = ""
    while city not in CITY_DATA.keys():
        city_input = input("\nWhich city would you like to see?"
                           "\nAvailable Cities: Chicago, New York City, Washington\n").lower()
        city = city_input

    # Get user input for the month (All, January, February, ...,June)
    month = ""
    while month not in months:
        month_input = input("What month would you like to view? All, January, ..., December\n").title()
        month = month_input

    # Get user input for the day of the week (All, Monday, Tuesday, ..., Sunday)
    day = ""
    while day not in days:
        day_input = input("What day would you like to view? All, Monday, ..., Sunday\n").title()
        day = day_input

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of the week to filter by, or "all" to apply no day filter

    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
<<<<<<< HEAD
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.day_name()
    
    if month != 'all':
        df = df[df['Month'] == month]
    
    if day != 'all':
        df = df[df['Day of Week'] == day]
=======
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df['Month'] = df['Start Time'].dt.strftime('%B')
    df["Day of Week"] = df["Start Time"].dt.day_name()
    df["Hour"] = df["Start Time"].dt.hour
    df["Year"] = df["Start Time"].dt.year

    if month != "All" and day != "All":
        df = df[(df["Month"] == month) & (df["Day of Week"] == day)]
    elif month != "All":
        df = df[df["Month"] == month]
    elif day != "All":
        df = df[df["Day of Week"] == day]
>>>>>>> refactoring

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...')
    start_time = time.time()
    
    print("\nThe most common Year: {}".format(df['Year'].value_counts().idxmax()))    
     
     # # TO DO: display the most common month
    print("\nThe most common month: {}".format(df['Start Station'].value_counts().idxmax()))

    # TO DO: display the most common day of week

    print("The Most common Day of Week: {}".format(df['Day of Week'].value_counts().idxmax()))

    # TO DO: display the most common start hour 
    print("Most common Start Hour: {}".format(df['Hour'].value_counts().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trips."""
    print('\nCalculating The Most Popular Stations and Trips...')
    start_time = time.time()

     #TO DO: display most commonly used start station
    print("\nMost Commonly Used Start Station: {}".format(df['Start Station'].value_counts().idxmax()))

     # TO DO: display most commonly used end station
    print("\nMost Commonly Used End Station: {}".format(df['End Station'].value_counts().idxmax()))

    # TO DO: display most frequent combination of start station and end station trip
    most_common_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print("\nMost Frequent Combination of Start Station and End Station Trip: {}".format(most_common_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total Travel Time: {}".format(total_travel_time))

    # Average Travel Time
    avg_travel_time = df['Trip Duration'].avg()
    print("Average Travel Time: {}".format(avg_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean Travel Time: {}".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of User Types:")
    print(user_types)

    #TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print("\nCounts of Genders:")
        print(gender_counts)

 # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        recent_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()[0]

        print("\nEarliest Birth Year: {}".format(earliest_birth_year))
        print("Recent Birth Year: {}".format(recent_birth_year))
        print("Most Common Birth Year: {}".format(most_common_birth_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
       

        restart = input('\nWould you like to restart? Enter "yes" or "no".\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
