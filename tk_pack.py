"""
Tkinter Pack
"""
import tkinter as tk

def main():
    form = tk.Tk()
    form.title("Tkinter Pack")
    form.geometry("400x300")
    # 基本題：resizable(False, False)
    # 加分題：resizable(True, True)
    form.resizable(True, True)

    # 左側欄 (固定寬度)
    left_sidebar = tk.Frame(form, bg="lightgreen", width=40)
    left_sidebar.pack(side="left", fill="y")
    left_sidebar.pack_propagate(False)

    # 右側欄 (固定寬度)
    right_sidebar = tk.Frame(form, bg="lightblue", width=40)
    right_sidebar.pack(side="right", fill="y")
    right_sidebar.pack_propagate(False)

    # 上層 (固定高度)
    top_frame = tk.Frame(form, bg="red", height=60)
    top_frame.pack(side="top", fill="x")
    top_frame.pack_propagate(False)

    # 紅色區域內的 3 個 Label (平均分佈，靠上)
    label_left = tk.Label(top_frame, text="left", bg="white", fg="black")
    label_left.pack(side="left", anchor="n", expand=True)

    label_center = tk.Label(top_frame, text="center", bg="white", fg="black")
    label_center.pack(side="left", anchor="n", expand=True)

    label_right = tk.Label(top_frame, text="Right", bg="white", fg="black")
    label_right.pack(side="left", anchor="n", expand=True)

    # 下層 (固定高度)
    bottom_frame = tk.Frame(form, bg="blue", height=30)
    bottom_frame.pack(side="bottom", fill="x")
    bottom_frame.pack_propagate(False)

    # 中層 (填滿剩餘空間)
    middle_frame = tk.Frame(form, bg="yellow")
    middle_frame.pack(side="top", fill="both", expand=True)

    form.mainloop()


if __name__ == "__main__":
    main()
