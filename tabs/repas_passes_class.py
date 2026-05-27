import customtkinter as ctk
from functions import *

class repas_passes_class:
    def __init__(self, parent):
        parent.configure(fg_color="#035efc")

        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)
        

        self.frame = ctk.CTkFrame(parent, fg_color="transparent")

        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)

        self.frame.grid(row=0, column=0, sticky="nsew")
        self.left_panel = ctk.CTkFrame(self.frame, fg_color="transparent")
        self.left_panel.grid(row=0, column=0, padx=(60,10), pady=20, sticky="nsew")

        self.left_header = ctk.CTkLabel(
            self.left_panel,
            text="recherchez par la date",
            font=("Arial", 20),
            text_color="white"
        )
        self.left_header.grid(row=0, column=0, pady=20, padx=60)

        self.header_selected_repas = ctk.CTkLabel(
            self.left_panel,
            text="Repas Selectione",
            font=("Arial", 20),
            text_color="white"
        )
        self.header_selected_repas.grid(row=2, column=0, pady=20, padx=60)

        self.right_panel = ctk.CTkFrame(self.frame, fg_color="transparent")
        self.right_panel.grid(row=0, column=1, padx=10, pady=20, sticky="nsew")
        self.right_panel.grid_columnconfigure(0, weight=1)
        self.right_panel.grid_rowconfigure(1, weight=1)
        
        self.right_header_panel = ctk.CTkFrame(self.right_panel, fg_color="transparent")
        self.right_header_panel.grid(row=0, column=0, pady=20)

        self.right_header = ctk.CTkLabel(
            self.right_header_panel,
            text="Liste des repas",
            font=("Arial", 20),
            text_color="white"
        )
        self.right_header.grid(row=0, column=0, pady=20)

        self.repas_list_frame = ctk.CTkScrollableFrame(self.right_panel, fg_color="transparent")
        self.repas_list_frame.grid(row=1, column=0, pady=20, sticky="nsew")

        self.create_liste_repas()

    def refresh_repas_liste(self):
        for widget in self.repas_list_frame.winfo_children():
            widget.destroy()

        self.create_liste_repas()

    def create_liste_repas(self):

        def select_repas():
            return

        repas = get_all_repas()
        for index, repa in enumerate(repas):
            create_repas_card(self.repas_list_frame, repa, index, 0, select_repas)


        

    