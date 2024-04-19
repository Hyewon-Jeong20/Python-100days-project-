# # # student_scores = {
# # #     "Harry" : 81,
# # #     "Ron" : 78,
# # #     "Hermione" : 99,
# # #     "Droaco" : 74,
# # #     "Neville" : 62
# # # }
# # #
# # # student_grades = {}
# # #
# # # for student in student_scores :
# # #     print(student)
# # #     score = student_scores[student]
# # #     print(score)
# # #     if score > 90 :
# # #         student_grades[student] = "Outstanding"
# # #     elif score > 80 :
# # #         student_grades[student] = "Excceds Expectation"
# # #     elif score > 70 :
# # #         student_grades[student] = "Acceptable"
# # #     else :
# # #         student_grades[student] = "Fail"
# # # print(student_grades)
# # #
# # #
# # #
# #
# # capitals = {
# #     "France" : "Paris",
# #     "Germany" : "Berlin"
# # }
# # #Nesting a List in a Dictionary
# # travel_log = {
# #     "France" : ["Paris", "Lille", " Dijion"],
# #     "Germany" : ["Berilin", "Hamburg", "Stuttgart"]
# # }
# #
# # #Nesting Dictionary in a Dictionary
# # travel_log = {
# #     "France" : {"citis_visited" : ["Paris", "Lille", "Dijion"], "total_visits" : 12},
# #     "Germany" : {"citis_visited" : ["Berilin", "Hamburg", "Stuttgart"], "total_visits" : 20}
# # }
# #
# # #Nesting Dictionary in a List
# #
# # travel_log = {
# #     {
# #      "contry" : "France",
# #      "citis_visited" : ["Paris", "Lille", "Dijion"],
# #      "total_visits" : 12
# #     },
# #     {
# #      "country" : "Germany" ,
# #      "citis_visited" : ["Berilin", "Hamburg", "Stuttgart"],
# #      "total_visits" : 20
# #     },
# # }
# #
# #
#
#
# country = input() # Add country name
# visits = int(input()) # Number of visits
# list_of_cities = eval(input()) # create list from formatted string
#
# travel_log = [
#   {
#     "country": "France",
#     "visits": 12,
#     "cities": ["Paris", "Lille", "Dijon"]
#   },
#   {
#     "country": "Germany",
#     "visits": 5,
#     "cities": ["Berlin", "Hamburg", "Stuttgart"]
#   },
# ]
# # Do NOT change the code above 👆
#
# # TODO: Write the function that will allow new countries
# # to be added to the travel_log.
# def add_new_country(name, time_visited, cities_visited) :
#   new_country = {}
#   new_country["country"] = name
#   new_country["visits"] = time_visited
#   new_country["cities"] = cities_visited
#   travel_log.append(new_country)
#
# # Do not change the code below 👇
# add_new_country(country, visits, list_of_cities)
# print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
# print(f"My favourite city was {travel_log[2]['cities'][0]}.")

# from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
bid_dictionary = {}
bidding_finished = False

def find_highest_bidder(bidding_record) :
    highest_bid = 0
    winner = ""

    for bidder in bidding_record :
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid :
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished :
    name = input("What is your name?")
    price = int(input("What is your bid: $"))
    bid_dictionary[name] = price
    should_continue = input("Do you have other user? Type '"'Yes'"' or '"'No'"'\n")
    if should_continue == "no" :
        bidding_finished = True
        find_highest_bidder(bid_dictionary)
    # elif should_continue = "yes" :
    #     cleaer()

