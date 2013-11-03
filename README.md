Mukioplayer-Py-Mac-1.200.04
===========================
This is a solution of the damn fact that Mac, one of the best OS in human history, does not have a reliable and nice video commit software.

Written in Python, based on Mukioplayer, this is a quick way to enjoy commit(DanMu) on Mac.

Download
------
I will upload every version here: https://sourceforge.net/projects/mukioplayerpymac/

However, feel free to download here via ZIP. I just want to provide you a way to download all the old versions.

Usage
------
Download all the files, extract into one folder. Personally I do not suggest you go anywhere above ‘~’, for you would meet all kinds of privilege problems, which I suppose would drive you mad.

Make sure you have a web browser which can play Flash.

Make sure you use Python 2.7 (this is provided along with OSX), and run ‘python server.py’.

After “Vid”, drag in the video file you would like to play. Generally speaking, .flv, .hlv, .mp4 files would be fine, however, there ’s no guarantee that they can play in this player. And don’t blame me for that: Personally, I am sure that videos with H.264+AAC won’t have any problem, which would include most of the online videos. Remember to put a   ‘   before and after you drag the file. Enter.

For XML, drag in the XML file. Commit files from Bilibili would be OK, which had beed tested, while those from other sites are pending test. Please tell me the test result you have, this would be very helpful, and hereby I thank you in advance for your help. Enter.

Now the browser would open by herself, enjoy it!

After you use it, BE SURE to input Ctrl+C in the bash window!

Things you should know
-----

Please do not include anything besides characters or numbers in your folder or filename. There ’s no guarantee that symbols would be cool.

Make sure you use Python 2.7, 3.3 won’t work for it doesn’t have some important network modules.

This software is not made for playing anything above the folder “~”. Don’t get surprised if it gives you funny results.
(Update: Now it should can play things regardless the original location.)

I am completely new to Python and programming, so do please help me to improve this, and I would appreciate it very much.

About me
-----
Beining, CDC of ACI-CFG, 1st year CS student of UT.

Get in touch with me via cnbeining[at]gmail.com  .

Copyleft
-----
A number of opensource codes are used in this little project,especially the main programme, Mukioplayer. The website of Mukioplayer is https://code.google.com/p/mukioplayer/  ,MIT License.

The part of web server is from http://yige.org  .

This project is uses MIT licence. 

Update history
-----
,04: Change the way to load the player to make it able to full screen.

.03: Change the way to start server to make it safer(also slower, sorry)

.02: ???

.01: First version
