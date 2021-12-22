# yandere-dl

currently just a image board downloader that provides you the highest quality sauce byte by byte to ensure you get every pixel of those anime ti-----. Hmm, odd. Somebody cut me off there. . . Anyways, let us proceed.

# SUPPORTED SITES

DISCLAIMER: Visiting any of these sites will result in exposure to adult content. This tool is meant for those of age 18 and older.

yande.re
danbooru
gelbooru

# EASIEST WAY TO GET YANDERE-DL (FOR WINDOWS USERS)

For Windows users, the easiest way is to download the [latest executable file from the Releases tab](https://github.com/0xSTAR/yandere-dl/releases/download/v1.0.0/yandere-dl.exe). From there, move the executable file into any directory of your choosing (it is recommended to create a dedicated folder for yandere-dl). Then, double click the executable to open it, and a prompt will appear. Next you must provide a search term, a rating, the order, and the amount of pages you would like (each page is ~40 images). You can leave these blank to have them at their default values. This goes without saying, but press enter afterwards.

To actually use this, make sure to read below, and yes, [take this shortcut to get there faster](https://github.com/0xSTAR/yandere-dl#actual-usage-of-yandere-dl) because the next section is explaining how to use it from source.

# FROM SOURCE

Note: Getting the source from the repository may not always result in a working version of yandere-dl, so it is advisable to get a source release from the Releases tab if cloning the repository results in failure of the application.

This requires that you have Python 3.6 or newer installed. If you do not already have Python installed, you can get it from the [official website](https://www.python.org/).
When installing make sure to check the option "Add to PATH"

Clone the repository, or easier if you aren't experienced with this kind of thing: [download from the web interface](https://github.com/0xSTAR/yandere-dl/archive/refs/heads/main.zip)

Extract from the zip.

Open up a command prompt, terminal, or whatever you got on your operating system.
Change directories into that folder.

If you do not know how to do these things, it is expected of you to already know how . . . so go watch some videos or read some documentation if you must.

```
cd UNTIL/YOU/GET/TO/THAT/YANDERE-DL/FOLDER...
```

Once you are there, you can do one of three things . . .

If you are on Linux you can run the 'build.sh' shell script. Do keep in mind, it is not guaranteed to work and will require your super user password during it's execution. But if it does work, then that's great!

```
./build.sh
```

Or . . .

Run the 'build.py' script to create a binary for your operating system like so...

On Windows . . .
```
python build.py
```

On Mac or Linux . . .
```
python3 build.py
chmod +rwx ./dist/yandere-dl
```
If you have any issues. . . Check how to properly install pyinstaller to your machine on Mac or Linux and then run the build.py script again.


OR ... !

Windows: Run yandere-dl straight from the 'yandere-dl.py' file like so . . .
```
python yandere-dl.py
```

or for Linux and Mac users. . .
```
python3 yandere-dl.py
```


# ACTUAL USAGE OF YANDERE-DL

This script downloads images specifically available on the [yande.re](https://yande.re/), [danbooru]() and [gelbooru]() image boards.

So, all tags used are specific to that website. I suggest you visit it and get used to the tags and conventions if you are not already (even though this script is most likely to be used by people who already use yande.re and want an easier way of saving the images offline)

yandere-dl will ask for these 4 specificities:
- 1. Search term or better known as 'tag(s)'
- 2. Rating (safe, explicit, questionable)
- 3. Order (rank, score)
- 4. Pages ( any number >= (greater than or equal to) 1 )

Here is an example of a simple query to yandere-dl:
- Search: girls_und_panzer seifuku
- Rating:
- Order:
- Pages:

EXPLAINING what this query would do:

For the Search:
This search used both the tags 'girls_und_panzer' and 'seifuku'. To use multiple tags make sure to put a ' ' (space) in between.
Leaving this value blank, just like the others are would not break the script. It would just allow to search from all available images.

For the Rating:
Leaving the rating blank leaves the query open to receieve images from all ratings. This was to demonstrate that. Of course, this means that supplying 'safe','explicit', or 'questionable' would narrow down the query to just images with those ratings.

For the Order:
Leaving the order blank defaults to 'rank', the default of the site. Rank is the current ranking of an image based on the day, I believe. Supplying 'score' will query for the best image by score over all of time.

For the Pages:
Leaving pages blank will result in only one page of search results being downloaded (each page is ~ (about) 40 images). Only values >= (greater than or equal to) 1 are accepted for the amount of pages.

As you may notice, all of these values can be left blank to be set to their defaults.


It is highly recommended to continue reading to find out more effective ways of utilizing yandere-dl. Make sure to check anytime you obtain a new release, as the methods of using yandere-dl may have been vastly improved, while deprecating the old, less user-friendly things.

# USAGE CONTINUED...

  - yande.re, danbooru and gelbooru downloaders support using the keywords 'e', 'q', and 's' as shorthand for 'explicit', 'questionable' and 'safe'.

  - Gelbooru uses the term 'Sort' rather than 'Order'

# MORE

Coming soon . . .
