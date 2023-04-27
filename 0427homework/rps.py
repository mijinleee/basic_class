import random

options = ['가위', '바위', '보']
computer_choice = random.choice(options)

while True:
    user_input = input("가위, 바위, 보 중에서 골라주세요: ")
    if user_input in options:
        if user_input == '가위':
            if computer_choice == '가위':
                print("비겼다.")
            elif computer_choice == '바위':
                print("졌다.")
            else:
                print("이겼다.")
            break
        elif user_input == '바위':
            if computer_choice == '가위':
                print("이겼다.")
            elif computer_choice == '바위':
                print("비겼다.")
            else:
                print("졌다.")
            break
        else:
            if computer_choice == '가위':
                print("졌다.")
            elif computer_choice == '바위':
                print("이겼다.")
            else:
                print("비겼다.")
            break
    else:
        print("잘못된 입력입니다. 다시 입력해주세요.")
