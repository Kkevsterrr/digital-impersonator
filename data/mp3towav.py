import os
import time

try:
	from ffmpy import FFmpeg
	import progressbar
except ImportError:
	import pip
	pip.main(["install", "ffmpy"])
	pip.main(["install", "progressbar2"])
	from ffmpy import FFmpeg
	import progressbar


tot_num = 0
curr_count =0

def convert(fileName, savedir):
	#print '\x1b[4;32;40m' +'\r' +'Converting ' + local_filename +'\x1b[0m'
	ff = FFmpeg(inputs={(fileName+'.mp3'): '-hide_banner -loglevel panic'},outputs={os.path.join(savedir, fileName+'.wav'): None})
	#print ff.cmd
	try:
		ff.run()
	except:
		print '\x1b[4;30;41m' + 'Err running ' + ff.cmd + ', please try again.'+ '\x1b[0m'

def make_dir(path):
    try:
        os.makedirs(path)
        print '\x1b[4;32;40m' + 'New directory made at ' + path + '\x1b[0m'
    except OSError:
        if not os.path.isdir(path):
            raise

#adding progress bar since this process takes such a long time
def get_count(path):
	global tot_num
	for filename in os.listdir(dir_path):
		local = filename.split('.')
		local_ext = local[-1]
		if local_ext == "mp3":
			tot_num += 1	

if __name__ == "__main__":
	dir_path = os.path.dirname(os.path.realpath(__file__))
	new_path = os.path.join(dir_path, 'WAV')
	make_dir(new_path)
	get_count(dir_path)
	#print 'Num ber of mp3 files to convert: ' + str(tot_num)
	with progressbar.ProgressBar(widgets=[
    ' [', progressbar.Timer(), '] ',
    progressbar.Bar(), ' (' ,progressbar.SimpleProgress(),') '
    ],
	max_value=tot_num) as bar:
		for filename in os.listdir(dir_path):
			local = filename.split('.')
			local_filename = local[0]
			local_ext = local[-1]
			# Check to see if wav exists
			curr_count += 1
			if os.path.isfile(os.path.join(new_path, local_filename+'.wav')):
				print '\x1b[4;31;40m' + local_filename+'.wav already exists' +'\x1b[0m'
			else:
				if local_ext == "mp3":
					convert(local_filename,new_path)
			bar.update(curr_count)
