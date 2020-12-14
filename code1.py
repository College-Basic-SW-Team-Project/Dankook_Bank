from tkinter import *
# tkinter 모듈을 포함시킨다.


def IdPassword():
    print("아이디 : %s\n패스워드 : %s\n\n로그인 되었습니다.\n다음을 눌러주세요." %
          (e1.get(), e2.get()))
    # get으로 Entry 내용을 가져온다.


window = Tk()
# tkinter 모듈 안에 있는 Tk 클래스가 윈도우를 나타낸다.
window.title("단국뱅킹")

Label(window, fg="blue", text="ID 입력").grid(row=0)

Label(window, fg="blue", text="PASSWORD 입력").grid(row=1)

e1 = Entry(window, width=30)

e2 = Entry(window, width=30)

e1.grid(row=0, column=1)

e2.grid(row=1, column=1)

button = Button(window, text='로그인', command=IdPassword).grid(
    row=3, column=2, sticky=W, pady=4)
button = Button(window, text='다음', command=window.quit).grid(
    row=4, column=2, sticky=W, pady=4)

window.mainloop()


class BankAccount:

    def __init__(self):
        self.__balance = 0

    def withdraw(self, amount):
        self.__balance -= amount
        print("귀하의 통장에서 %d 원이 송금되었습니다." % amount)
        return self.__balance
    # 송금에 대한 함수 정의한다.

    def deposit(self, amount):
        self.__balance += amount
        print("귀하의 통장에 %d 원이 입금되었습니다." % amount)
        return self.__balance
    # 입금에 대한 함수 정의한다.

    def get_balance(self):
        return self.__balance


a = BankAccount()
# 변수 a에 클래스 BankAccount를 할당한다.

while True:
    menu = int(input('\n원하시는 기능을 선택하세요 ( 1 : 입금, 2 : 송금, 3 : 종료 ) : '))
    if type(menu) != int:
        print("번호를 입력하십시오.")
    elif menu < 0 or menu > 3:
        print("잘못된 번호입니다. 다시 입력해주세요.")
    else:
        if menu == 1:
            a.deposit(int(input('\n입금할 금액을 입력하세요(원) : ')))
            print('귀하의 잔액은 ', a.get_balance(), '원 입니다.\n')
        elif menu == 2:
            a.withdraw(int(input('\n송금할 금액을 입력하세요(원) : ')))
            print('귀하의 잔액은 ', a.get_balance(), '원 입니다.\n')
        elif menu == 3:
            print('\n최종 싸인을 완료해주세요.\n')
            break
