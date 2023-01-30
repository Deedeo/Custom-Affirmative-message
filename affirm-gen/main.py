print("\033[1;32;40m", "Hello Welcome to your", "\033[1;32;40m",
      "daily affirmation generator.", "\033[0m")
username = input("Enter your Username>  ")

if username == "David" or username == "david":
  print("Hi David")

  today = input("Which day of the week is today? ")
  if today == "monday" or today == "Monday":
    print("Start the week strong!", username)

  if today == "tuesday" or today == "Tuesday":
    print("Tackle this", today, "with enthusiasm!", username)

  if today == "Wednesday" or today == "wednesday":
    print(username, "Hump day is halfway there!")

  if today == "Thursday" or today == "thursday":
    print("Almost to the weekend! Enjoy your day", username)

  if today == "Friday" or today == "friday":
    print("it's that time", username, "to celebrate the end of the week!")

  if today == "Saturday" or today == "saturday":
    print("Enjoy your well-deserved day off!", username)

  if today == "Sunday" or today == "sunday":
    print(username, "C'mon don't feel lazy lets go for", today, "service!")

elif username == "tony" or username == "Tony":
  print("Hi", username)
  today = input("Which day of the week is today? ")
  if today == "monday" or today == "Monday":
    print("Make the most of a brand new week!", username)

  if today == "tuesday" or today == "Tuesday":
    print("Embrace the opportunities ahead!", username)

  if today == "Wednesday" or today == "wednesday":
    print(username, "Hump day is a sign of progress!")

  if today == "Thursday" or today == "thursday":
    print("One more day to the weekend!", username)

  if today == "Friday" or today == "friday":
    print(username, "Let's finish the week on a high note!")

  if today == "Saturday" or today == "saturday":
    print("Time for some well-deserved rest and relaxation!", username)

  if today == "Sunday" or today == "sunday":
    print(username,
          "A chance to go to church and recharge for the week ahead!")
else:
  print("Sorry User not found please enjoy the rest of your day!")
