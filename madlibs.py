def main():
	# write your code here
	time= input("Enter a number from 1 to 12:")
	time2=int(time)
	items= input("Enter a noun (plural):")
	name=input("Enter a name: ")
	name2=name.capitalize()
	scream=input("Enter any sentence:")
	scream2=scream.upper()
	v=input("Enter a verb:")
	print()
	print("The story goes...")
	print()






	print("It was %d o'clock when I heard a knock at the door."%(time2))
	print( "I opened the door and there was a box full of %s with a note saying \"From Mr. %s.\""%(items,name2))
	print("Just as I closed the door I heard a scream \"%s.\" "%(scream2))
	print("I froze in place and all I could do was %s."%(v))




if __name__ == '__main__':
	main()
