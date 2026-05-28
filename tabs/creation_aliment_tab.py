import customtkinter as ctk
from functions import *
from tkinter import filedialog
import shutil
import os

def build_creation_aliment_tab(creation_aliment_tab):
    creation_aliment_tab.configure(fg_color="#035efc")

    creation_aliment_tab.grid_columnconfigure(0, weight=1)

    header = ctk.CTkLabel(
        creation_aliment_tab, 
        fg_color="transparent",
        text="Creez un aliment",
        text_color="White",
        font=("Arial", 20, "bold"))
    header.grid(row=0, pady=20)

    entry_frame = ctk.CTkFrame(creation_aliment_tab, fg_color="transparent")
    entry_frame.grid(row=1, sticky="nsew")

    entry_frame.grid_columnconfigure(0, weight=1)
    entry_frame.grid_columnconfigure(1, weight=1)

    aliment_nom_label = ctk.CTkLabel(
        entry_frame,
        fg_color="transparent",
        text="Nom de l'aliment",
        text_color="White",
        pady=10,
        font=("Arial", 20,))
    aliment_nom_label.grid(row=0, column=0, padx=(0, 20), sticky="e")

    aliment_nom_entry = ctk.CTkEntry(entry_frame, height=20, width=220)
    aliment_nom_entry.grid(row=0, column=1, sticky="w")

    aliment_calories_label = ctk.CTkLabel(
        entry_frame,
        fg_color="transparent",
        text="Nombre de calories par gramme",
        text_color="White",
        pady=10,
        font=("Arial", 20,))
    aliment_calories_label.grid(row=1, column=0, padx=(0, 20), sticky="e")

    aliment_calories_entry = ctk.CTkEntry(entry_frame, height=20, width=220)
    aliment_calories_entry.grid(row=1, column=1, sticky="w")

    selected_image_path = None

    def choisir_image():

        nonlocal selected_image_path

        file_path = filedialog.askopenfilename(
            title="Choisir une image",
            filetypes=[
                ("Images", "*.png *.jpg *.jpeg")
            ]
        )

        if not file_path:
            return

        file_name = os.path.basename(file_path)
        destination = os.path.join("images", file_name)
        shutil.copy(file_path, destination)
        print(destination)

        selected_image_path = destination

        image_path_label.configure(
                text=destination
            )


    image_button = ctk.CTkButton(
        entry_frame,
        text="Choisir une image",
        command=choisir_image
    )
    image_button.grid(row=2, column=0, pady=20, padx=20, sticky="e")

    image_path_label = ctk.CTkLabel(
        entry_frame,
        fg_color="transparent",
        text="Chemin de l'image",
        text_color="White",
        pady=10,
        font=("Arial", 20,))
    image_path_label.grid(row=2, column=1, sticky="w")

    def save_aliment():
        nom = aliment_nom_entry.get()
        calories_par_gram = float(aliment_calories_entry.get())

        print(create_aliment(nom, calories_par_gram, selected_image_path))

        image_path_label.configure(
                text="Chemin de l'image"
            )
        
        aliment_nom_entry.delete(0, "end")
        aliment_calories_entry.delete(0, "end")



    save_button = ctk.CTkButton(
        creation_aliment_tab,
        text="Sauvegarder l'aliment",
        command=save_aliment
    )
    save_button.grid(row=2, column=0, pady=20)

    