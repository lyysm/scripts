'''
Author: liuyin
Date: 2022-08-22 01:00:02
LastEditTime: 2022-08-22 02:48:29
FilePath: /scripts/wordle-helper/gui.py
Description:  gui版本
'''
from ctypes.wintypes import WORD
import tkinter
import customtkinter as ctk
APP_NAME = "Wordle Helper"
APP_SIZE = "400x240"
WORD_LENGTH_LIST=['1','2','3','4','5','6','7','8','9','10']


def start_new_game():
    print(1)
# 首页
def show_home(a):
    # Frame
    # https://github.com/TomSchimansky/CustomTkinter/wiki/CTkFrame
    f_home = ctk.CTkFrame(master=a)
    f_home.pack(pady=20, padx=40, fill="both", expand=True)

    # Button
    # https://github.com/TomSchimansky/CustomTkinter/wiki/CTkButton
    b_new_game = ctk.CTkButton(master=f_home, command=new_game_app, text="开始新游戏")
    b_new_game.pack(pady=12, padx=10) 
    b_dict_manager = ctk.CTkButton(master=f_home, command=start_new_game, text="词库管理")
    b_dict_manager.pack(pady=12, padx=10)
    b_help = ctk.CTkButton(master=f_home, command=start_new_game, text="使用帮助")
    b_help.pack(pady=12, padx=10)

# 开始新游戏
def new_game_app():
    ctk.set_appearance_mode("System")
    # Themes: blue (default), dark-blue, green
    ctk.set_default_color_theme("blue")
    app = ctk.CTk()  # create CTk window like you do with the Tk window
    app.geometry("1000x600")
    app.title("Wordle Helper -- 新游戏")
    no_letters = []
    ################################################################
    # 参数
    f_params = ctk.CTkFrame(master=app)
    f_params.pack(pady=20, padx=60, fill="both", expand=True)

                            
    # f_params.grid(row=0, column=0, sticky="nswe")
    # 设置单词长度
    # Label 
    # https://github.com/TomSchimansky/CustomTkinter/wiki/CTkLabel
    l_word_length = ctk.CTkLabel(text="单词长度",master=f_params, justify=tkinter.LEFT)
    l_word_length.pack(pady=12, padx=10)
    # OptionMenu
    # https://github.com/TomSchimansky/CustomTkinter/wiki/CTkOptionMenu
    om_word_length = ctk.CTkOptionMenu(f_params, values=WORD_LENGTH_LIST)
    om_word_length.pack(pady=12, padx=10)
    # 不包含的字母(灰色)
    def add_no_letters():
        for l in e_no_letters.get():
            if l not in no_letters:
                no_letters.append(l)
        print(no_letters)
        l_no_letters_value.set_text(no_letters)
    l_no_letters = ctk.CTkLabel(text="不包含的字母(灰色)",master=f_params, justify=tkinter.LEFT)
    l_no_letters.pack(pady=12, padx=10)
    e_no_letters = ctk.CTkEntry(master=f_params, placeholder_text="abcd")
    e_no_letters.pack(pady=12, padx=10)

    b_add_no_letters = ctk.CTkButton(master=f_params,command=add_no_letters, text="添加")
    b_add_no_letters.pack(pady=12, padx=10)
    ################################################################
    # 实时显示当前配置
    f_status = ctk.CTkFrame(master=app)
    f_status.pack(pady=20, padx=60, fill="both", expand=True)
    l_no_letters = ctk.CTkLabel(text="灰色:",master=f_status, justify=tkinter.LEFT)
    l_no_letters.pack(pady=12, padx=10, fill="both", expand=True)
    l_no_letters_value = ctk.CTkLabel(text=no_letters,master=f_status, justify=tkinter.RIGHT)
    l_no_letters_value.pack(pady=12, padx=10, fill="both", expand=True)
    app.mainloop()



    # label_1 = ctk.CTkLabel(text="hhh" ,master=frame_main, justify=tkinter.LEFT)
    # label_1.pack(pady=12, padx=10)
   







def startApp():
    # Modes: system (default), light, dark
    ctk.set_appearance_mode("System")
    # Themes: blue (default), dark-blue, green
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()  # create CTk window like you do with the Tk window
    app.geometry(APP_SIZE)
    app.title(APP_NAME)

    # 主页面
    show_home(app)

    # frame_main = ctk.CTkFrame(master=app)
    # frame_main.pack(pady=20, padx=60, fill="both", expand=True)

    # # 设置单词长度
    # # Label 
    # # https://github.com/TomSchimansky/CustomTkinter/wiki/CTkLabel
    # l_word_length = ctk.CTkLabel(text="单词长度",master=frame_main, justify=tkinter.LEFT)
    # l_word_length.pack(pady=12, padx=10)
    # # OptionMenu
    # # https://github.com/TomSchimansky/CustomTkinter/wiki/CTkOptionMenu
    # om_word_length = ctk.CTkOptionMenu(frame_main, values=WORD_LENGTH_LIST)
    # om_word_length.pack(pady=12, padx=10)
    # # label_1 = ctk.CTkLabel(text="hhh" ,master=frame_main, justify=tkinter.LEFT)
    # # label_1.pack(pady=12, padx=10)

    # def button_function():
    #     print("button pressed")
    # # Use CTkButton instead of tkinter Button
    # button = ctk.CTkButton(
    #     master=app, text="CTkButton", command=button_function)
    # button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    app.mainloop()


if __name__ == "__main__":
    startApp()
