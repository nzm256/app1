fuel = 10.0
addition = 5.0
efficiency = 18.0
distance = efficiency * total_fuel
destination = 200
def Fuel(fuel, addition):
  fuel += addition
  return fuel
  
def alert(destination, distance):
  if destination > distance:
    print("you need to add fuel!")
  else:
    print("you have enough fuel!")
