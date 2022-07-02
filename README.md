# YouTubeDownload
This script helps to download any open public videos from you tube using Python as base

Steps:

download pytube and install it

#Mac instructions

update Python to latest:

brew install python

cd "/Applications/Python <Latest version>"

You will need to make sure you have certificate setup for the youtube URLs
sudo "./Install Certificates.command"

pip install pytube

Once all setup

Command to run:

python YouTube.py "<YouTube URL>"

This is going to pull the video and store in the download folder in the same directory where the python script it.
