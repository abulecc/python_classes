  # #how maany seconds are there in 42 minutes 42 seconds

# x = 60 * 42 
# x = 2520 + 42

# print(x)

# # how many miles are there in 10 kilometer? HINT; there are 1.61 kilometer in a mile

# x = 10 / 1.61

# print(x)

# #  if you run 10 kilometer in 42 mins 42 seconds what is the average pace time per mile in minutes and seconds? what is the average speed in mile per hour

# x_average_pace = 42.7 / 6.211180
# print(x)

# m_average_speed = 42 + (42/60)   
# print (m_average_speed)

# s_distance = (42*60) + 42 
# print (s_distance)

# #Recall 1 mile = 1.61km
# x = 10 
# x = 10/1.61
# print(x)

# #in terms of miles/mins
# x = 6.21/42.7
# print(x)

# #in terms of miles/minutes

# x = 6.21/2562
# print(x)

# x = 42.7/60
# print(x)

# x = 6.21/0.71
# print (x)

# # The volume of sphere with radius (r) is 4/3 pie r square. what is the volume of 
# # sphere with radius 5?

# pi = 3.142
# r = 5 
# volume = 4/3 * pi * r**3
# print(volume)

#Queestion 5
# normal_price = 24.95
# discount = 0.40 * normal_price
# sale_price_per_book = normal_price-discount
# total_price = sale_price_per_book*60
# first_book_shipping = 3
# other_book_shipping = 0.75
# total_shipping_cost = 3 + (0.75*59)
# wholescale_price = (total_price + total_shipping_cost)
# print(wholescale_price)

# Question 6

start_time = (6*60 + 52) *60
easy_pace = (8*60 + 15) * 2
tempo_pace = (7*60 +12) * 3

run_time = easy_pace+tempo_pace
home_time = start_time+run_time
breat_fast_hour = (home_time//3600)
break_fast_min = (home_time%3600) // 60
break_fast_sec = (home_time%3600) % 60

print(f"{'break_fast_hour'}:{break_fast_min}:{break_fast_sec}am")

