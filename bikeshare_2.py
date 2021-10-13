import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_OPTIONS = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
DAY_OPTIONS = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # Get city input
    city = str(input("Enter a city to see data. Options: New York, Chicago, Washington: \n"))
    city_options = ['new york', 'chicago', 'washington']

    while city.lower() not in city_options:
        city = str(input('Please enter a correct city or terminate program. Options: New York, Chicago, Washington: \n'))
    city = city.lower()

    # Get month input
    month = str(input(
        'Enter a month between January and June to apply month filter or "All" to skip month filter: \n'))
    
    
    while month.lower() not in MONTH_OPTIONS:
        month = str(input('Please enter a month between January and June or All, or terminate program: \n'))
    month = MONTH_OPTIONS.index(month.lower())

    # Get day input
    day = str(input('Enter a day of the week to apply day filter or "All" to skip day filter: \n'))
    
    

    while day.lower() not in DAY_OPTIONS:
        day = str(input('Please enter a day of the week or All, or terminate program: \n'))
    day = day.lower()

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
    df = pd.read_csv(CITY_DATA[city], index_col=[0])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    df['hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 0:
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.capitalize()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    month = df['month'].mode()[0]
    print(f'Most common month is: {MONTH_OPTIONS[month].capitalize()}')

    # display the most common day of week
    print(f'Most common day of the week is: {df["day_of_week"].mode()[0]}')


    # display the most common start hour
    print(f'Most common start hour is: {df["hour"].mode()[0]}')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print(f'Most common Start Station is: {df["Start Station"].mode()[0]}')

    # display most commonly used end station
    print(f'Most common End Station is: {df["End Station"].mode()[0]}')

    # display most frequent combination of start station and end station trip
    print(f'Most frequent combination of Start and End Stations is: {(df["Start Station"] + "-" + df["End Station"]).mode()[0]}')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    df['travel_time'] = df['End Time'] - df['Start Time']

    # display total travel time
    print(f'Total Travel Time is: {df["travel_time"].sum()}')

    # display mean travel time
    print(f'Mean Travel Time is: {df["travel_time"].mean()}')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(f'\nThe count of User Types is: {df["User Type"].value_counts()}')

    # Display counts of gender
    if 'Gender' in df.columns:
        print(
            f'\nThe count of Male Gender is: {(df.Gender == "Male").sum()} and count of Female Gender is {(df.Gender == "Female").sum()}'
            )
    else:
        print('\nThis data has no Gender')
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print(f'\nEarliest Year of Birth is: {int(df["Birth Year"].min())}')
        print(f'\nMost Recent Year of Birth is: {int(df["Birth Year"].max())}')
        print(f'\nMost Common Year of Birth is: {int(df["Birth Year"].mode()[0])}')
    else:
        print("\nThis data doesn't have Year of Birth")



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    see_data(df)

def see_data(df):
    start = 0
    while True and start < len(df):
        raw_data = str(input('Would you like to see raw data? \n'))
        if raw_data.lower() != 'yes':
            break
        else:
            data_list = df.iloc[start:start+5].to_dict('records')
            for data in data_list:
                print(f'\n{data}')
        start += 5
        



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
