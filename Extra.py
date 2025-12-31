math = int(input("What did you get on your math exam?"))
science = int(input("What did you get on your science exam?"))
SS = int(input("What did you get on your SS exam?"))
english = int(input("What did you get on your english exam?"))
PE = int(input("What did you get on your PE exam?"))

percentage = (math + science + SS + english + PE)*100 / 500

print("You got", percentage)

if percentage > 90:
    print("You got a A")
elif 80 < percentage < 90:
    print("You got a B")
elif 60 < percentage < 80:
    print("You got a C")
elif percentage < 50:
    print("You got a F")


