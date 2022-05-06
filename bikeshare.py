import time
import pandas as pd
import numpy as np

# Establish a map for the city data files
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# Establish a map for the days of the week to use with the user input
days = {'su' : 'sunday', 'm': 'monday', 'tu' : 'tuesday', 'w' : 'wednesday',
        'th' : 'thursday', 'f' : 'friday', 'sa' : 'saturday'}



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True: # you'll remain in the loop until a break statment
        city = input('\nWould you like to see data for Chicago, New York City, or Washington?\n').lower()
        
        if city in CITY_DATA:
            print('Looks like you want to hear about ', city.title())
            break # ends loop
    
    while True: # you'll remain in the loop until a break statment
    
        filter = input('\nWould you like to filter the data by month, day, or not at all? Type anything other than "month" or "day" for no time filter.\n')    
        
        # TO DO: get user input for month (all, january, february, ... , june)               
        if filter == 'month':
            print('\nWe will make sure to filter by month!\n')
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            while True:
                month = input('\nWhich month? January, February, March, April, May, or June? Please type out the full month name.\n').lower()
                if month in months: 
                    break
                else:
                    month = month.title()
                    print(f'\n{month} is an invalid entry.\n')
            day = 'all'
            #print(month)
            #print(day)
            break # ends loop

        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        elif filter == 'day':
            print('\nWe will make sure to filter by day!\n')
            while True:
                try:
                    day = days[input('\nWhich day? Please type a day with the following abbreviations M, Tu, W, Th, F, Sa, Su.\n').lower()]
                    break
                except:
                    print('\nPlease enter the day again.\n')
            month = 'all'
            #print(month)
            #print(day)
            break # ends loop
                       
        else:
            print('\nWe will not filter the data.\n')
            month = 'all'
            day = 'all'
            #print(month)
            #print(day)
            break

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('\nWhat is the most popular month for traveling?\n')
    month_mode = df['month'].mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    print(months[month_mode-1].title())
    #month_time = time.time()
    #print('\nThat took ', month_time - start_time, 'seconds.\n') 

    # TO DO: display the most common day of week
    print('\nWhat is the most popular day for traveling?\n')
    print(df['day_of_week'].mode()[0])
    #day_time = time.time()
    #print('\nThat took ', day_time - month_time, 'seconds.\n') 

    # TO DO: display the most common start hour
    print('\nWhat is the most popular hour of day to start traveling?\n')
    df['hour'] = df['Start Time'].dt.hour
    print(df['hour'].mode()[0])
    #hour_time = time.time()
    #print('\nThat took ', hour_time - day_time, 'seconds.\n') 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('\nWhat is the most commonly used start station?\n')
    start_station_mode = df['Start Station']. mode()[0]
    print(start_station_mode)

    # TO DO: display most commonly used end station
    print('\nWhat is the most commonly used end station?\n')
    end_station_mode = df['End Station']. mode()[0]
    print(end_station_mode)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start-End'] = df['Start Station'].str.cat(df['End Station'], sep='-')
    print('\nWhat is the most frequent combination of start station and end station trip?\n')
    combo_mode = df['Start-End'].mode()[0]
    print(combo_mode)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('\nWhat is the total travel time?\n')
    print(total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('\nWhat is the mean travel time?\n')
    print(mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\nWhat are the user type counts?\n')
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    try:
        print('\nWhat are the gender counts?\n')
        genders = df['Gender'].value_counts()
        print(genders)
    except:    
        print('\nThis city does not track gender.\n')
             
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('\nWhat is the earliest birth year?\n')
        earliest = int(df['Birth Year'].min())
        print(earliest)
        print('\nWhat is the most recent birth year?\n')
        recent = int(df['Birth Year'].max())
        print(recent)
        print('\nWhat is the most common birth year?\n')
        most_common = int(df['Birth Year'].mode()[0])
        print(most_common)
    except:    
        print('\nThis city does not birth year.\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def raw_data(df):
    """Displays 5 rows of data until user wants to stop""" 
    
    data_counter = 0
    raw = input('\nWould you like to view raw individual trip data? Type yes or no.\n').lower()
         
    if raw == 'yes':
        print(df.head())
        while True:
            again = input('\nWould you like to view more raw individual trip data? Type yes or no.\n').lower()
            if again == 'yes':
                data_counter += 5
                print(df[data_counter:data_counter+5])
            elif again == 'no':
                break
            else:
                print('\nPlease enter yes or no.\n')
    elif raw == 'no':
        print('\nThank you for viewing the bikeshare stats.\n')
    else:
        print('\nPlease enter yes or no.\n')

                              
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
