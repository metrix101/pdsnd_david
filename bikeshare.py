import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    city = ''
    month = 'all'
    day = 'all'
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while city.lower() not in CITY_DATA:
        city = input("Enter City name (Chicago, New York City, Washington): ").lower()
        if city not in CITY_DATA:
            print(f"invalid city name. Please choose from Chicago, New York City, or Washington")


    # TO DO: get user input for month (all, january, february, ... , june)
    while month.lower() not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        month = input("Enter month name (all, january, february, ..., june: ").lower()
 
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while day.lower() not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        day = input("Enter day of the week (all, monday, tuesday, ..., sunday: ").lower()
 
    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.day_name()
    
    if month != 'all':
        df = df[df['Month'] == month]
    
    if day != 'all':
        df = df[df['Day of Week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['Month'].mode()[0]
    print(f"The most common month for bike rides is: {common_month}")

    # TO DO: display the most common day of week
    common_day = df['Day of Week'].mode()[0]
    print(f"The most common day of the week for bike rides is: {common_day}")

    # TO DO: display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    common_hour = df['Hour'].mode()[0]
    print(f"The most common start hour for bike rides is: {common_hour}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print(f"The most commonly used start station is: {start_station}")

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print(f"The most commonly used end station is: {end_station}")

    # TO DO: display most frequent combination of start station and end station trip
    trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print(f"The most frequent combination of start station and end station is: {trip[0]} to {trip[1]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f"The total travel time for bike rides is: {total_travel_time} seconds")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f"The mean travel time for bike rides is: {mean_travel_time} seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Types'].value_counts()
    print("Counts of User Types: ")
    for user_type, count in user_types.items():
        print(f"{user_type}: {count}")


    # TO DO: Display counts of gender
    if 'Gender' in df:
        genders = df['Gender:'].value_counts()
        print("\nCounts of Gender: ")
        for gender, count in genders.items():
            print(f"{gender}: {count}")
    else:
        print("\nGender information not available in this dataset.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth_year = int(df['Birth Year'].min())
        recent_birth_year = int(df['Birth Year'].max())
        common_birth_year = int(df['Birth Year'].mode[0])
        print("\nBirth Year Statistics:")
        print(f"Earliest Birth Year: {earliest_birth_year}")
        print(f"Most Recent Birth Year: {recent_birth_year}")
        print(f"Most Common Birth Year: {common_birth_year}")
    else:
        print("\nBirth year information not available in this dataset.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
