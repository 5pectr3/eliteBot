"""
Module for distance and jump calculation

This module allows the user to input two valid systems and 
calculates a distance between them using the EDSM API.
Furthermore, the user may input a jump range, and the module will calculate
the number of jumps required.

Author: 5pectr3
Date:   7/6/2021
"""
import requests
import json
import urllib



def first_inside_quotes(s):
       """
       Returns: The first substring of s between two (double) quote characters.
       
       Parameter s: a string to search
       Precondition: s a string with at least two (double) quote characters.
       """
       result = s.find("\"")
       result1 = s.find("\"",result+1, len(s))
       return(s[int(result+1):int(result1)])

def get_x(inp):
    """
    Returns the x-value coordinate from a JSON string

    Parameter inp: the string to slice
    Precondition: inp is a valid JSON string containing the
    letter x
    """
    search = inp.find('x')
    comma = inp.find(',', search)
    substring = inp[search : comma+1]
    substring = substring.replace('x\":', '')
    substring = first_inside_quotes(substring)
    return float(substring)

def get_y(inp):
    """
    Returns the y-value coordinate from a JSON string

    Parameter inp: the string to slice
    Precondition: inp is a valid JSON string containing the
    letter y
    """
    search = inp.find('y')
    comma = inp.find(',', search)
    substring = inp[search : comma+1]
    substring = substring.replace('y\":', '')
    substring = first_inside_quotes(substring)
    return float(substring)

def get_z(inp):
    """
    Returns the z-value coordinate from a JSON string

    Parameter inp: the string to slice
    Precondition: inp is a valid JSON string containing the
    letter z
    """
    search = inp.find('z')
    comma = inp.find(',', search)
    substring = inp[search : comma]
    substring = substring.replace('z\":', '')
    substring = first_inside_quotes(substring)
    return float(substring)

def calc(x1,y1,z1,x2,y2,z2):
    """
    Returns the 3-dimensional distance between 2 sets of points

    Parameter x1,y1,z1: the coordinates of the first point
    Parameter x2,y2,z2: the coordinates of the second point
    Precondition: all values are valid floats or ints
    """
    return ((((x2-x1)**2)+((y2-y1)**2)+((z2-z1)**2))**(1.0/2.0))

def get_dist_range(start, end, jumprange):
    """
    Returns the distance and required jumps between two valid systems.

    Example: get_distance('daibais', 'garabaei', 22)
    Returns: The distance between daibais and garabaei is 79ly, and it will 
    take 4 jumps with your range of 22ly.

    Parameter start: The name of the starting system
    Parameter end: The name of the end system
    Parameter jumprange: The jumprange of your current or intended ship
    Precondition: Parameters start and end must be valid, non-empty strings
    consisting of valid Elite Dangerous systems. 
    Precondition: Jumprange must be a valid non-zero int or float
    """
    web_url = 'https://www.edsm.net/api-v1/system?'
    web_url2 = 'https://www.edsm.net/api-v1/system?'
    s1 = 'systemName=' + start + '&showCoordinates=1'
    web_url = web_url + s1
    if (" " in web_url):
        web_url = web_url.replace(" ","+")
    response = urllib.request.urlopen(web_url)
    s2 = 'systemName=' + end + '&showCoordinates=1'
    web_url2 = web_url2 + s2
    if (" " in web_url2):
        web_url2 = web_url2.replace(" ","+")
    response2 = urllib.request.urlopen(web_url2)
    response = str(response.read(), 'utf-8')
    response2 = str(response2.read(), 'utf-8')
    start_coordx = get_x(response) 
    start_coordy = get_y(response)
    start_coordz = get_z(response)
    end_coordx = get_x(response2)
    end_coordy = get_y(response2)
    end_coordz = get_z(response2)
    distance = round(calc(start_coordx,start_coordy,start_coordz,end_coordx,end_coordy,end_coordz))
    if ("+" in end):
      end = end.replace("+", " ")
    if ("+" in start):
      start = start.replace("+", " ")
    distance = round(calc(start_coordx,start_coordy,start_coordz,end_coordx,end_coordy,end_coordz))
    jumps = round(float(distance)/float(jumprange))
    return(print('The distance between ' + str(start) + ' and ' + str(end) + ' is ' + str(distance) + 'ly, and it will take ' + str(jumps) + ' jumps with your range of ' + str(jumprange) + 'ly.'))
    
    
    
def get_distance(start, end):
    """
    Returns the distance between two valid systems.

    Example: get_distance('daibais', 'garabaei')
    Returns: The distance between daibais and garabaei is 79ly.

    Parameter start: The name of the starting system
    Parameter end: The name of the end system
    Precondition: Parameters start and end must be valid, non-empty strings
    consisting of valid Elite Dangerous systems. 
    """
    web_url = 'https://www.edsm.net/api-v1/system?'
    web_url2 = 'https://www.edsm.net/api-v1/system?'
    s1 = 'systemName=' + start + '&showCoordinates=1'
    web_url = web_url + s1
    if (" " in web_url):
        web_url = web_url.replace(" ","+")
    response = urllib.request.urlopen(web_url)
    s2 = 'systemName=' + end + '&showCoordinates=1'
    web_url2 = web_url2 + s2
    if (" " in web_url2):
        web_url2 = web_url2.replace(" ","+")
    response2 = urllib.request.urlopen(web_url2)
    response = str(response.read(), 'utf-8')
    response2 = str(response2.read(), 'utf-8')
    start_coordx = get_x(response) 
    start_coordy = get_y(response)
    start_coordz = get_z(response)
    end_coordx = get_x(response2)
    end_coordy = get_y(response2)
    end_coordz = get_z(response2)
    distance = round(calc(start_coordx,start_coordy,start_coordz,end_coordx,end_coordy,end_coordz))
    if ("+" in end):
      end = end.replace("+", " ")
    if ("+" in start):
      start = start.replace("+", " ")
    return('The distance between ' + str(start) + ' and ' + str(end) + ' is ' + str(distance) + 'ly')




    