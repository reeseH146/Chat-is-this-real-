# UI with CustomTkinter : 
  ## 22/12/24
    - Like pygame, CTK can run "normally" with stuff like buttons created "sequentially" or using classes from OOP but its seems more abstracted than Pygame
    - Window and event loop is built in
    - Documentation seems pretty simple and people say its good for simple apps and prototyping
    - CTK uses "grid" to align objects on window or grids of window, weight is the portion of the window this takes up ((weight/sum of total weights) = % of window)
    - Sticky is used to stick a side of a widget onto the side/s of a grid
    - Rowspan/columnspan is how many it fills, default is 1 so fills the specified row/column and doesn't continue
    - Padx/pady is dist from each x/y side

# Networking with python sockets std : 
  ## 22/12/24
    - Sockets are endpoints of a bidirectional connection in a network, so like ports at cities
    - There are different "channel types" which is a way for these sockets to connect and communicate? (TCP / UDP / UNIX Domain Sockets)
    - Computers have ports which are numbers/locations which the device allows connections to connect to and handle individually (e.g. 80 for HTTP/HTTPS), some are already used but those over 4000 tend to be free, overwriting ports could cause conflicts with data send/recieved. Use of ports separates connections making it easier to differentiate between connections and easily manage the data to/from them.
    - Sockets are the combination of ports and local IP address to target the device and its specific port