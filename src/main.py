import tkinter as tk
from tkinter import messagebox
from ip_calculator import get_network_info
from utils import valid_ip, valid_cidr, valid_mask, mask_to_cidr

def launch_calculator():
    start.destroy()
    open_calculator()

def open_calculator():
    global entry_ip, entry_mask_or_cidr, output_text, selected_option

    calc = tk.Tk()
    calc.title("IP Subnet Calculator")

    tk.Label(calc, text="Adresse IP :").pack()
    entry_ip = tk.Entry(calc)
    entry_ip.pack()

    selected_option = tk.StringVar(value="CIDR")
    frame_radio = tk.Frame(calc)
    tk.Radiobutton(frame_radio, text="CIDR (/xx)", variable=selected_option, value="CIDR").pack(side='left')
    tk.Radiobutton(frame_radio, text="Masque", variable=selected_option, value="Masque").pack(side='left')
    frame_radio.pack()

    entry_mask_or_cidr = tk.Entry(calc)
    entry_mask_or_cidr.pack()

    tk.Button(calc, text="Calculer", command=on_calculate).pack(pady=5)

    output_text = tk.Text(calc, height=5, width=50)
    output_text.pack()
    output_text.config(state='disabled')

    calc.mainloop()

def on_calculate():
    ip = entry_ip.get()
    method = selected_option.get()
    value = entry_mask_or_cidr.get()

    if not valid_ip(ip):
        messagebox.showerror("Erreur", "Adresse IP invalide.")
        return

    if method == "CIDR":
        if not valid_cidr(value):
            messagebox.showerror("Erreur", "CIDR invalide (0-32).")
            return
        cidr = value
    else:
        if not valid_mask(value):
            messagebox.showerror("Erreur", "Masque invalide.")
            return
        cidr = mask_to_cidr(value)
        if cidr is None:
            messagebox.showerror("Erreur", "Masque non valide (non contigu).")
            return

    result = get_network_info(ip, cidr)

    # Masquer soit le CIDR soit le masque selon le choix initial
    if method == "CIDR":
        del result["CIDR"]
    else:
        del result["Masque de sous-réseau"]

    output_text.config(state='normal')
    output_text.delete(1.0, tk.END)
    for key, val in result.items():
        output_text.insert(tk.END, f"{key}: {val}\n")
    output_text.config(state='disabled')


# Interface de démarrage
start = tk.Tk()
start.title("IP Subnet Calculator")

tk.Label(start, text="Bienvenue dans le calculateur IP", font=("Arial", 14)).pack(pady=10)
tk.Label(start, text="Par Said MESBAHI", font=("Arial", 12)).pack(pady=5)
tk.Button(start, text="Lancer", command=launch_calculator).pack(pady=10)

start.mainloop()
