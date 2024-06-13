import random
import matplotlib.pyplot as plt



print("Hello welcome to kavin world!")
print("You will have rounds to guess a number between 1 and 6. Good luck!")
result=[]
round=int(input("Enter number of rounds\n"))

def drawchart():
    xaxis=list(range(1,len(result)+1))
    plt.plot(xaxis,result)
    plt.title("Progress of the Game")
    plt.xlabel("Rounds")
    plt.ylabel('Result (1 = Success, 0 = Failure)')
    plt.xticks(xaxis)
    plt.yticks([0, 1], ['Failure', 'Success'])
    plt.show()

while round>0:
    predicted_number=int(input("Predict the number between 1 and 6\n"))
    generate_random_number=random.randrange(1,6)
    print(f"Predicted number = {predicted_number} \nGenerated number = {generate_random_number}\n")
    if predicted_number==generate_random_number:
        print("Congratulation!You scored point🥳\n")
        result.append(1)
    else:
        print("Better luck next time😊\n")
        result.append(0)
    round-=1
drawchart()
print("Have a nice day")







