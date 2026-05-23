import customtkinter as ctk
from functions import *

def build_repas_passes_tab(repas_passes_tab):
    repas_passes_tab.configure(fg_color="#035efc")

    repas_passes_tab.grid_rowconfigure(1, weight=1)

    repas_passes_tab.grid_columnconfigure(0, weight=1)
    repas_passes_tab.grid_columnconfigure(1, weight=1)

    left_panel = ctk.CTkFrame(repas_passes_tab, fg_color="transparent")
    left_panel.grid(row=1, column=0, padx=(60,10), pady=20, sticky="nsew")

    right_panel = ctk.CTkScrollableFrame(repas_passes_tab, fg_color="transparent")
    right_panel.grid(row=1, column=1, padx=10, pady=20, sticky="nsew")
    right_panel.grid_columnconfigure(0, weight=1)

    header = ctk.CTkLabel(
        left_panel,
        text="Filtres de recherche",
        font=("Arial", 20),
        text_color="white"
    )
    header.grid(row=0, column=0, pady=20, padx=60)

    header = ctk.CTkLabel(
        right_panel,
        text="Liste des repas",
        font=("Arial", 20),
        text_color="white"
    )
    header.grid(row=0, column=0, pady=20)

    repas = get_all_repas()

    def select_repas():
        return

    for index, repas in enumerate(repas, start=1):
        create_repas_card(right_panel, repas, index, 0, select_repas)
    