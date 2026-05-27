import customtkinter as ctk
from functions import *
from tkcalendar import DateEntry

class repas_passes_class:
    
    def __init__(self, parent):
        parent.configure(fg_color="#035efc")

        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        self.liste_repas = get_all_repas()
        

        self.frame = ctk.CTkFrame(parent, fg_color="transparent")

        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=2)

        self.frame.grid(row=0, column=0, sticky="nsew")
        self.left_panel = ctk.CTkFrame(self.frame, fg_color="transparent")
        self.left_panel.grid(row=0, column=0, padx=(20,10), pady=20, sticky="nsew")

        self.left_panel.grid_rowconfigure(2, weight=1)
        self.left_panel.grid_columnconfigure(0, weight=1)

        self.left_header = ctk.CTkLabel(
            self.left_panel,
            text="recherchez par la date",
            font=("Arial", 20),
            text_color="white"
        )
        self.left_header.grid(row=0, column=0, pady=20, padx=60)

        self.date_picker = DateEntry(
            self.left_panel,
            width=16,
            background='darkblue',
            foreground='white',
            borderwidth=2,
            date_pattern='yyyy-mm-dd'
        )
        self.date_picker.grid(row=1, column=0, pady=10)
        self.date_picker.bind("<<DateEntrySelected>>", self.filter_repas_by_date)

        self.selected_repas_frame = ctk.CTkScrollableFrame(self.left_panel, fg_color="transparent")
        self.selected_repas_frame.grid(row=2, column=0, pady=20, padx=60, sticky="nsew")

        self.selected_repas = ctk.CTkLabel(
            self.selected_repas_frame,
            text="Aucun repas selectionne",
            font=("Arial", 20),
            text_color="white"
        )
        self.selected_repas.grid(row=2, column=0, pady=20, padx=60)

        

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
        self.liste_repas = get_all_repas()
        for widget in self.repas_list_frame.winfo_children():
            widget.destroy()

        self.create_liste_repas()

    def create_liste_repas(self):

        def select_repas(repas):
            for widget in self.selected_repas_frame.winfo_children():
                widget.destroy()
            for index, item in enumerate(repas.items):
                item_label = ctk.CTkLabel(
                    self.selected_repas_frame,
                    text_color="white",
                    text=item.aliment.nom
                )
                item_label.grid(row=index)
                create_repas_item_card(self.selected_repas_frame, item, index, 0)
            label_total = ctk.CTkLabel(
                self.selected_repas_frame,
                fg_color="transparent",
                text_color="white",
                font=("Arial", 20, "bold"),
                text=f"total: {repas.calories_total()} cal"
            )
            label_total.grid(row = index + 1)
            print(repas.ID)
            print(repas.type_repas)
                       
        for index, repa in enumerate(self.liste_repas):
            create_repas_card(self.repas_list_frame, repa, index, 0, select_repas)

    def filter_repas_by_date(self, event=None):
            for widget in self.repas_list_frame.winfo_children():
                widget.destroy()

            selected_date = self.date_picker.get()
            self.liste_repas = get_repas_by_date(selected_date)
            self.create_liste_repas()
            


        

    