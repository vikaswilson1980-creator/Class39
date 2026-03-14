import tkinter as tk
def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        result_label.config(text="Product: " + str(product))
    except ValueError:
        result_label.config(text="Please enter valid numbers")
root = tk.Tk()
root.title("Product Calculator")
root.geometry("300x200")
label1 = tk.Label(root, text="Enter First Number:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()
label2 = tk.Label(root, text="Enter Second Number:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()
calculate_button = tk.Button(root, text="Calculate Product", command=calculate_product)
calculate_button.pack(pady=10)
result_label = tk.Label(root, text="")
result_label.pack()
root.mainloop()