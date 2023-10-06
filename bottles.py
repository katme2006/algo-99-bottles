def bottles_loop():
    #collect input
    x = input('Please enter a number of bottles: ')
    x= int(x)

    #loop through a range and print each number in the song except the last two lines where the words change
    for i in range(x,2,-1):
       print(f"{i} bottles of beer on the wall, {i} bottles of beer.\nTake one down and pass it around, {i-1} bottles of beer on the wall.")

    print(f"2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around, 1 bottle of beer on the wall.")
    print(f"1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no bottles of beer on the wall.")

#bottles_loop()


#NO LOOP

def bottles_noloop():
    #collect input
    x = input('Please enter a number of bottles: ')
    x= int(x)


    #lambda function with formatted string for each iteration that will be printed
    bottle_line_printer = lambda num: f'{num} bottles of beer on the wall, {num} bottles of beer.\n Take one down and pass it around {num-1} bottles of beer on the wall \n'

    #map will print for every iteration created by range function, and our range function starts at whatever number the user inputs
    song = map(bottle_line_printer,range(x,2,-1))

    #last two lines are exceptions
    two ='2 bottles of beer on the wall, 2 bottles of beer.\n Take one down and pass it around one bottle of beer on the wall \n'
    one ='1 bottles of beer on the wall, 1 bottle of beer.\n Take one down and pass it around no bottles of beer on the wall \n'

    #When we run song our lambda function fires on all iterations of range. We use unpacking operator to unpack/print each iteration in song's range and then print last two exception lines
    print(*song, two, one)


bottles_noloop()




