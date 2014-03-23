from gmusicapi import Mobileclient
import sys, csv

if len(sys.argv) != 3:
  print 'usage gmusicexporter.py email_address password'
  sys.exit(1)

outputFile = open('GMusicPlaylists.csv', 'w')
csvWriter = csv.writer(outputFile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

api = Mobileclient()
if api.login(sys.argv[1], sys.argv[2]) == False:
  raise Exception('Incorrect email and/or password')

library = api.get_all_songs()
csvWriter.writerow(['title', 'artist', 'album'])
for track in library:
  track['title'] = track['title'].encode('utf-8')
  track['artist'] = track['artist'].encode('utf-8')
  track['album'] = track['album'].encode('utf-8')

  csvWriter.writerow([track['title'] , track['artist'] , track['album']])
outputFile.close()

print 'Done'
print 'Your library is saved in "GMusicPlaylists.csv"'
