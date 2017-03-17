#!/usr/bin/env python

"""
Based on PyVimeo.

https://github.com/vimeo/vimeo.py
"""

import os
import json

import vimeo

from pprint import pprint

def main():

    config_name = 'acesstoken.json'

    # Automated Stuff.  No Touchy!

    config_path = os.path.dirname(os.path.abspath(__file__)) + os.sep + config_name

    with open(config_path) as json_data:
        vars = json.load(json_data)

        v = vimeo.VimeoClient(
        token=vars['AccessToken'],
        key=vars['ClientID'],
        secret=vars['ClientSecret'])

        video_uri = v.upload('/Volumes/ProjectsRaid/WorkingProjects/babylondreams/PastProjectsArchive/IndustrieShowreel_h264.mp4')

        # Make the request to the server for the "/me" endpoint.
        about_me = v.get('/me')

        assert about_me.status_code == 200  # Make sure we got back a successful response.
        pprint(about_me.json())   # Load the body's JSON data.

        # end main

__all__ = ['MyDummyClass', 'my_dummy_function']

if __name__ == '__main__':
    main()