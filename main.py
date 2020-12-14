import json
from tkinter import *
from tkinter import messagebox


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.switch_frame(LoginPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


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
        profile_button = Button(
            self, text="프로필", command=lambda: master.switch_frame(BalancePage))
        sign_up_button = Button(
            self, text="회원가입", command=lambda: master.switch_frame(SignUpPage))

        PK.grid(row=0, column=1)
        ID.grid(row=1, column=1)
        password.grid(row=2, column=1)
        login_button.grid(row=2, column=2, sticky=W, pady=4)
        profile_button.grid(row=3, column=2, sticky=W, pady=4)
        sign_up_button.grid(row=4, column=2, sticky=W, pady=4)


class BalancePage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        InputWithdraw = StringVar()
        InputDeposit = StringVar()

        Label(self, fg="black", text="이름").grid(row=0)
        Label(self, fg="blue", text="").grid(row=0, column=1)
        Label(self, fg="black", text="잔액").grid(row=1)
        Label(self, fg="blue", text="").grid(row=1, column=1)

        withdraw_button = Button(
            self, text="송금", command=lambda: withdraw(InputWithdraw))
        withdraw_entry = Entry(self, width=10, textvariable=InputWithdraw)

        deposit_button = Button(
            self, text="입금", command=lambda: deposit(InputDeposit))
        deposit_entry = Entry(self, width=10, textvariable=InputDeposit)

        end_button = Button(self, text="종료", command=lambda: )


class SignUpPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)


def write(pk, username, id, password):
    user_file_path = "./json/users.json"

    user_data = {}
    user_data[pk] = []
    user_data[pk].append({

    })


def read(pk):
    user_file_path = "./json/users.json"
    with open(user_file_path, "r") as json_file:
        json_data = json.load(json_file)
        user = json_data.get(pk)
        return user


def loginRead(pk):
    user_file_path = "./json/users.json"
    with open(user_file_path, "r") as json_file:
        json_data = json.load(json_file)
        user = json_data.get(pk)
        ID = user.get("id")
        Password = user.get("password")
        return ID, Password


def sign_in(pk, username, id, password):
    pass


def login(inputPK,
          inputID,
          inputPassword):
    pk = inputPK.get()
    ID = inputID.get()
    Password = inputPassword.get()
    db = loginRead(pk)
    db_id = db[0]
    db_password = db[1]
    if db_id != ID or db_password != Password:
        messagebox.askyesno(title="로그인 실패", message="아이디 혹은 비밀번호가\n 틀렸습니다.")
    else:
        messagebox.askyesno(title="로그인 성공", message="프로필 버튼을 누르십시오.")


def withdraw(balance, amount):
    balance -= amount
    messagebox.askyesno(message=f"귀하의 통장에서 {amount}원이 송금되었습니다.")


def deposit(balance, amount):
    balance += amount
    messagebox.askyesno(title="송금 성공!", message=f"귀하의 통장에 {amount}원이 입금되었습니다.")


window = App()
window.title("단국뱅킹")
window.mainloop()
