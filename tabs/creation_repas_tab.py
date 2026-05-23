import customtkinter as ctk
from functions import *

def build_creation_repas_tab(creation_repas_tab):
    creation_repas_tab.configure(fg_color="#035efc")

    creation_repas_tab.grid_rowconfigure(1, weight=1)

    creation_repas_tab.grid_columnconfigure(0, weight=1)
    creation_repas_tab.grid_columnconfigure(1, weight=1)

    selected_aliment = None
    current_repas = None

    left_panel = ctk.CTkFrame(creation_repas_tab, fg_color="transparent")
    left_panel.grid(row=1, column=0, padx=(60,10), pady=20, sticky="nsew")
    

    right_panel = ctk.CTkScrollableFrame(creation_repas_tab, fg_color="transparent")
    right_panel.grid(row=1, column=1, padx=10, pady=20, sticky="nsew")
    right_panel.grid_columnconfigure(0, weight=1)

    header = ctk.CTkLabel(
        left_panel,
        text="Construisez votre repas",
        font=("Arial", 20),
        text_color="white"
    )
    header.grid(row=0, column=0, pady=20)

    selected_aliment_frame = ctk.CTkFrame(left_panel, fg_color="transparent")
    selected_aliment_frame.grid(row=1, column=0, pady=20)

    selected_aliment_label = ctk.CTkLabel(
        selected_aliment_frame,
        text="Aucun aliment sélectionné",
        font=("Arial", 20),
        text_color="white"
    )
    selected_aliment_label.grid(row=0, column=0, pady=(0, 15))

    entry_frame = ctk.CTkFrame(selected_aliment_frame, fg_color="transparent")
    entry_frame.grid(row=1, column=0, pady=(0, 15))

    poids_label = ctk.CTkLabel(
        entry_frame,
        text="Poids:",
        font=("Arial", 16),
        text_color="white"
    )
    poids_label.grid(row=0, column=0, padx=(0, 10))

    poids_entry = ctk.CTkEntry(
        entry_frame,
        placeholder_text="Poids en grammes"
    )
    poids_entry.grid(row=0, column=1)

    def on_ajouter_item_click():
        nonlocal current_repas

        if selected_aliment is None:
            selected_aliment_label.configure(
                text="Sélectionnez un aliment"
            )
            return

        try:
            poids = int(poids_entry.get())

        except ValueError:
            selected_aliment_label.configure(
                text="Poids invalide"
            )
            return

        if current_repas is None:

            type_repas = type_repas_var.get()

            item_repas = create_item_repas(
                selected_aliment,
                poids,
                repas=None,
                type_repas=type_repas
            )
        else:
            item_repas = create_item_repas(
                selected_aliment,
                poids,
                current_repas
            )

        current_repas = item_repas.repas
        current_repas.items.append(item_repas)
        refresh_current_repas_display()
        print(f"{current_repas.ID}, {current_repas.type_repas}, {current_repas.date}, {current_repas.items}")

        
    button_frame = ctk.CTkFrame(selected_aliment_frame, fg_color="transparent")
    button_frame.grid(row=2, column=0, pady=(0, 15))        

    ajouter_item_button = ctk.CTkButton(
        button_frame,
        text="ajouter l'aliment au repas",
        command=on_ajouter_item_click
    )
    ajouter_item_button.grid(row=0, column=0, padx=10)

    type_repas_var = ctk.StringVar(value="Déjeuner")

    type_repas_menu = ctk.CTkOptionMenu(
        button_frame,
        values=["Déjeuner", "Dîner", "Souper", "Collation"],
        variable=type_repas_var
    )
    type_repas_menu.grid(row=0, column=1, padx=10)

    meal_items_frame = ctk.CTkFrame(left_panel, fg_color="transparent")
    meal_items_frame.grid(row=3, column=0, pady=15)

    def refresh_current_repas_display():
        for widget in meal_items_frame.winfo_children():
            widget.destroy()

        if current_repas is None:
            return

        for index, item in enumerate(current_repas.items):
            item_label = ctk.CTkLabel(
                meal_items_frame,
                text=f"{item.aliment.nom} - {item.poids}g - {item.calories():.1f} calories",
                font=("Arial", 14),
                text_color="white"
            )
            item_label.grid(row=index, column=0, sticky="w", pady=3)

        footer_frame = ctk.CTkFrame(meal_items_frame, fg_color="transparent")
        footer_frame.grid(row=len(current_repas.items), column=0, sticky="w", pady=(10, 0))

        total_label = ctk.CTkLabel(
            footer_frame,
            text=f"Total: {current_repas.calories_total():.1f} calories",
            font=("Arial", 16, "bold"),
            text_color="white"
        )
        total_label.grid(row=0, column=0)

        def fermer_repas():
            nonlocal current_repas
            current_repas = None
            refresh_current_repas_display()

        fermer_repas_button = ctk.CTkButton(
            footer_frame,
            text="Fermer le repas",
            command=fermer_repas
        )

        fermer_repas_button.grid(row=0, column=1, padx=10, pady=10)

    def select_aliment(aliment):
        nonlocal selected_aliment
        selected_aliment = aliment
        selected_aliment_label.configure(text=aliment.nom)
        


    header = ctk.CTkLabel(right_panel, text="Liste des items de repas",  font=("Arial", 20), text_color="white", padx=20, pady=20)
    header.grid(row=0, column=0, padx=20)

   

    aliments = get_all_aliments()

    for index, aliment in enumerate(aliments, start=1):
        create_aliment_card(right_panel, aliment, index, 0, select_aliment)


    