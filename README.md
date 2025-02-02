# **spotify downloader**  
## Here is a simple presentation of how to use it  





  
### **project description**  
➢ Spotify downloader allows downloading spotify playlists to your computer.  

  
### **how to install it ?**
➢ Step 1 :  
➀ download python from the official website with a version higher than 3.10.  
➁ open cmd and check that python and pip are present like this: **python --version** and **pip --version**.  
➂ in the cmd download the dependencies like this: **pip install colorama** , **pip install spotipy** and **pip install yt_dlp**  

➢ Step 2 :  
➀ download the downloader.py and the info.json in the same folder.  
➁ go to 'spotify dashboard developer' to create an application (for the redirection url use this one http://localhost:8888/callback).  
➂ copy the client id and client secret then paste them into the info.json file at the indicated location. (if you don't have an editor use open with + notepad).  
➃ run the downloader.py and follow the instructions, the downloaded music will be automatically added to the folder where the program is located.


### **How does it work?**
➢ the program retrieves the link of the spotify playlist provided by the user and adds in a list the names and author of the songs, then the program will search and download the audios from youtube with the best format proposed until having gone through the entire list of music.    

### **next update **  
➢ more download option (solo download, types of format, and others).  
➢ increased limit of 100 downloads per call.  
