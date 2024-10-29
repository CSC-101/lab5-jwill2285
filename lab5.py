import data
import math


# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.

# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
def time_add(first: data.Time, second: data.Time) -> data.Time:
    #first adds the hours, minutes, and seconds together of the two inputs
    hours = first.hour + second.hour
    minutes = first.minute + second.minute
    seconds = first.second + second.second
    #checks if the seconds and minutes are greater than 60, if they are takes the amount of times
    #that it is divided by 60 and adds it to the one above it. After that leaves the remainder after
    #dividing by 60
    if seconds >= 60:
        minutes += seconds // 60
        seconds %= 60
    if minutes >= 60:
        hours += minutes // 60
        minutes %= 60
    return "Hours: {}, Minutes: {}, Seconds: {}".format(hours,minutes,seconds)
# Part 4
def is_descending(numbers : list[float])->bool:
    #makes two unique lists to check similarity
    originalList = numbers[:]
    checkedList = numbers[:]
    #runs the selection sort to make sure the list is in order
    for i in range(len(checkedList) - 1):
        big_idx = i
        for j in range(i + 1, len(checkedList)):  # finding index of smallest
            if checkedList[j] > checkedList[big_idx]:
                big_idx = j
        if big_idx != i:
            temp = checkedList[big_idx]
            checkedList[big_idx] = checkedList[i]
            checkedList[i] = temp
    #before returning checks if the lists are the same, if not returns false
    return checkedList == originalList
# Part 5
def largest_between(lists: list[int], second : int, third : int)->any:
    #grabs the first value that the list is checking for using the second parameter
    largest_val = lists[second]
    #checks if second or third is outside the lists parameters
    if second < 0 or third < 0:
        return None
    if second > len(lists) or third > len(lists):
        return None
    #if inside parameters, checks for largest value and will return at end
    for i in range(second,third):
        if lists[i] > largest_val:
            largest_val = lists[i]
    return largest_val

# Part 6
from data import Point
def furthest_from_origin(coords : list[Point])->None or data.Point:
    #sets max and furthest at 0 to start
    max_distance = 0
    furthest_index = 0
    #checks if list is empty
    if coords == []:
        return None
    #checks the distance of each point values and if the distance is greater
    #than the max distance then it returns it as the new highest value
    for i in range(len(coords)):
        distance_squared = coords[i].x ** 2 + coords[i].y ** 2
        if distance_squared > max_distance:
            max_distance = distance_squared
            furthest_index = i

    return furthest_index