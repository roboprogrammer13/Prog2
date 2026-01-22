import tkinter as tk
import time

CIL = 10  # cílový čas v sekundách
bezi = False
start_cas = 0
tecky = 0

def start():
    global bezi, start_cas
    bezi = True
    start_cas = time.time()
    info_label.config(text="Zkus odhadnout 10 sekund")
    vysledek_label.config(text="")
    animace()

def animace():
    global tecky
    if bezi:
        tecky = (tecky + 1) % 4
        anim_label.config(text="Čas běží" + "." * tecky)
        root.after(300, animace)

def stop():
    global bezi
    if not bezi:
        return

    bezi = False
    konec = time.time()
    uplynulo = konec - start_cas
    rozdil = uplynulo - CIL

    vysledek_label.config(
        text=f"Tvůj čas: {uplynulo:.2f} s\nOdchylka: {rozdil:+.2f} s"
    )

    # Hodnocení
    if abs(rozdil) < 0.3:
        hodnoceni("😃 Skvělé!", "Perfektní odhad!")
    elif abs(rozdil) < 1:
        hodnoceni("🙂 Dobrá práce!", "Bylo to těsně.")
    else:
        hodnoceni("😐 Zkus to znovu", "Trénink dělá mistra.")

def hodnoceni(smajl, text):
    anim_label.config(text=smajl)
    info_label.config(text=text)

# --- GUI ---
root = tk.Tk()
root.title("Odhadni 10 sekund")
root.geometry("300x250")

info_label = tk.Label(root, text="Stiskni START", font=("Arial", 12))
info_label.pack(pady=10)

anim_label = tk.Label(root, text="", font=("Arial", 16))
anim_label.pack(pady=10)

vysledek_label = tk.Label(root, text="", font=("Arial", 12))
vysledek_label.pack(pady=10)

start_btn = tk.Button(root, text="START", width=15, command=start)
start_btn.pack(pady=5)

stop_btn = tk.Button(root, text="STOP", width=15, command=stop)
stop_btn.pack(pady=5)

root.mainloop()
