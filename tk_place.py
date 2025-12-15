"""
Tkinter Place 
座標比例：側欄 10%、上層 20%、中層 70%、下層 10%
"""
import tkinter as tk

def main():
    form = tk.Tk()
    form.title("Tkinter Place")
    form.geometry("400x300")
    # 基本題：resizable(False, False)
    # 加分題：resizable(True, True)
    form.resizable(True, True)

    # 左側欄 (寬度 10%)
    left_sidebar = tk.Frame(form, bg="lightgreen")
    left_sidebar.place(relx=0, rely=0, relwidth=0.1, relheight=1.0)

    # 右側欄 (寬度 10%)
    right_sidebar = tk.Frame(form, bg="lightblue")
    right_sidebar.place(relx=0.9, rely=0, relwidth=0.1, relheight=1.0)

    # 上層 (高度 20%)
    top_frame = tk.Frame(form, bg="red")
    top_frame.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.2)

    # 紅色區域內的 3 個 Label (三等分位置)
    label_left = tk.Label(top_frame, text="left", bg="white", fg="black")
    label_left.place(relx=1/6, rely=0, anchor="n")

    label_center = tk.Label(top_frame, text="center", bg="white", fg="black")
    label_center.place(relx=0.5, rely=0, anchor="n")

    label_right = tk.Label(top_frame, text="Right", bg="white", fg="black")
    label_right.place(relx=5/6, rely=0, anchor="n")

    # 中層 (高度 70%)
    middle_frame = tk.Frame(form, bg="yellow")
    middle_frame.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.7)

    # 下層 (高度 10%)
    bottom_frame = tk.Frame(form, bg="blue")
    bottom_frame.place(relx=0.1, rely=0.9, relwidth=0.8, relheight=0.1)

    form.mainloop()


if __name__ == "__main__":
    main()
