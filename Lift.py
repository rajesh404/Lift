import random

#The seed value below ensures that the random values remain same over different executions.
random.seed(0)

lifts = [random.randint(-2,50), random.randint(-2,50), random.randint(-2,50)]
weights = [random.randint(25,500), random.randint(25,500), random.randint(25,500)]
button = int(input())
random_lift = random.randint(0,2)
lift_sent = 0
diff = [abs(lifts[0]-button), abs(lifts[1]-button), abs(lifts[2]-button)]

#Comparing them
if diff[0]>diff[1] and weights[1]<550:
    lifts[1] = button
    weights[1] = random.randint(25,120)
    lift_sent = "number 2"
    print("Lift 2 is coming for you. Please wait.")
elif diff[1]>diff[2] and weights[2]<550:
    lifts[2] = button
    weights[2] = random.randint(25,120)
    lift_sent = "number 3"
    print("Lift 3 is coming for you. Please wait.")
elif diff[1]>diff[0] and weights[0]<550:
    lifts[0] = button
    weights[0] = random.randint(25,120)
    lift_sent = "number 1"
    print("Lift 1 is coming for you. Please wait.")

#The else statement here helps to choose a lift in-case any two lifts 
#are in the same situation, like, having same floor and/or weights
else:
    lifts[random_lift] = button
    weights[random_lift] = random.randint(25,120)
    lift_sent = "number "+random_lift
    print("Lift",random.randint(1,2), "is coming for you. Please wait")

print()
print("------Below are some useful data------")
print("Lifts' current floor:",lifts)
print("Lifts' current weight:", weights)
print("Your current floor:", button)
print("Random lift number is:", random_lift)
print("closest lift values are:", diff)
print("The lift sent is :", lift_sent)
