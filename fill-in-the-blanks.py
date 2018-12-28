#easy fill in the blanks 
easy = "We humans beings have many organs but there are ___1___ imp.organs that connect us with the environment.\
The organ that helps us to see are ___2___.The organ that helps us to hear are ears.\
The organ that helps us to taste is ___3___.The organ that helps to smell is nose.\
the organ that hepls us feeling and touching is ___4___.\n"
#medium fill in the blanks 
medium = "___1___ is an electronic devices capable to receive information as input and output.\
___2___ is the input device throught which we can move the on-screen cursor to differen items on the screen.\
___3___ is a volatile memory.Full form of CPU is central ___4___ unit"
#difficult fill in the blanks 
difficult = "National game of india is ___1___ Indian hockey team \
won its first olympic gold medal in ___2___.The team was formed in ___3___.CHAK DE INDIA movie is based on ___4___ sport."
#list of correct answers of easy level
easy_ans = ["5", "eyes", "tongue","skin"]
#list of correct answers of medium level
medium_ans = ["computer", "mouse", "ram","processing"]
#list of correct answers of difficult level
difficult_ans= ["hockey", "1928", "calcutta","hockey"]


#methos start that prompts the user to input the fgame level 
def start():
    while True:
        level=raw_input("HELLO FRIEND..Which level of game u want to play? easy/medium/difficult!!")
        if level=="easy":
            print "\n \n please fill in the blanks (in lower case) \n \n" 
            run(easy,easy_ans)
        elif level=="medium":
            print "\n \nplease fill in the blanks (in lower case)\n \n"
            run(medium,medium_ans)
        elif level=="difficult":
            print "\n \n please fill in the blanks (in lower case)\n \n"
            run(difficult,difficult_ans)
        else:
            print "Incorrect Level"
#this is the main logic of the program that takes the ques and the correct answer and matches the answer given by the user             
def run(para,answers):
    print para
    response=[]
    response=userinput(answers)
    j=0
    while j<len(response):
        if response[j] == answers[j]:
            para= para.replace("___"+str(j+1)+"___",response[j])
            print "congo ur " +str(j+1)+ " ans is correct"
        else:
           print para
           print "ans " +str(j+1)+ " is wrong. You have one chance left. " 
           a=raw_input("what is the ans of " +str(j+1)) 
           if a == answers[j]:
               para= para.replace("___"+str(j+1)+"___",a)
           else:
               print "u lost"
        j=j+1
    print para
    
# this method takes the answer from the user and returns it to the main code to check whether the input is correct or not    
def userinput(answers):
    response=[]
    k=1
    for i in answers:
        no=raw_input("what is answer "+str(k)+ "?")
        response.append(no)
        k=k+1
    return response
# the starter of the code that calls the start method which prompts user to select the game level                   
start()      
