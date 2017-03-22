#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Simple command-line example for Custom Search.
Command-line application that does a search.
"""

__author__ = 'author-name'

from googleapiclient.discovery import build
import urllib.request
import app, os, glob

def findLink(googleData):
    start = googleData.find("'link':")
    tempString = googleData[start:]

    # finds the comma after the link
    finalString = tempString[:tempString.find(',')]
    return finalString

def imageAPI(searchTerms):
    arrayLinks = []  # empty list for array of links from search terms
    # if os.path.isfile("linkdir.txt") and os.stat("linkdir.txt").st_size > 0:
    #     os.remove("linkdir.txt")
    for term in searchTerms:
        # Build a service object for interacting with the API. Visit
        # the Google APIs Console <http://code.google.com/apis/console>
        # to get an API key for your own application.
        service = build("customsearch", "v1",
                developerKey=key)

        res = service.cse().list(
          q=term,
          cx='017491541522676942495:plkvt5o3nws',
          num= 1,
          start= 1,
          searchType= "image",
          imgType="photo",
        ).execute()
        linkRes = findLink(str(res))
        link = linkRes[linkRes.find('h'):-1]
        arrayLinks.append(link)
    return arrayLinks
        # output = open("linkdir.txt","a")
        # output.write(link + "\n")
        # output.close()
def main(searchTerms):
    try:
      arrayLinks = imageAPI(searchTerms)
      return arrayLinks
    except exception as err:
        print(err)
