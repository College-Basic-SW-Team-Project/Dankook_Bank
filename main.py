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
        sign_up_button = Button(
            self, text="회원가입", command=lambda: master.switch_frame(SignUpPage))
        exit_button = Button(self, text="종료", command=self.quit)

        PK.grid(row=0, column=1)
        ID.grid(row=1, column=1)
        password.grid(row=2, column=1)
        login_button.grid(row=2, column=2, sticky=W, pady=4)
        sign_up_button.grid(row=3, column=2, sticky=W, pady=4)
        exit_button.grid(row=4, column=2, sticky=W, pady=4)


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


def login(inputPK, inputID, inputPassword):
    pk = inputPK.get()
    ID = inputID.get()
    Password = inputPassword.get()
    print(type(pk))
    print(pk)
    if not pk or not ID or not Password:
        messagebox.askyesno(
            title="로그인 에러", message="보안번호, 아이디 혹은 비밀번호를\n 입력하시지않았습니다.")
    else:
        db = loginRead(pk)
        db_id = db[0]
        db_password = db[1]
        if db_id != ID or db_password != Password:
            messagebox.askyesno(
                title="로그인 실패", message="보안번호, 아이디 혹은 비밀번호가\n 틀렸습니다.")
        else:
            messagebox.askyesno(title="로그인 성공", message="창을 닫고 진행하십시오.")


window = App()
window.title("단국뱅킹")
window.mainloop()
