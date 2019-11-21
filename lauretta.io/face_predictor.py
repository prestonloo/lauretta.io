#!/usr/bin/env python

'''
Task 2:
Have a file face_predictor.py or equivalent that takes one string that represents the access code for https://hackattic.com/challenges/basic_face_detection and returns the json structure face_tiles that fulfils the requirements in the hackattic challenge
Feel free to use hackattic and even the discussion board for hints.
That's it. It’s okay to not be accurate there are no points for an exact answer, only good code.
'''

import requests 
import shutil
#import face_recognition

def face_predictor(accessCode):
    
    #create url with access code
    URL = "https://hackattic.com/challenges/basic_face_detection/problem?access_token="+accessCode
    
    #send a http get request to url
    result = requests.get(URL) 
    
    #extract image url from http response
    resultJSON = result.json() 
    imageURL = resultJSON['image_url']

    #send a http get request to image url
    result = requests.get(imageURL, stream=True)
    
    #extract image from http response and save as a image.jpg file
    image = open('image.jpg', 'wb')
    result.raw.decode_content = True
    shutil.copyfileobj(result.raw, image)

    #from here onward we have the downloaded picture and next will be to process the downloaded picture to identify the face using face_recognition module
    #however, the installation of face_recognition module on my workstation failed.

#below is a test case with a valid access code
face_predictor("abd61693020c5135")
