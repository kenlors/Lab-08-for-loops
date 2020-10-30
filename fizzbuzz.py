usernum = int(userinput)
if usernum < 1:
  print("Invalid")
else:
    for i in range(usernum, 0, 101):
    print(i)
    if i % 3 == 0:
      print("Fizz")
    if i % 5 == 0:
      print("Buzz")
    if i % 3 && 5 == 0:
      print("FizzBuzz")
