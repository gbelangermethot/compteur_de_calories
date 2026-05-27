import customtkinter as ctk
import sqlite3
from aliment import Aliment
from PIL import Image
from functions import *
from tabs.creation_repas_tab import build_creation_repas_tab
from tabs.repas_passes_class import *


app = ctk.CTk()

app.geometry("1200x800")
app.title("Comteur de calories")

tab_view = ctk.CTkTabview(app)
tab_view.pack(fill="both", expand=True)

creation_repas_tab = tab_view.add("Construire votre repas")
build_creation_repas_tab(creation_repas_tab)

repas_passes_tab = tab_view.add("Repas passe")
repas_passes_page = repas_passes_class(repas_passes_tab)

creation_aliment_tab = tab_view.add("Ajouter un aliment")

def refresh():
    repas_passes_page.refresh_repas_liste()

tab_view.configure(command=refresh)


app.mainloop()