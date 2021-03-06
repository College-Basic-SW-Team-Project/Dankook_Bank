import json  # json모듈을 호출한다.
import os.path  # os.path를 호출한다.
from tkinter import *  # tkinter 모듈을 포함한다.
from tkinter import messagebox  # thkinter 모듈에서 메세지박스를 호출한다.

# App 클래스를 정의합니다.


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None  # 기본 프레임은 없다.
        self.switch_frame(LoginPage)  # 시작하면 로그인 페이지 클래스로 프레임을 전환합니다.

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


# 로그인 페이지 클래스를 정의합니다.
class LoginPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        inputPK = StringVar()
        inputID = StringVar()
        inputPassword = StringVar()

        Label(self, fg="blue", text="보안번호 입력").grid(row=0)
        Label(self, fg="blue", text="ID 입력").grid(row=1)
        Label(self, fg="blue", text="PASSWORD 입력").grid(row=2)

        PK = Entry(self, width=30, textvariable=inputPK)
        ID = Entry(self, width=30, textvariable=inputID)
        password = Entry(self, width=30, textvariable=inputPassword)

        login_button = Button(self, text="로그인", command=lambda: login(
            inputPK, inputID, inputPassword))
        sign_up_button = Button(
            self, text="회원가입", command=lambda: master.switch_frame(SignUpPage))
        exit_button = Button(self, text="종료", command=self.quit)

        PK.grid(row=0, column=1)
        ID.grid(row=1, column=1)
        password.grid(row=2, column=1)
        login_button.grid(row=2, column=2, sticky=W, pady=4)
        sign_up_button.grid(row=3, column=2, sticky=W, pady=4)
        exit_button.grid(row=4, column=2, sticky=W, pady=4)


# 회원가입 페이지 클래스를 정의합니다.
class SignUpPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        inputPK = StringVar()
        inputUsername = StringVar()
        inputID = StringVar()
        inputPassword = StringVar()

        SignInLabel = Label(
            self, fg="blue", text="회원 가입").grid(row=0, column=1)
        Label(self, fg="blue", text="보안 코드").grid(row=1)
        Label(self, fg="blue", text="유저 이름").grid(row=2)
        Label(self, fg="blue", text="아이디").grid(row=3)
        Label(self, fg="blue", text="비밀번호").grid(row=4)

        PK = Entry(self, width=20, textvariable=inputPK)
        username = Entry(self, width=20, textvariable=inputUsername)
        ID = Entry(self, width=20, textvariable=inputID)
        password = Entry(self, width=20, textvariable=inputPassword)

        submit_button = Button(self, text="회원 가입", command=lambda: sign_in(
            inputPK, inputUsername, inputID, inputPassword))
        back_button = Button(
            self, text="이전으로", command=lambda: master.switch_frame(LoginPage))

        PK.grid(row=1, column=1)
        username.grid(row=2, column=1)
        ID.grid(row=3, column=1)
        password.grid(row=4, column=1)
        submit_button.grid(row=10, column=2, sticky=W, pady=4)
        back_button.grid(row=10)


# 회원가입 페이지에서 입력받은 정보를 json 파일에 저장하는 함수
def signWrite(pk, username, ID, password):
    user_file_path = "./json/users.json"
    user_data = {}

    # json 파일이 존재하는지 확인
    if os.path.exists(user_file_path):
        with open(user_file_path, "r") as json_file:
            user_data = json.load(json_file)

        user_data[pk] = {
            "pk": pk,
            "username": username,
            "id": ID,
            "password": password,
            "balance": "0"
        }

        with open(user_file_path, "w") as outfile:
            json.dump(user_data, outfile, indent=4)

    # json파일이 존재하지않을 경우 실행
    else:
        user_data[pk] = {
            "pk": pk,
            "username": username,
            "id": ID,
            "password": password,
            "balance": "0"
        }

        with open(user_file_path, "w") as outfile:
            json.dump(user_data, outfile, indent=4)


# 잔액을 json파일에 입력하는 함수
def writeBalance(pk, balance):
    user_file_path = "./json/users.json"
    with open(user_file_path, "r") as json_file:
        user_data = json.load(json_file)

    user_data[pk]["balance"] = str(balance)
    with open(user_file_path, "w") as outfile:
        json.dump(user_data, outfile, indent=4)


# json 내부 내용 출력 함수
def read(pk):
    user_file_path = "./json/users.json"

    # json 파일이 존재하는지 확인
    if os.path.exists(user_file_path):
        with open(user_file_path, "r") as json_file:
            json_data = json.load(json_file)
            user = json_data.get(pk)
            return user


# 로그인을 위해 json에서 id, ps를 불러오는 함수
def loginRead(pk):
    user_file_path = "./json/users.json"

    # json 파일이 존재하는지 확인
    if os.path.exists(user_file_path):
        with open(user_file_path, "r") as json_file:
            json_data = json.load(json_file)
            user = json_data.get(pk)
            ID = user.get("id")
            Password = user.get("password")
            return ID, Password

    # json파일이 존재하지않을 경우 실행
    else:
        messagebox.askyesno(title="DB 에러", message="DB가 존재하지 않습니다.")


# 회원가입 부분
def sign_in(inputPK, inputUsername, inputID, inputPassword):
    pk = inputPK.get()
    username = inputUsername.get()
    ID = inputID.get()
    password = inputPassword.get()
    data = read(pk)

    # 회원가입 확인(validation)
    if data is not None:
        data_pk = data.get("pk")
        data_user = data.get("username")
        data_id = data.get("id")
        data_password = data.get("password")
        if pk == data_pk:
            messagebox.askyesno(title="Validation Error",
                                message="중복되는 보안 코드가 이미 있습니다.")

        elif username == data_user:
            messagebox.askyesno(title="Validation Error",
                                message="중복되는 이름이 이미 있습니다.")
        elif ID == data_id:
            messagebox.askyesno(title="Validation Error",
                                message="중복되는 아이디가 이미 있습니다.")
        elif password == data_password:
            messagebox.askyesno(title="Validation Error",
                                message="중복되는 비밀번호가 이미 있습니다.")
        else:
            if not pk:
                messagebox.askyesno(
                    title="회원가입 오류", message="보안 코드를 입력하지 않았습니다.")
            elif not username:
                messagebox.askyesno(
                    title="회원가입 오류", message="유저 이름을 입력하지 않았습니다.")
            elif not ID:
                messagebox.askyesno(
                    title="회원가입 오류", message="아이디를 입력하지 않았습니다.")
            elif not password:
                messagebox.askyesno(
                    title="회원가입 오류", message="비밀번호를 입력하지 않았습니다.")
            else:
                db = signWrite(pk, username, ID, password)
                messagebox.askyesno(
                    title="회원가입 성공", message="회원가입 성공\n '이전으로' 버튼을 눌러주십시오.")
    else:
        if not pk:
            messagebox.askyesno(
                title="회원가입 오류", message="보안 코드를 입력하지 않았습니다.")
        elif not username:
            messagebox.askyesno(title="회원가입 오류", message="유저 이름을 입력하지 않았습니다.")
        elif not ID:
            messagebox.askyesno(title="회원가입 오류", message="아이디를 입력하지 않았습니다.")
        elif not password:
            messagebox.askyesno(title="회원가입 오류", message="비밀번호를 입력하지 않았습니다.")
        else:
            db = signWrite(pk, username, ID, password)
            messagebox.askyesno(
                title="회원가입 성공", message="회원가입 성공\n '이전으로' 버튼을 눌러주십시오.")


# 로그인 부분
def login(inputPK, inputID, inputPassword):
    pk = inputPK.get()
    ID = inputID.get()
    password = inputPassword.get()
    if not pk:
        messagebox.askyesno(
            title="로그인 에러", message="보안 코드를 입력하지 않았습니다.")
    elif not ID:
        messagebox.askyesno(title="로그인 에러", message="아이디를 입력하지 않았습니다.")
    elif not password:
        messagebox.askyesno(title="로그인 에러", message="비밀번호를 입력하지 않았습니다.")
    else:
        db = loginRead(pk)
        if db is not None:
            db_id = db[0]
            db_password = db[1]
            if db_id != ID:
                messagebox.askyesno(
                    title="로그인 실패", message="아이디가 틀렸습니다.")
            elif db_password != password:
                messagebox.askyesno(title="로그인 실패", message="비밀번호가 틀렸습니다.")
            else:
                messagebox.askyesno(title="로그인 성공", message="알림창을 닫고 진행하십시오.")
                bank = BankAccount(pk)
                while True:
                    menu = int(
                        input('\n원하시는 기능을 선택하세요 ( 1 : 입금, 2 : 송금, 3 : 종료 ) : '))
                    if type(menu) != int:
                        print("번호를 입력하십시오.")
                    elif menu < 0 or menu > 3:
                        print("잘못된 번호입니다. 다시 입력해주세요.")
                    else:
                        if menu == 1:
                            bank.deposit(int(input('\n입금할 금액을 입력하세요(원) : ')))
                            print('귀하의 잔액은 ', bank.get_balance(), '원 입니다.\n')
                        elif menu == 2:
                            bank.withdraw(int(input('\n송금할 금액을 입력하세요(원) : ')))
                            print('귀하의 잔액은 ', bank.get_balance(), '원 입니다.\n')
                        elif menu == 3:
                            print('\n이용해주셔서 감사합니다.\n\n종료 버튼을 눌러주십시오.')
                            break
        else:
            pass


# 은행 기능 클래스
class BankAccount:

    def __init__(self, pk):
        data = read(pk)
        self.__pk = pk
        self.__balance = data.get("balance")
        self.__balance = int(self.__balance)

    # 입금에 대한 함수 정의
    def deposit(self, amount):
        if amount < 0:
            print("음수는 입력할 수 없습니다.")
        else:
            self.__balance += amount
            print(f"귀하의 통장에 {amount} 원이 입금되었습니다.")
            writeBalance(self.__pk, self.__balance)
            return self.__balance

    # 송금에 대한 함수 정의
    def withdraw(self, amount):
        if amount > self.__balance:
            print("잔액이 부족합니다.")
        else:
            self.__balance -= amount
            print(f"귀하의 통장에서 {amount} 원이 송금되었습니다.")
            writeBalance(self.__pk, self.__balance)
            return self.__balance

    # 잔액을 가져오는 함수 정의
    def get_balance(self):
        return self.__balance


# 프로그램 실행 부분
window = App()
window.title("단국뱅킹")
window.mainloop()
