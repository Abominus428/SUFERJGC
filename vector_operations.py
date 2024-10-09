import numpy as np
import tkinter as tk

class VectorOperationsCalculator:
    def __init__(self, parent):
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        # 选择运算类型
        self.operation_var = tk.StringVar(value="dot")
        tk.Radiobutton(self.parent, text="点积", variable=self.operation_var, value="dot").pack(anchor="w")
        tk.Radiobutton(self.parent, text="叉积", variable=self.operation_var, value="cross").pack(anchor="w")
        tk.Radiobutton(self.parent, text="范数", variable=self.operation_var, value="norm").pack(anchor="w")

        # 输入框
        self.label1 = tk.Label(self.parent, text="向量A (逗号分隔):")
        self.label1.pack()
        self.vector_a_entry = tk.Entry(self.parent)
        self.vector_a_entry.pack()

        self.label2 = tk.Label(self.parent, text="向量B (逗号分隔):")
        self.label2.pack()
        self.vector_b_entry = tk.Entry(self.parent)
        self.vector_b_entry.pack()

        # 计算按钮
        self.calc_button = tk.Button(self.parent, text="计算", command=self.calculate)
        self.calc_button.pack(pady=10)

        # 结果标签
        self.result_label = tk.Label(self.parent, text="")
        self.result_label.pack()

    def calculate(self):
        operation = self.operation_var.get()
        try:
            vector_a = np.array([float(x) for x in self.vector_a_entry.get().split(',')])
            result = ""
            if operation == "dot":
                vector_b = np.array([float(x) for x in self.vector_b_entry.get().split(',')])
                result = np.dot(vector_a, vector_b)
                self.result_label.config(text=f"点积: {result}")
            elif operation == "cross":
                vector_b = np.array([float(x) for x in self.vector_b_entry.get().split(',')])
                result = np.cross(vector_a, vector_b)
                self.result_label.config(text=f"叉积: {result}")
            elif operation == "norm":
                result = np.linalg.norm(vector_a)
                self.result_label.config(text=f"范数: {result}")
        except ValueError:
            self.result_label.config(text="输入无效，请重新输入向量！")
