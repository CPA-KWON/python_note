from random import randint

pc_choice=randint(1,100)
playing=True
attempt=0
max_attempt=100

while playing:
    attempt= attempt +1
    input_n=int(input("1~100까지의 숫자를 입력하세요: "))

    if input_n<1 or input_n>100:
        print("1~100까지의 숫자를 입력하세요: ")
    elif input_n==pc_choice:
        print("You Won!")
        playing=False
    elif attempt == max_attempt:
        print("You Lose")
        print("pc_choice: ",pc_choice)
        playing= False
    elif input_n > pc_choice:
        print("Down")
        print(max_attempt-attempt, "번의 기회가 남았습니다다")
    elif input_n < pc_choice:
        print("Up")
        print(max_attempt-attempt, "번의 기회가 남았습니다다")