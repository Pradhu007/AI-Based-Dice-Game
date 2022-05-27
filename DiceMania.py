import random

#The Dice Class contains one method known as "roll" which  assists in simulating the roll of a dice.




class Dice:



    def __init__(self,randomsides):
        self.sides = randomsides











    def roll(self):

     return random.randint(1,self.sides)






obj = Dice(6) #Creating an object to call methods and athributes  from the Dice  class. Also included customization which allows the user to change the sides of the dice according to their choice


def welcome():
    print("..............................................................................")
    print("................................WELCOME TO DICE MANIA.........................")
    print(".................................BY PRADHU007.................................")

welcome()

playername = input("What would you like the program to call you as?")


randombotnames = ["Funkyman123","PerryPicker","Market23","Joseph123","iambetterthanyou"]
botname = random.choice(randombotnames)
#Randomly picks a name for the bot from the list of names  using the choice method from the random class.




#The checkforwinner function is used for determining the final winner. It takes the playerscore and the botscore for parameters and uses a list of conditions to determine the final winner of the overall rounds player
def checkfinalwinner(playerscore,botscore):



    if playerscore > botscore:

        return "The overall winner is {} ! ".format(playername)

    elif playerscore < botscore:
        return "Game Over, Unfortunately  the bot  {} has won the game. ".format(botname)
    else:
        return  "The Game is a tie. No one is a winner"








winningsreal = 0
winningsbot = 0
#The winningsreal and the winningsbot is a counter which monitors how monitors the amount of rounds  a player or a bot has won

rounds = int(input("How many rounds would you like to play?"))
#Used to store the amount of rounds which the user wants to play
for i in range(rounds):


   input(">>Enter to roll the Dice,you have  " + str(i) + " out of  " + str(rounds) + " rounds left to go ")
   realperson = obj.roll()


   bot = obj.roll()
   # Calls the roll method from the Dice class to choose a random dice side.

   if realperson > bot:
        print("You have won round {} ".format(i))



        winningsreal = winningsreal  + 1


   elif realperson == bot:
    print("The game is a draw")

   elif realperson < bot:
        print("The opponent has won  round {}".format(i))




        winningsbot = winningsbot + 1





print("_________________Overall Scoring________________________________________")
print("You have won a total of  {} games .".format(winningsreal))
print("The bot has won a total of {} games .".format((winningsbot)))
print("___________________ Winner is!___________________________________________")
winner = checkfinalwinner(winningsreal,winningsbot)
print(winner)
print("------------------------Thank You for Playing Dice Mania------------------")














