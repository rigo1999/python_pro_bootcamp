# love calculator
print("The Love Calculator is calculating your score...")
name1 = input("What is your name?")
name2 = input("What is their name?")
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
name = (name1 + name2).upper()
tr_ue = 'TRUE'
lo_ve = 'LOVE'
count_true = 0
count_love = 0
for t in range(len(tr_ue)):
    for letter in range(len(name)):
        if tr_ue[t] == name[letter]:
            count_true += 1

for l in range(len(lo_ve)):
    for leta in range(len(name)):
        if lo_ve[l] == name[leta]:
            count_love += 1
#sting concatenation to get the two digits
score = str(count_true) + str(count_love)

if int(score) < 10 or int(score) > 90:
    print(f"Your score is {socre}, you go together like coke and mentos.")
elif int(score) in range(40,50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")


