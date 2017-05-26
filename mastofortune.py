#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, time
import codecs
#UTF8Writer = codecs.getwriter('utf8')
#sys.stdout = UTF8Writer(sys.stdout)

from mastodon import Mastodon

def get_fortune(db):
	return "".join(os.popen("fortune "+db).readlines())

if(len(sys.argv)<=4):
	sys.stderr.write("Usage: mastofortune client_token_file user_token_file api_base_url fortune_database\nSee https://mastodonpy.readthedocs.io/en/latest/ for information about how to create token files\n")
	sys.exit(1)

mastodon=Mastodon(sys.argv[1], access_token=sys.argv[2], api_base_url=sys.argv[3])
db=sys.argv[4]

while True:
	status=get_fortune(db)
	print(status)
	mastodon.status_post(status)
	time.sleep(600)

