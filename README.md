# Mybasement
A portable UHF RFID system, Utilizing Raspberry Pi 4, FM-503 w/ UHF Anttena, uesed to track large inventory location data.
Created in a strange room in my basement.

I needed to easily mess with code between my Pi and comp. I'm sure there are different ways, this was the one I chose at 11:47pm 

Thanks for hanging out in my basement. Please feel free to give input and help me add to my development toolkit.

In the words of a very famous man, "Hi draw, draw, draw"

Goals of system:

FM503comm: Communicate with an FM-503 and the 5.5dbi antenna. Found here (https://www.aliexpress.com/item/4000133201826.html)
  - Send command to Multi-Read, and do it Continuously.
  - Read outputs from reader 
  
GPS_dongle: Connect to USB GPS dongle and recieve GPS locations on command
  - determin direction of travel, adjust coordinates perpendicular to more accuratly represent location of tags

Paperclip: Data processor
  - Pairs tag id with GPS coordinates at time of read. 
  - Takes medien value of a grouping of like tag id's, find the medien GPS location, to most accuratly pinpoint tag location
  - creates data structered for Database
  
Database: Probably use Sheets
  - Update database with location of tag id and time since last scan
  - highlight items that apeared on previous scan, but not this scan (to help flag when a unit has moved or sold)
  
Application: MAP
  - Would like to create a map that will allow you to use values from the database to search for particular items. (Stock #, Year, Make, Model)
  - list items and displays on the map all available items that share the same value
  - click on specific item to get all the details
  

