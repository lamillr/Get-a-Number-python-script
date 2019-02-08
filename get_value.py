def get_value(prompt, value_min, value_max):
    while True:
        number_text = input(prompt)
        try:
            number = int(number_text)
        except ValueError:
            print('Invalid number. Please enter digits.')
            continue #return to the top of the loop
        if number<value_min:
            print('Value too small')
            print ('The minimum value is', value_min)
            continue
        if number>value_max:
            print('Value to large')
            print ('The maximum value is', value_max)
            continue
        #If we get here the number is valid
        #return it
    return number

ride_number=get_value(prompt='Please enter the ride number you want:',value_min=1,value_max=5)
print('You have selected:', ride_number)
