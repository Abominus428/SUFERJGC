import tkinter as tk
from arithmetic import ArithmeticCalculator  # 导入四则运算模块

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("多功能计算器")
        self.root.geometry("400x600")  # 设置初始窗口大小

        # 创建一个主Frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)

        # 创建返回主窗口按钮
        self.back_button = tk.Button(self.root, text="返回主窗口", command=self.show_main)
        self.back_button.pack(side="top", anchor="nw", padx=10, pady=10)
        self.back_button.pack_forget()  # 初始时隐藏该按钮

        # 开始显示主界面
        self.show_main()

    def clear_frame(self):
        """清空主Frame中的内容"""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_main(self):
        """显示主窗口内容"""
        self.clear_frame()
        self.back_button.pack_forget()  # 隐藏返回按钮

        # 在主窗口中可以添加其他功能的按钮
        arithmetic_button = tk.Button(self.main_frame, text="四则运算", command=self.show_arithmetic)
        arithmetic_button.pack(pady=50)

    def show_arithmetic(self):
        """显示四则运算界面"""
        self.clear_frame()
        self.back_button.pack(side="top", anchor="nw", padx=10, pady=10)  # 显示返回按钮
        ArithmeticCalculator(self.main_frame)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
