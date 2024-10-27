from scipy.special import comb
import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont

# 定义计算概率的函数
def calculate_probability(a, b, c, d):
    # 验证输入条件
    if not (isinstance(a, int) and a > 0):
        return "出错信息: '需要牌的剩余总张数' 必须是正整数"
    if not (isinstance(a, int) and a <= d):
        return "出错信息: '需要牌的剩余总张数' 必须小于等于剩余牌总数"
    if not (isinstance(b, int) and b > 0):
        return "出错信息: '需要牌的至少数量' 必须是正整数"
    if not (isinstance(b, int) and b <= a):
        return "出错信息: '需要牌的至少数量' 必须小于等于'需要牌的剩余总张数'"
    if not (isinstance(b, int) and b <= c):
        return "出错信息: '需要牌的至少数量' 必须小于等于'弃牌后收到的牌数'"
    if not (isinstance(c, int) and c > 0):
        return "出错信息: '弃牌后收到的牌数' 必须是正整数"
    if not (isinstance(c, int) and c <= d):
        return "出错信息: '弃牌后收到的牌数' 必须小于等于剩余牌总数"
    if not (isinstance(d, int) and d > 0):
        return "出错信息: '剩余牌总数' 必须是正整数"
    
    # 核心概率计算
    p = 0
    for i in range(b, c + 1):
        p += (comb(a, i) * comb(d - a, c - i)) / comb(d, c)
    return f"成功概率: {round(100 * p, 2)}%"  # 保留两位小数

# 定义按钮点击后的计算功能
def on_calculate():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        c = int(entry_c.get())
        d = int(entry_d.get())
        
        # 调用概率计算函数
        result = calculate_probability(a, b, c, d)
        label_result.config(text=result)
        
    except ValueError:
        messagebox.showerror("输入错误", "所有输入必须是整数")

# 动态调整字体大小
current_font_size = 10  # 初始字体大小
def resize_fonts():
    global current_font_size
    # 获取窗口的宽度和高度
    new_width = root.winfo_width()
    new_height = root.winfo_height()
    # 计算新的字体大小
    new_size = int(min(new_width / 30, new_height / 10))
    
    # 只有在新大小与当前大小不同时才更新字体
    if new_size != current_font_size:
        current_font_size = new_size
        font = tkFont.Font(size=new_size)
        label_a.config(font=font)
        label_b.config(font=font)
        label_c.config(font=font)
        label_d.config(font=font)
        entry_a.config(font=font)
        entry_b.config(font=font)
        entry_c.config(font=font)
        entry_d.config(font=font)
        label_result.config(font=font)
        btn_calculate.config(font=font)

# 延迟调整字体以避免频繁触发循环
def on_resize(event):
    root.after(100, resize_fonts)

# 创建窗口
root = tk.Tk()
root.title("小丑牌成功概率计算器")

# 设置窗口的最小尺寸
root.minsize(400, 200)

# 第一行：需要牌的剩余总张数（a）和需要牌的至少数量（b）
label_a = tk.Label(root, text="需要牌的剩余总张数")
label_a.grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_a = tk.Entry(root, width=5)
entry_a.grid(row=0, column=1, sticky="w", padx=5, pady=5)

label_b = tk.Label(root, text="需要牌的至少数量")
label_b.grid(row=0, column=2, sticky="e", padx=5, pady=5)
entry_b = tk.Entry(root, width=5)
entry_b.grid(row=0, column=3, sticky="w", padx=5, pady=5)

# 第二行：弃牌后收到的牌数（c）和剩余牌总数（d）
label_c = tk.Label(root, text="弃牌后收到的牌数")
label_c.grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_c = tk.Entry(root, width=5)
entry_c.grid(row=1, column=1, sticky="w", padx=5, pady=5)

label_d = tk.Label(root, text="剩余牌总数")
label_d.grid(row=1, column=2, sticky="e", padx=5, pady=5)
entry_d = tk.Entry(root, width=5)
entry_d.grid(row=1, column=3, sticky="w", padx=5, pady=5)

# 第三行：显示概率或错误信息
label_result = tk.Label(root, text="", fg="blue")
label_result.grid(row=2, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

# 第四行：计算按钮
btn_calculate = tk.Button(root, text="开始计算", command=on_calculate)
btn_calculate.grid(row=3, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

# 设置列和行的权重，使窗口放大时元素自动扩展
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(4):
    root.grid_rowconfigure(i, weight=1)

# 绑定窗口尺寸变化事件
root.bind("<Configure>", on_resize)

# 启动主循环
root.mainloop()
