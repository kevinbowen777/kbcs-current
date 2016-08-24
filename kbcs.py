#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 17:38:16 2016
Purpose: fetch currently playing track on http://kbcs.org
and print to the console.
@author: kbowen (kevin.bowen@gmail.com)
TODO - simplify banner
"""

import requests

r = requests.get('http://kbcsweb.bellevuecollege.edu/play/api/nowplaying/')

now_playing = r.json()

title = now_playing['title']
playlistId = now_playing['playlistId']
"""
Some station programs do not populate data properly and return a
playlistId of zero with no song information
"""
if playlistId == 0:
    # break banner
    print ('==================================')
    print 'KBCS 91.3 FM Radio  - ', title
    print ('---------------------------------')
    print ('Station Break.')
    print 'Try again in a few minutes.'
    print ('==================================')
else:
    artist = now_playing['artist']
    title = now_playing['title']
    # playlist banner
    print ('==================================')
    print 'Now playing on KBCS 91.3 FM Radio'
    print ('---------------------------------')
    print 'Artist:', artist, '\n', 'Title: ', title
    print ('==================================')
