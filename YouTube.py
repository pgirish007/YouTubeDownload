from pytube import YouTube
import sys
import os

def main(argv):
	if (len(argv) < 2):
		print("Youtune URL is missing in the input")
		sys.exit(2)
		
	cwd = os.getcwd()
	print(cwd)
	for arg in argv[1:]:
		try:
			yt = YouTube(arg)
			stream = yt.streams.get_highest_resolution()
			stream.download(cwd + "/downloaded")
		except:
			print("Error occured")
			
		
if __name__ == "__main__":
	main(sys.argv)
	print("Task completed")