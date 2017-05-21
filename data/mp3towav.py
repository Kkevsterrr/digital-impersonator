import argparse
import os

try:
	from ffmpy import FFmpeg
except ImportError:
	import pip
	pip.main(["install", "ffmpy"])
	from ffmpy import FFmpeg

def convert(fileName, savedir):
	print 'Converting ' + local_filename
	ff = FFmpeg(inputs={(fileName+'.mp3'): None},outputs={os.path.join(savedir, fileName+'.wav'): None})
	#print ff.cmd
	try:
		ff.run()
	except:
		print 'Err running ' + ff.cmd + ', please try again.'

def make_dir(path):
    try:
        os.makedirs(path)
        print 'New directory made at ' + path
    except OSError:
        if not os.path.isdir(path):
            raise

if __name__ == "__main__":
	dir_path = os.path.dirname(os.path.realpath(__file__))
	new_path = os.path.join(dir_path, 'WAV')
	make_dir(new_path)
	for filename in os.listdir(dir_path):
		local = filename.split('.')
		local_filename = local[0]
		local_ext = local[-1]
		# Check to see if wav exists
		if os.path.isfile(os.path.join(new_path, local_filename+'.wav')):
			print local_filename+'.wav already exists'
		else:
			if local_ext == "mp3":
				convert(local_filename,new_path)
