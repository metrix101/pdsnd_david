import time
import pandas as pd
import numpy as np

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December', 'All']

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
        'Saturday', 'Sunday', 'All']

data_switch = True


def get_filters():
    """
    Asks the user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of the week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # Get user input for the city (Chicago, New York City, Washington)
    city = ""
    while city not in CITY_DATA.keys():
        city_input = input("\nWhich city would you like to see?"
                           "\nAvailable Cities: Chicago, New York City, Washington\n").lower()
        city = city_input

    # Get user input for the month (All, January, February, ..., December)
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

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...')
    start_time = time.time()

    print("Most common Year: {}".format(df['Year'].value_counts().idxmax()))
    print("Least common Year: {}".format(df['Year'].value_counts().idxmin()))

    print("Most common Month: {}".format(df['Month'].value_counts().idxmax()))
    print("Least common Month: {}".format(df['Month'].value_counts().idxmin()))

    print("Most common Day of Week: {}".format(df['Day of Week'].value_counts().idxmax()))
    print("Least common Day of Week: {}".format(df['Day of Week'].value_counts().idxmin()))

    print("Most common Start Hour: {}".format(df['Hour'].value_counts().idxmax()))
    print("Least common Start Hour: {}".format(df['Hour'].value_counts().idxmin()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trips."""
    print('\nCalculating The Most Popular Stations and Trips...')
    start_time = time.time()

    print("\nMost Commonly Used Start Station: {}".format(df['Start Station'].value_counts().idxmax()))
    print("\nMost Commonly Used End Station: {}".format(df['End Station'].value_counts().idxmax()))

    most_common_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print("\nMost Frequent Combination of Start Station and End Station Trip: {}".format(most_common_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    print("Total Travel Time: {}".format(total_travel_time))

    average_travel_time = df['Trip Duration'].mean()
    print("Average Travel Time: {}".format(average_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...')
    start_time = time.time()

    user_types = df['User Type'].value_counts()
    print("Counts of User Types:")
    print(user_types)

    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print("\nCounts of Genders:")
        print(gender_counts)

    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        recent_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()[0]

        print("\nEarliest Birth Year: {}".format(earliest_birth_year))
        print("Recent Birth Year: {}".format(recent_birth_year))
        print("Most Common Birth Year: {}".format(most_common_birth_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def display_data(df, data_switch):
    count = 0
    while data_switch:
        data_prompt = input("Would you like to view the data? Yes/No\n").title()
        if data_prompt == "Yes" and count < len(df):
            print(df.iloc[count: count + 5])
            count += 5
        elif count >= len(df):
            print("You reached the end of the file.")
        else:
            data_switch = False


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df, data_switch)

        restart = input('\nWould you like to restart? Enter "yes" or "no".\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
