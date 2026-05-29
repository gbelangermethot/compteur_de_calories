import customtkinter as ctk
import sqlite3
from aliment import Aliment
from PIL import Image
from functions import *
from tabs.creation_repas_class import *
from tabs.repas_passes_class import *
from tabs.creation_aliment_tab import *


app = ctk.CTk()

app.geometry("1200x800")
app.title("Comteur de calories")

tab_view = ctk.CTkTabview(app)
tab_view.pack(fill="both", expand=True)

creation_repas_tab = tab_view.add("Construire votre repas")
creation_repas_page = creation_repas_class(creation_repas_tab)

repas_passes_tab = tab_view.add("Repas passe")
repas_passes_page = repas_passes_class(repas_passes_tab)

creation_aliment_tab = tab_view.add("Ajouter un aliment")
build_creation_aliment_tab(creation_aliment_tab)

def refresh():
    repas_passes_page.refresh_repas_liste()
    creation_repas_page.refresh_aliment_list()

tab_view.configure(command=refresh)


app.mainloop()