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

usernum1 = int(raw_input())
userinput = raw_input()

for x in range(usernum1):
    print "Oh... next time bring some patients then!"
    userinput = userinput - 1
    
    if usernum1 >= 1:
        print "Have you been sick for the past 24 hours?"
    else:
        print "Then you are none of my concern! Leave my sight!"
        
    if userinput == "yes":
        print "What is your temperature?"
    else:
        print "Then you are none of my concern! Leave my sight!"
        
    if usernum1 > 102:
        print "Have you recently traveled to West Africa?"
    else:
        print "Then you are none of my concern! Leave my sight!"
        
    if userinput == "yes":
        print "Ebola! Ebola! Ebola!"
    else:
        print "Oh, well then you must not have ebola..."
        
    userinput = userinput - 1
    
print "Now go die in a hole."
