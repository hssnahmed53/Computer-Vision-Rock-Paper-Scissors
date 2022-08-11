import random
import cv2
from keras.models import load_model
import numpy as np
import time
model = load_model ('keras_model.h5')

choice = ["rock","paper","scissors"]
scores = {"computer_score": 0 , "user_score": 0}

def get_preditction(prediction):
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    flag = False

    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        # Press q to close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            flag = True
            start = time.time()

        if flag == True:
            end = 5 - (time.time() - start)
            current_score = "Your score: " + str(user_score), "Computers score: " + str(computer_score)
            cv2.putText(frame, str(int(end)), (350,238), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0), 3, cv2.LINE_4)
            cv2.putText(frame, str(current_score), (31,445), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3, cv2.LINE_4)
            cv2.imshow('frame', frame)

def get_computer_choice():
    print("The Computer is thinking...")
    time.sleep(3)
    randnum = randrange(0,2)
    return choice[randnum]

def get_user_choice(prediction):
    choice_values = {"name": "", "number": 0, "index": 3}
    for i in range(0,4):
        if float(prediction[0][i]) > choice_values["number"]:
            choice_values["number"] = float(prediction[0][i])
            choice_values["index"] = i

    if choice_values["index"] == 0:
        choice_values["name"] == "rock"
    elif choice_values["index"] == 1:
        choice_values["name"] == "paper"
    elif choice_values["index"] == 2:
        choice_values["name"] == "scissors"
    elif choice_values["index"] == 3:
        choice_values["name"] == "nothing"
    return choice_values["name"]

def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        return "draw"
    else:
        if computer_choice == "rock":
            if user_choice == "paper":
                print(f"You Won this round, the computer chose: ",computer_choice)
                user_score += 1
            else:
                print(f"Looks like ya lost this round, the computer chose: ",computer_choice)
                computer_score += 1    
        elif computer_choice == "paper":
            if user_choice == "scissors":
                print(f"Nice! you Won the round, the computer chose: ",computer_choice)
                user_score += 1
            else:
                print(f"Hmmm...you didn't win this round, the computer chose: ",computer_choice)
                computer_score += 1
        elif computer_choice == "scissors":
            if user_choice == "rock":
                print(f"Good job! you Won this round, the computer chose: ",computer_choice)
                user_score += 1
            else:
                print(f"Sorry you didn't win this round, the computer chose: ",computer_choice)
                computer_score += 1
        elif user_choice == "exit":
            return "exit"

def play(prediction):
    while True:
        computer_choice = get_computer_choice()
        user_choice = get_user_choice(prediction)
        if computer_score == 3:
            print("Looks like the Computer won the game!")
            break
        elif user_score == 3:
            print("Nice! you won the game")
            break

    if user_choice == "nothing":
        return {"computer_choice": "",
        "user_choice": "",
        "winner": ""
        }
    else:
        winner = get_winner(computer_choice, user_choice)
        return {"computer_choice": computer_choice,
            "user_choice": user_choice,
            "winner": winner
            }