#!/usr/bin/env python
# coding: utf-8

# In[1]:


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
    print('Hello! Let\'s explore some US bikeshare data!')
    print('-'*40)
    return city, month, day

#This project aim to learn python
# In[2]:


# get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
cities = list(CITY_DATA.keys())
city = input("Please choose one those cities: Chicago, New York city, Washington:\n").lower()

while (city not in cities):
   city = input("Which city do you want explore?").lower()
   print("Chicago", "New York", "Washington")


# In[3]:


# get user input for month (all, january, february, ... , june)
months = ["all", "january", "february", "march", "april", "may", "june"]
month = input("Please choose one those monhts:\n").lower()

while (month not in months):
   month = input("Please choose one those monhts").lower()
   print("january", "february", "march", "april", "may", "june")


# In[4]:


# get user input for day of week (all, monday, tuesday, ... sunday)
day_of_week = ["all", "monday", "tuesday", "wednesday", "thursday", "friday","saturday","sunday"]
day = input("Please choose a day of week:\n").lower()

while (day not in day_of_week):
   day = input("Which day do you prefer?").lower()
   print("monday", "tuesday", "wednesday", "thursday", "friday","saturday","sunday")


# In[5]:


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
    df = pd.read_csv(CITY_DATA['chicago'])
#convert the Start Time column to datetime
    df['Start Time']=pd.to_datetime(df['Start Time'])    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA['washington'])
#convert the Start Time column to datetime
    df['Start Time']=pd.to_datetime(df['Start Time'])   

#extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day

#filter by month if applicable
    if month != 'all':   
#use the index of the months list to get the corresponding int
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1
    
    #filter by month to create the new dataframe
    df = df[df['month'] == month]
    #filter by day of week if applicable
    if day != 'all':            
    #filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()]
    
    return df


# In[7]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month:",common_month)

    # display the most common day of week    
    day_week = df['day_of_week'].mode()[0]
    print("The most common day of week:",day_week)

    # display the most common start hour  
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most popular hour
    popular_hour = df['hour'].mode()[0]  
    print('Most Popular Start Hour:', popular_hour)

# In[8]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time:",total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("mean travel time:",mean_travel_time)

    # display median travel time
    median_travel_time = df['Trip Duration'].median()
    print("median travel time:",median_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[9]:


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User Type:",user_types)


    # Display counts of gender

    count_gender= df['Gender'].value_counts()
    print("Gender Number:",count_gender)


    # Display earliest, most recent, and most common year of birth
    
    earliest_birth = df['Birth Year'].min()
    print("The earliest year of Birth:", earliest_birth)
    recent_birth = df['Birth Year'].max()
    print("The most recent year of birth:", recent_birth)
    common_birth = df['Birth Year'].mode()[0]
    print("The most common year of birth:",common_birth)
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[11]:


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

#change in refactoring branch
#second change in refactoring branch
# In[ ]:




