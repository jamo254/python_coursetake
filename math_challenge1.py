# Given  a MathOp()  function try the following calculations
# 3 / 2
# 3 // 2
# 3 % 2
# 3 ** 2

def MathOp():
  division = 3 / 2
  floor_division = 3 // 2
  modulus = 3 % 2
  power = 3**2
  return [division, floor_division, modulus, power]

[division, floor_division, modulus, power] = MathOp()

print(division)
print(floor_division)
print(modulus)
print(power)

#Challenge 2

# Given  a Challenge()  function try the following calculations
# 3 + 2
# 3 - 2
# 3 // 2
# 3 ** 3
    

def Challenge():
    #declare variables
  addition = 3 + 2
  sub = 3 - 2
  floorDivision = 3 // 2
  power = 3 ** 3
  return [addition, sub,floorDivision, power] 

[addition, sub, floorDivision, power] = Challenge()

print('Addition', addition)
print('Sub:', sub)
print('Floor division:', floorDivision)
print('Power:', power)





    





