MEETUP_API_KEY=
RAW="rsvps-$(date +%Y-%m-%d).json"
ATTENDEES="attendees-$(date +%Y-%m-%d).txt"

if [[ -n "$1" ]]; then
   curl "https://api.meetup.com/2/rsvps?key=${MEETUP_API_KEY}&sign=true&rsvp=yes&event_id=$1&page=100" > $RAW

   python create.py $RAW > $ATTENDEES
   cat extras.txt >> $ATTENDEES

   echo "Attendees are in $ATTENDEES"
else
   echo "usage: get.sh event_id"
fi
