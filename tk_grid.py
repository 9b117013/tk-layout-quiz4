"""
Tkinter Grid 
"""
import tkinter as tk

def main():
    form = tk.Tk()
    form.title("Tkinter Grid")
    form.geometry("400x300")
    # 基本題：resizable(False, False)
    # 加分題：resizable(True, True)
    form.resizable(True, True)

    # 設定 Grid 結構 (3欄 x 3列)
    form.columnconfigure(0, minsize=40)  # 左側欄固定寬度
    form.columnconfigure(1, weight=1)   # 中間欄延展
    form.columnconfigure(2, minsize=40)  # 右側欄固定寬度

    form.rowconfigure(0, minsize=60)  # 上層固定高度
    form.rowconfigure(1, weight=1)    # 中層延展
    form.rowconfigure(2, minsize=30)  # 下層固定高度

    # 左側欄
    left_sidebar = tk.Frame(form, bg="lightgreen", width=40)
    left_sidebar.grid(row=0, column=0, rowspan=3, sticky="nsew")
    left_sidebar.grid_propagate(False)

    # 右側欄
    right_sidebar = tk.Frame(form, bg="lightblue", width=40)
    right_sidebar.grid(row=0, column=2, rowspan=3, sticky="nsew")
    right_sidebar.grid_propagate(False)

    # 上層
    top_frame = tk.Frame(form, bg="red")
    top_frame.grid(row=0, column=1, sticky="nsew")
    top_frame.grid_propagate(False)

    # 紅色區域內的 3 個 Label (3欄平均分配)
    top_frame.columnconfigure(0, weight=1)
    top_frame.columnconfigure(1, weight=1)
    top_frame.columnconfigure(2, weight=1)

    label_left = tk.Label(top_frame, text="left", bg="white", fg="black")
    label_left.grid(row=0, column=0, sticky="n")

    label_center = tk.Label(top_frame, text="center", bg="white", fg="black")
    label_center.grid(row=0, column=1, sticky="n")

    label_right = tk.Label(top_frame, text="Right", bg="white", fg="black")
    label_right.grid(row=0, column=2, sticky="n")

    # 中層
    middle_frame = tk.Frame(form, bg="yellow")
    middle_frame.grid(row=1, column=1, sticky="nsew")

    # 下層
    bottom_frame = tk.Frame(form, bg="blue", height=30)
    bottom_frame.grid(row=2, column=1, sticky="nsew")
    bottom_frame.grid_propagate(False)

    form.mainloop()


if __name__ == "__main__":
    main()
