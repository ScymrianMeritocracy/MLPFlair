#!/usr/bin/python

import argparse
import os
import praw
import yaml

def loadflair():
    """Load flair list from file beside ourself."""
    mypath = os.path.dirname(os.path.realpath(__file__))
    myconf = open("{}/flair.yaml".format(mypath), "r")
    myflair = yaml.safe_load(myconf)
    myconf.close()
    return myflair["flairs"]

def update(sublist, flairlist):
    """Loop through given subreddits and create templates."""
    r = praw.Reddit()
    for sub in sublist:
        flairs = r.subreddit(sub).flair.templates
        try:
            for flair in flairlist:
                flairs.add(flair[1], flair[0])
        except:
            print("{}: trouble adding flair templates".format(sub))

def whatdo():
    """Handle argument parsing."""
    ap = argparse.ArgumentParser(__file__)
    ap.add_argument("subreddit", nargs="+", help="a subreddit name")
    return ap.parse_args()

if __name__ == "__main__":
    mysubs = whatdo()
    update(mysubs.subreddit, loadflair())
