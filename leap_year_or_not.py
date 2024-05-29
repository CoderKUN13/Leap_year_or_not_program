year = int(input("Enter the year: "))


if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("This is a Leap year")
    else:
      print("This is not a Leap year")
  else:
    print("Leap year")
else:
  print("This is not a Leap year")
