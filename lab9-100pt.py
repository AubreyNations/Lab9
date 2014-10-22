############################################
#                                          # 
#                   100pt                  #
#             Patient Diagnosis            #
############################################

# Create a program that tests if patients needs to be admitted to the hospital.
# Ask the user for their temperature, and if they have been sick in the last 24 hours.
# Additionally, ask if the user has recently travelled to West Africa.
# The program should continue to run until there are no patients left to diagnose (i.e. a while loop).

# Criteria for Diagnosis:
# - A temperature of over 105F
# - A temperature of over 102F and they have been sick in the last 24 hours
# - A temperature over 100, OR they've been sick in the last 24 hours, AND they've recently travelled to West Africa.

print "How many patients are there?"

usernum = int(raw_input())

for x in range(usernum):
    print "Have you been sick for the past 24 hours?"
    sick = raw_input()

    print "What is your temperature?"
    temp = int(raw_input())

    print "Have you recently traveled to West Africa?"
    travel = raw_input()

    if temp > 105 and sick == "yes":
        print "You need to go to the hospital!"

    if temp > 102 and sick == "yes":
        print "You need to go to the hospital!"
    
    if travel == "yes":
        if temp > 100 or sick == "yes":
            print "EBOLA!!!"