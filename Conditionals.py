userReply = input("Do you need to ship a package? (Enter yes or no) ")
if userReply == "yes":
    print("We can help you ship that package!")
else:
    print("Please come back when you need to ship a package. Thank you.")
userReply = input("Would you like to buy stamps, buy an evenlope, or make a copy? (Enter stamps, envelope, or copy) ")
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply =="envelope":
    print("We have many evelope sizes to choose from.")
elif userReply == "copy":
    copies = input("how many copies would you like? (Enter a number) ")
    print("Here are {} copies. ".format(copies))
else:
    print("Thank you, please come again")
    