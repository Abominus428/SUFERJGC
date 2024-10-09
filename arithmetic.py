import tkinter as tk

class ArithmeticCalculator:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame

        # 显示输入和结果的文本框
        self.display = tk.Entry(self.parent_frame, justify="right", font=("Arial", 20), bd=10)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")  # 使用 sticky 来适应大小

        # 存储表达式和结果的变量
        self.expression = ""
        self.result_shown = False  # 标记是否已经显示了结果
        self.ans = ""  # 用于存储上一次的计算结果

        # 创建按钮
        self.create_buttons()

        # 配置行和列的权重，确保随着窗口大小调整
        for i in range(7):  # 行数增加到 6 以适应新按钮行
            self.parent_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.parent_frame.grid_columnconfigure(j, weight=1)

    def create_buttons(self):
        """创建计算器的按钮"""
        # 定义按钮的标签和位置
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
            ('(', 4, 0), ('0', 4, 1), (')', 4, 2), ('/', 4, 3),
            ('C', 5, 0), ('ANS', 5, 1), ('=', 5, 2, 2),  # 让 "=" 按钮占用两列
            ('DEL', 6, 0), ('.', 6, 1)  # 添加小数点按钮
        ]

        # 使用循环创建按钮并将它们放在网格中
        for (text, row, col, *size) in buttons:
            if text == '=':
                btn = tk.Button(self.parent_frame, text=text, width=10, height=3, command=self.calculate_result)
            elif text == 'C':
                btn = tk.Button(self.parent_frame, text=text, width=10, height=3, command=self.clear)
            elif text == 'DEL':
                btn = tk.Button(self.parent_frame, text=text, width=10, height=3, command=self.delete_last)
            elif text == 'ANS':
                btn = tk.Button(self.parent_frame, text=text, width=10, height=3, command=self.use_ans)
            else:
                btn = tk.Button(self.parent_frame, text=text, width=10, height=3, command=lambda t=text: self.update_expression(t))
            btn.grid(row=row, column=col, columnspan=size[0] if size else 1, padx=5, pady=5, sticky="nsew")  # 使用 sticky 来适应大小

    def update_expression(self, value):
        """更新表达式"""
        if self.result_shown:
            if value.isdigit() or value == '.' or value == 'ANS' or value == '(':
                self.expression = value
            elif value == '-':
                self.expression += value  # 允许输入负数
            else:
                self.expression += value
            self.result_shown = False
        else:
            # 检查小数点的输入逻辑
            if value == '.' and (not self.expression or self.expression[-1] in '+-*/('):
                self.expression += '0.'  # 如果表达式为空或最后一个字符是运算符，自动加上 0
            elif value == '.' and '.' in self.expression.split()[-1]:
                return  # 防止在一个数字中输入多个小数点
            if value == '-' and (self.expression == '' or self.expression[-1] in '+-*/('):
                self.expression += value  # 允许在表达式开头或在运算符后输入负数
            elif value == '(':
                self.expression += value
            elif value == ')':
                if self.expression and self.expression[-1] != '(':
                    self.expression += value  # 允许在表达式中添加右括号
            else:
                self.expression += value

        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

    def calculate_result(self):
        """计算结果"""
        try:
            result = eval(self.expression)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
            self.ans = str(result)  # 记录上一次的结果
            self.expression = str(result)
            self.result_shown = True
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "错误")
            self.expression = ""
            self.result_shown = False

    def delete_last(self):
        """删除最后一个字符"""
        if self.result_shown:
            return
        self.expression = self.expression[:-1]
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

    def clear(self):
        """清空输入"""
        self.expression = ""
        self.display.delete(0, tk.END)
        self.result_shown = False

    def use_ans(self):
        """使用上一次的结果"""
        if self.result_shown:
            self.expression = self.ans
        else:
            self.expression += self.ans

        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)
