#!/usr/bin/python2

print "NELNUMBERS by @nvemb3r"
print "----------------------"

current_int = 0
area_code = 0
is_valid = False

while is_valid is False:

	try:
		# Ask for the target area code
		area_code = raw_input("Area Code? : ")

		# If the input is a three digits
		if len(area_code) == 3 and int(area_code):
		
			# Input is valid
			is_valid = True
		else:
			# Input is invalid
			is_valid = False
			print "Please enter a valid area code"

	except ValueError:
		# Otherwise, it is invalid
		is_valid = False

		# Tell user to try agian
		print "Please enter a valid area code"

while (current_int < 9999999 + 1):
	print str(area_code) + str(current_int)
	current_int = current_int + 1
