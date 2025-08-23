def is_power_of_four(number):
  if number <= 0:
    return False
  is_power_of_two = (number & (number - 1)) == 0
  if not is_power_of_two:
    return False
  return (number & 0x55555555) != 0

user_input = int(input("Enter your number: "))

if is_power_of_four(user_input):
  print(f"{user_input} is a power of 4")
else:
  print(f"{user_input} is not a power of 4")