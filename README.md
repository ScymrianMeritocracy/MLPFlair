MLPFlair
========

This is a simple script to create the dozens of "standard" My Little Pony flair templates for a sub on Reddit. Scymrian Meritocracy subreddits have a few extra flairs, and these are included.

Requirements
------------

 * [PRAW4](https://praw.readthedocs.io/en/praw4/index.html)
 * [PyYAML](http://pyyaml.org/)

Setup
-----

Copy the example configuration to a file called `praw.ini`, and edit at least the stuff in caps to suit your needs. This file and `flair.yaml` are expected to be in the same directory as the script. Note that the `client_id` and `client_secret` values are obtained in your [account preferences](https://github.com/reddit/reddit/wiki/OAuth2-Quick-Start-Example#first-steps). The account used must be a moderator with `flair` privileges in the target subreddits.

Usage
-----

To create flair templates in /r/foo, /r/bar, and /r/baz:

    $ amupdate.py foo bar baz
