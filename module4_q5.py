Complete the code to iterate through the keys and values of the car_prices dictionary, printing out some information about each one.

solution:


def car_listing(car_prices):
  result = ""
  for k,v in car_prices.items():
    result += "{} costs {} dollars".format(k,v) + "\n"
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))