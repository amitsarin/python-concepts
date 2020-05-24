print("-----------create a quiz game----------")
import requests
import json
import pprint
import random
import html
url= "https://opentdb.com/api.php?amount=1"
endGame=""
correct_score=0
incorrect_score=0
while endGame!= "quit":
    r=requests.get(url)
    if(r.status_code !=200):
        endGame=input("sorry, problem retrieving the question, Press enter to try again or type 'quit': ")
    else:
        valid_answer=False
        answer_number=1
        data=json.loads(r.text)
        question=data['results'][0]['question']
        answers=data['results'][0]['incorrect_answers']
        correct_answer=data['results'][0]['correct_answer']
        answers.append(correct_answer)
        random.shuffle(answers)

        print(html.unescape(question) + "\n")

        for answer in answers:
            print(str(answer_number) + "-" + html.unescape(answer))
            answer_number+=1
            
        while valid_answer==False:
            user_answer= input("\nType the number of the correct answer: ")
            try:
                user_answer=int(user_answer)
                if (user_answer>len(answers) or user_answer<=0):
                    print("Invalid answer, select correct choice: ")
                else:
                    valid_answer = True
            except:
                print("Invalid answer, use only numbers")
            
        user_answer=answers[int(user_answer)-1]
        if user_answer==correct_answer:
            print("\nCongratulations!! you answered correctly! The correct answer is :" +html.unescape(correct_answer))
            correct_score+=1
        else:
            print("sorry,"+ html.unescape(user_answer) + " is incorrect. The correct answer is :" +html.unescape(correct_answer))
            incorrect_score+=1
        print("\n#####################################")
        print("Your score is:")
        print("correct answers: " + str(correct_score))
        print("incorrect answers: " + str(incorrect_score))
        print("\n#####################################")    
        endGame=input("\nPress enter to play again or type 'quit' to quit the game: ").lower()
print("\n Thanks for playing")

        
                
