import time
import sys 
import os
import math 

drill_movement = "\n\nPractice movement (dashdancing, shorthopping, wavelanding, wavedashing, on battlefield)\n"
drill_shuffl = "\n\nPractice Shuffl'd Nairs and drill shines, on air and on shield\n"
drill_waveshine ="\n\nPractice waveshining on FD\n"
drill_shielddrop = "\n\nPractice shield dropping on battlefield\n"
drill_ledgestall = "\n\nPractice ledgestalling(up-b stall)\n"
drill_SHL = "\n\nPractice short hop laser\n"
drill_ledgeairs = "\n\nAerials off of a ledge\n"



def drill_timer(drill_name,drill_time):
	print drill_name
	original_time = drill_time
	while drill_time >= 0 :
		time.sleep(1)
		sys.stdout.write('\r ' + str(drill_time)+ ' second(s)'+'           ') #add extra spaces after drill time so that nubmers don't overwrite eacho tehr
		sys.stdout.flush() # important
		drill_time -= 1 
	return original_time

def drill_cooldown(drill_name):
	print "\n\nNext drill (%s) in: \n" % drill_name
	for n in range(0,15):
		time.sleep(1)
		sys.stdout.write('\r ' + str(15-n)+' second(s)'+'           ')  #prefix with \r so that line is rewritten.
		sys.stdout.flush() # important
		n += 1

def sec_to_min(total_time):
	sec_time = total_time%60
	minute_time = int(math.floor(total_time/60))
	real_time = str(minute_time) + ' minutes and ' + str(sec_time) + ' seconds'
	return real_time

try:
	# Win32
	from msvcrt import getch
	print "\n Press any key to start SSBM Fox training!"
	getch()

	total_time = 0

	total_time += drill_timer(drill_shuffl,120) 
	drill_cooldown("Waveshine Practice")
	total_time += drill_timer(drill_waveshine, 300)
	drill_cooldown("ShieldDropping")
	total_time += drill_timer(drill_shielddrop, 60)
	drill_cooldown("LedgeStalling")
	total_time += drill_timer(drill_ledgestall,60)
	drill_cooldown("LedgeAirs")
	total_time += drill_timer(drill_ledgeairs,60)
	drill_cooldown("Shuffl'd Nairs")
	total_time += drill_timer(drill_shuffl,120)
	drill_cooldown("ShortHopLasers")
	total_time += drill_timer(drill_SHL,120)

	print("\n\nTotal Drill Time Elapsed: " + sec_to_min(total_time) + ". Good Job!\n")
	print "\n Don't forget your match analysis! :)\n"

except:
	print"lazar"
try:
	os.system('pause')
except:
	print"Lazar\n"