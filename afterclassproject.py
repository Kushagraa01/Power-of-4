def is_power_of_eight(number):
  if number <= 0:
    return False
  if (number & (number - 1)) != 0:
        return False
  return (number & 0x92492492) != 0
user_input = int(input("Enter your number: "))

if is_power_of_eight(user_input):
  print(f"{user_input} is a power of 8")
else:
  print(f"{user_input} is not a power of 8")