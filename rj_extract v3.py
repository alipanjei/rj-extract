#radio javan extracter v3
#symple code to extract download links from radio javan music service, using "radiojavanapi" and "Pyperclip".
#run "pip install radiojavanapi" and "pip install pyperclip" prier to running this code
from radiojavanapi import Client
#used to interact with radio javan
import pyperclip
#used for copying text to clipboard
# Create a Client instance 
client = Client()
#try to choos the content type, for now it will be once only
content = input ('press p for podcasts, any other letter for songs: ')
#trying to make a loop for constant url extraction 
searchword = 0
selected = 1
while True :
    #enter keyword for searching
    searchword = input ( str ('please enter a keyword'))
    if searchword == 'exit' :
        break
    if content == 'p' :
        search = client.search (searchword).podcasts
    else:
        search = client.search (searchword).songs
    length = int ( len (search))
    selector = 1
    while True :
        print (f'there are {length} results. ')
        selected = selector
        selector = (int ( input ('please enter the  result number, enter 0 to go back.'))) -1
        if selector == -1 :
            break
        dict1 = dict (search [selector ])
        print ( f'name: {dict1.get ('name')}, artist: {dict1.get ('artist')}, date: {dict1.get ('created_at')}.')
        if selector == selected :
            if content == 'p' :
                podcast = client.get_podcast_by_id (dict1.get ('id'))
                print ('link copied to clipboard')
                pyperclip.copy (f' {podcast.title},\n {podcast.link}')
            else: 
                song = client.get_song_by_id (dict1.get ('id'))
                print (song.link)    
                pyperclip.copy (f' {song.title},\n {song.link}')
        else :
            continue
print ('byeBye')

