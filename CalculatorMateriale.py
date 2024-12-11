import tkinter as tk
from tkinter import messagebox

# Variabile globale
nr_placi_final = 0
suprafata_m2 = 0
tip_suprafata = ""
tip_material = ""  # Variabilă pentru tipul de material

# Funcția de calcul principal
def calculeaza():
    global nr_placi_final, suprafata_m2, tip_suprafata
    try:
        # Preluarea dimensiunilor
        lungime = float(entry_lungime.get())
        inaltime = entry_inaltime.get()
        latime = entry_latime.get()

        # Determinarea automată a tipului de suprafață în funcție de material
        if tip_material in ["Gresie", "Parchet"]:
            if not latime.strip():
                messagebox.showerror("Eroare", "Completează lățimea pentru podea!")
                return
            suprafata_m2 = lungime * float(latime)
            tip_suprafata = "Podea"
        elif tip_material in ["Faianță", "Lambriu"]:
            if not inaltime.strip():
                messagebox.showerror("Eroare", "Completează înălțimea pentru perete!")
                return
            suprafata_m2 = lungime * float(inaltime)
            tip_suprafata = "Perete"
        else:
            messagebox.showerror("Eroare", "Selectează un material valid!")
            return

        # Preluarea dimensiunilor plăcilor și pierderilor
        lungime_placa_cm = float(entry_lungime_placa.get())
        latime_placa_cm = float(entry_latime_placa.get())
        pierderi = float(entry_pierderi.get()) / 100

        # Calcularea suprafeței plăcii
        suprafata_placa_m2 = (lungime_placa_cm * latime_placa_cm) / 10_000  # Conversie cm² -> m²

        # Calcularea numărului de plăci
        nr_placi = suprafata_m2 / suprafata_placa_m2
        nr_placi_final = nr_placi * (1 + pierderi)

        # Afișarea informațiilor calculate
        messagebox.showinfo(
            "Rezultat parțial",
            f"Material: {tip_material}\n"
            f"Tip suprafață: {tip_suprafata}\n"
            f"Suprafața calculată: {round(suprafata_m2, 2)} m²\n"
            f"Număr de plăci necesare: {round(nr_placi_final, 2)}"
        )

        # Trecerea la următoarea fereastră
        show_second_window()
    except ValueError:
        messagebox.showerror("Eroare", "Introduceți valori valide!")

# Funcția pentru calcularea pachetelor și a costului total
def calculeaza_pachete():
    try:
        nr_placi_pachet = int(entry_placi_pachet.get())
        pret_pachet = float(entry_pret_pachet.get())

        # Calcularea numărului de pachete și a costului total
        nr_pachete = -(-nr_placi_final // nr_placi_pachet)  # Rotunjire în sus
        cost_total = nr_pachete * pret_pachet

        # Afișarea rezultatului final
        messagebox.showinfo(
            "Rezultat final",
            f"Material: {tip_material}\n"
            f"Tip suprafață: {tip_suprafata}\n"
            f"Suprafața calculată: {round(suprafata_m2, 2)} m²\n"
            f"Număr de plăci necesare: {round(nr_placi_final, 2)}\n"
            f"Număr de pachete necesare: {int(nr_pachete)}\n"
            f"Cost total: {round(cost_total, 2)} RON"
        )
    except ValueError:
        messagebox.showerror("Eroare", "Introduceți valori valide!")

# Funcția pentru selectarea materialului
def selecteaza_material(material):
    global tip_material
    tip_material = material
    root.deiconify()
    material_window.withdraw()

# Funcția pentru afișarea celei de-a doua ferestre
def show_second_window():
    second_window.deiconify()
    root.withdraw()

# Crearea ferestrei de selecție a materialului
material_window = tk.Tk()
material_window.title("Selectare Material")

material_window.geometry("400x250")

label_material = tk.Label(material_window, text="Selectează tipul de material", font=("Arial", 14))
label_material.pack(pady=20)

btn_gresie = tk.Button(material_window, text="Gresie", font=("Arial", 12), command=lambda: selecteaza_material("Gresie"))
btn_gresie.pack(pady=5)

btn_faianta = tk.Button(material_window, text="Faianță", font=("Arial", 12), command=lambda: selecteaza_material("Faianță"))
btn_faianta.pack(pady=5)

btn_parchet = tk.Button(material_window, text="Parchet", font=("Arial", 12), command=lambda: selecteaza_material("Parchet"))
btn_parchet.pack(pady=5)

btn_lambriu = tk.Button(material_window, text="Lambriu", font=("Arial", 12), command=lambda: selecteaza_material("Lambriu"))
btn_lambriu.pack(pady=5)

# Crearea ferestrei principale
root = tk.Toplevel()
root.title("Calculator Plăci")
root.geometry("600x400")
root.configure(bg="lightblue")
root.withdraw()


# Secțiunea pentru date generale
tk.Label(root, text="Dimensiuni Suprafețe", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(root, text="Lungime (m):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_lungime = tk.Entry(root)
entry_lungime.grid(row=1, column=1, pady=5)

tk.Label(root, text="Lățime (m) [doar pentru podea]:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_latime = tk.Entry(root)
entry_latime.grid(row=2, column=1, pady=5)

tk.Label(root, text="Înălțime (m) [doar pentru perete]:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_inaltime = tk.Entry(root)
entry_inaltime.grid(row=3, column=1, pady=5)

tk.Label(root, text="Lungime placă (cm):").grid(row=4, column=0, padx=10, pady=5, sticky="e")
entry_lungime_placa = tk.Entry(root)
entry_lungime_placa.grid(row=4, column=1, pady=5)

tk.Label(root, text="Lățime placă (cm):").grid(row=5, column=0, padx=10, pady=5, sticky="e")
entry_latime_placa = tk.Entry(root)
entry_latime_placa.grid(row=5, column=1, pady=5)

tk.Label(root, text="Pierderi (%):").grid(row=6, column=0, padx=10, pady=5, sticky="e")
entry_pierderi = tk.Entry(root)
entry_pierderi.grid(row=6, column=1, pady=5)

tk.Button(root, text="Calculează", command=calculeaza).grid(row=7, column=0, columnspan=2, pady=20)

# Crearea celei de-a doua ferestre
second_window = tk.Toplevel(root)
second_window.title("Calcul Pachete")
second_window.geometry("600x300")
second_window.withdraw()

tk.Label(second_window, text="Număr plăci/pachet:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_placi_pachet = tk.Entry(second_window)
entry_placi_pachet.grid(row=0, column=1, pady=5)

tk.Label(second_window, text="Preț pachet (RON):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_pret_pachet = tk.Entry(second_window)
entry_pret_pachet.grid(row=1, column=1, pady=5)

tk.Button(second_window, text="Calculează", command=calculeaza_pachete).grid(row=2, column=0, columnspan=2, pady=20)

# Rularea aplicației
root.mainloop()
