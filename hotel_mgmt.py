hotel = {
  '1': {
    '101': ['George Jefferson', 'Wheezy Jefferson'],
    
  },
  '2': {
    '237': ['Jack Torrance', 'Wendy Torrance'],
  },
  '3': {
    '333': ['Neo', 'Trinity', 'Morpheus']
  }
}
# using the start hotel above client can check in or check out of hotel
def hotel_check():
    check_in = input("Hi, please type 'check in' if checking in or 'check out' if checking out,")
    floor_number = str(input('Please enter your floor number:'))
    room_number = str(input('Please enter your room number'))
    print(floor_number)
    print(room_number)
    
    #  trys the floor number and if floor_number is in hotel it continues if not it asks if user wants to rety:
    try:
      if floor_number == hotel[floor_number]:
        pass
      #if person is checking out delete their room so others can stay
      if check_in == 'check out':
      # ensuring that the room they entered has occupants    
          if hotel[floor_number][room_number]:
            # delete occupants from room
              del hotel[floor_number][room_number]
              print("Thank you for checking out! Please come and stay with us again!")
              return hotel
          else:
            # prints message to inform user that room is vacant
              print("Sorry, that room is already vacant")
              # prompt user to see if they want to restart
              try_again = input("Would you like to try again?(yes/no) ")
              # if they want to restart it prompts first questions again 
              if try_again == 'yes':
                  hotel_check()
                  # if they dont want to retry it ends program
              else:
                  return
      elif check_in == 'check in':
          # if they want to check in we have to make sure the room is empty first by checking if that room exists
          # if the room isnt in the hotel then the user can check in
          # this does allow user to enter any room number and this will work as long as it is not occupied
          if room_number not in hotel[floor_number]:
            # we ask user for number of occupants to know how many names to ask for
            number_of_occupants = int(input('Please enter the number if occupants? '))
            print('You will be prompted to enter the name of each occupant')
            occupant_list = []
            # asks for each occupants name so that we can enter them into the room
            for i in range(number_of_occupants):
              full_name = str(input('Please enter occupants name: '))        
              occupant_list.append(full_name)
            hotel[floor_number][room_number] = occupant_list
          else:
            # if the room does show up it is occupied so we let the user know
            print("I'm sorry but that room is already occupied.")
            # prompt user to see if they want to restart
            try_again = input("Would you like to try again?(yes/no) ")
            # if they want to restart it prompts first questions again 
            if try_again == 'yes':
              hotel_check()
            else:
              return
    except KeyError:
      # if the floor isnt in the hotel we tell user 
      print('Sorry that is not a valid floor ')
      # ask user if they want to re-try
      re_try = input('Would you like to try again?(yes/no) ')
      # if they want to retry we reprompt them from the start
      if re_try == 'yes':
        hotel_check()
      else:
        # if they dont want to retry it ends program
        return
            
    print(hotel)    
hotel_check()
