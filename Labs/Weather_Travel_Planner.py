# With the use of conditional statements, this code will determine wether commuting is possible based on the weather.

#represents the distance to travel in miles
distance_mi = 0

#represents if the user is currently experiencing rainy weather
is_raining = False

#represents if the user has a bicycle
has_bike = False

#represents if the user has a car
has_car = False

#epresents if the user has an app that allows them to request a ride
has_ride_share_app = False

# If distance_mi is a falsy value:
if not distance_mi:
  print(False)
# If the distance is less than or equal to 1 mile:
elif distance_mi <= 1:
  if not is_raining:
    print(True)
  else:
    print(False)
# If the distance is greater than 1 mile and less than or equal to 6 miles:
elif distance_mi <= 6:
  if has_bike and not is_raining:
    print(True)
  else:
    print(False)
# If the person has a car or has a ride-share app
else:
  if has_car or has_ride_share_app:
    print(True)
  else:
    print(False)
