fuel = 10.0
addition = 5.0
efficiency = 18.0
distance = efficiency * total_fuel
destination = 200
people = 3
price = 162.0

def Fuel(fuel, addition):
  fuel = fuel + addition
  return fuel

def Real_Efficiency(efficiency, people):
  if people <= 2:
    return efficiency
  else efficiency = efficiency * (1 - 0.05*people)
    return efficiency

def Alert(destination, distance):
  if destination > distance:
    print("you need to add fuel!")
  else:
    print("you have enough fuel!")
