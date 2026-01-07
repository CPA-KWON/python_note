balance=300000000
input_n=1
def F_check_balance():
    print("잔액: ",balance)
def F_Withdrawal():
    global balance
    withdrawal=int(input("출금하실 금액을 입력하세요: "))
    if balance >= withdrawal:
        balance = balance - withdrawal
        print("출금이 완료돼었습니다")
        print("잔액: ",balance)
    else:
        print("잔액이 부족합니다")
def F_Deposit():
    global balance
    deposit=int(input("입금하실 금액을 입력하세요: "))
    balance= balance + deposit
    print("잔액: ",balance)
while input_n==1 or input_n==2 or input_n==3:
    input_n=int(input("이용하실 서비스를 선택해주세요 (1.잔액조회 2.출금 3.예금 4.취소:) "))
    if input_n==1:
        F_check_balance()
    elif input_n==2:
        F_Withdrawal()
    elif input_n==3:
        F_Deposit()
    else:
        print("이용해주셔서 감사합니다")
        input_n = 4