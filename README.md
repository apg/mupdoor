Sometimes, I need to present a list of RSVP'd members to our hosts for
Hack and Tell. So, some time ago, I hacked this shit together to do
that.  It attempts to output a person's name in plain text, and
assumes that you have a question in which you ask for them to put
their full name down.

    $ sed -i s/MEETUP_API_KEY=/MEETUP_API_KEY=<insert your meetup api key here>/ get.sh
    $ ./get.sh <meetup event id>

That should more or less do it...


## RAQs

### Why didn't you make the API call in the python script?

I originally thought I could do the whole thing in shell, but rather
than spend any more time on it, I just decided to call into Python,
which has much more expressive string handling (and JSON support).

### Hey! This thing doesn't work!

WFM, YMMV. Feel free to open an issue. I may be inclined to rewrite
this if someone finds it actually useful.
