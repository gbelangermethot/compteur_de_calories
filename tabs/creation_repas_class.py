import customtkinter as ctk
from functions import *

class creation_repas_class:
    def __init__(self, parent):
        #configuration du tab
        parent.configure(fg_color="#035efc")

        parent.grid_rowconfigure(0, weight=1)

        parent.grid_columnconfigure(0, weight=1)
        parent.grid_columnconfigure(1, weight=1)

        #variabe globales
        self.selected_aliment = None
        self.current_repas = None
        self.type_repas_var = ctk.StringVar(value="Déjeuner")

        #creation de la liste d'aliments
        self.aliments = get_all_aliments()

        #panneaux d'affichages droit et gauche
        self.left_panel = ctk.CTkFrame(parent, fg_color="transparent")
        self.left_panel.grid(row=0, column=0, padx=(60,10), pady=20, sticky="nsew")

        self.right_panel = ctk.CTkFrame(parent, fg_color="transparent")
        self.right_panel.grid(row=0, column=1, padx=10, pady=20, sticky="nsew")
        self.right_panel.grid_columnconfigure(0, weight=1)
        self.right_panel.grid_rowconfigure(1, weight=1)

        #entete panneau gauche
        self.header = ctk.CTkLabel(
            self.left_panel,
            text="Construisez votre repas",
            font=("Arial", 20),
            text_color="white"
        )
        self.header.grid(row=0, column=0, pady=20)

        #cadre pour l'item selectionné
        self.selected_aliment_frame = ctk.CTkFrame(self.left_panel, fg_color="transparent")
        self.selected_aliment_frame.grid(row=1, column=0, pady=20)

        #etiquette pour l'item selectionné
        self.selected_aliment_label = ctk.CTkLabel(
            self.selected_aliment_frame,
            text="Aucun aliment sélectionné",
            font=("Arial", 20),
            text_color="white"
        )
        self.selected_aliment_label.grid(row=0, column=0, pady=(0, 15))

        #cadre pour entrer le poids
        self.entry_frame = ctk.CTkFrame(self.selected_aliment_frame, fg_color="transparent")
        self.entry_frame.grid(row=1, column=0, pady=(0, 15))
        

        #etiquette pour le poids
        self.poids_label = ctk.CTkLabel(
            self.entry_frame,
            text="Poids:",
            font=("Arial", 16),
            text_color="white"
        )
        self.poids_label.grid(row=0, column=0, padx=(0, 10))

        #entrée texte pour le poids
        self.poids_entry = ctk.CTkEntry(
            self.entry_frame,
            placeholder_text="Poids en grammes"
        )
        self.poids_entry.grid(row=0, column=1)

        #cadre pour les boutton ajouter item et scroll select typ repas
        self.button_frame = ctk.CTkFrame(self.selected_aliment_frame, fg_color="transparent")
        self.button_frame.grid(row=2, column=0, pady=(0, 15))        

        #boutton pour ajouter l'item
        self.ajouter_item_button = ctk.CTkButton(
            self.button_frame,
            text="ajouter l'aliment au repas",
            command=self.on_ajouter_item_click
        )
        self.ajouter_item_button.grid(row=0, column=0, padx=10)

        #scroll select pour selectionner le type d repas
        self.type_repas_menu = ctk.CTkOptionMenu(
            self.button_frame,
            values=["Déjeuner", "Dîner", "Souper", "Collation"],
            variable=self.type_repas_var
        )
        self.type_repas_menu.grid(row=0, column=1, padx=10)

        #cadre pour les items du repas courrant
        self.repas_items_frame = ctk.CTkFrame(self.left_panel, fg_color="transparent")
        self.repas_items_frame.grid(row=3, column=0, pady=15)

        #cadre pour entete de la liste de repas
        self.header_frame = ctk.CTkFrame(self.right_panel, fg_color="transparent")
        self.header_frame.grid(row=0)

        #entete de la liste de repas
        self.liste_aliments_header = ctk.CTkLabel(self.header_frame, text="Choisissez un item",  font=("Arial", 20), text_color="white", padx=20, pady=20)
        self.liste_aliments_header.grid(row=0, column=0, padx=20)

        

        #entree pour filtrer les aliments
        self.aliment_filtre_entry = ctk.CTkEntry(self.header_frame, height=20, width=220)
        self.aliment_filtre_entry.grid(row=0, column=1, sticky="w")
        self.aliment_filtre_entry.bind(
            "<KeyRelease>",
            self.on_filtre_change
        )


        #cadre d'affichage de la liste d'aliments
        self.liste_aliment_frame = ctk.CTkScrollableFrame(self.right_panel, fg_color="transparent")
        self.liste_aliment_frame.grid(row=1, column=0, sticky="nsew")
        self.liste_aliment_frame.grid_columnconfigure(0, weight=1)

        #boucle affichant chacun des aliments
        self.afficher_liste_aliments(self.aliments)

    #fonction affichant chacun des aliments
    def afficher_liste_aliments(self, liste_aliments):
        for index, aliment in enumerate(liste_aliments, start=0):
            create_aliment_card(self.liste_aliment_frame, aliment, index, 0, self.select_aliment)

    #fonction créant un repas et ajoutasnt les items au repas courrant
    def on_ajouter_item_click(self):
            
            #texte affiché dans l'etiquette de l'aliment selectionné si aucun aliment ne l'est et on sort de la fonction
            if self.selected_aliment is None:
                self.selected_aliment_label.configure(
                    text="Sélectionnez un aliment"
                )
                return

            #on essaie de prendre le poids en int
            try:
                poids = int(self.poids_entry.get())
            
            #si echoue on affiche poids invalide et on sort de la fonction
            except ValueError:
                self.selected_aliment_label.configure(
                    text="Poids invalide"
                )
                return

            #s'il n'y a pas de repas courrant, on en creer un
            if self.current_repas is None:
                type_repas = self.type_repas_var.get()
                item_repas = create_item_repas(
                    self.selected_aliment,
                    poids,
                    repas=None,
                    type_repas=type_repas
                )

            #sinon on ajout l'item au repas courrant
            else:
                item_repas = create_item_repas(
                    self.selected_aliment,
                    poids,
                    self.current_repas
                )

            #le repas courrant devient le repas de l'item repas que nous venons de creer
            self.current_repas = item_repas.repas

            #on ajoute l'item a la list d'item du repas courrant
            self.current_repas.items.append(item_repas)

            #on raffraichit l'affichage pour afficher l'aliment
            self.refresh_current_repas_display()
            print(f"{self.current_repas.ID}, {self.current_repas.type_repas}, {self.current_repas.date}, {self.current_repas.items}")

    #fonction activant le filtre
    def on_filtre_change(self, event=None):
        texte = self.aliment_filtre_entry.get()

        if texte == "":
            self.refresh_aliment_list()
        else:
            self.filtrer_aliments(texte)
    
    def filtrer_aliments(self, nom):
        self.aliments = get_aliments_by_nom(nom)
        for widget in self.liste_aliment_frame.winfo_children():
            widget.destroy()
        self.afficher_liste_aliments(self.aliments)
        
    
    def refresh_aliment_list(self):
        self.aliments = get_all_aliments()
        for widget in self.liste_aliment_frame.winfo_children():
            widget.destroy()
        self.afficher_liste_aliments(self.aliments)

    def refresh_current_repas_display(self):
        #on detruis laffichage tu repas
        for widget in self.repas_items_frame.winfo_children():
            widget.destroy()

        #s'il n'y a pas de repas courrant, on sort de la fonction
        if self.current_repas is None:
            return

        #sinon pour chaque item repas dans le repas, on les affiche
        for index, item in enumerate(self.current_repas.items):
            self.item_label = ctk.CTkLabel(
                self.repas_items_frame,
                text=f"{item.aliment.nom} - {item.poids}g - {item.calories():.1f} calories",
                font=("Arial", 14),
                text_color="white"
            )
            self.item_label.grid(row=index, column=0, sticky="w", pady=3)

        #cadre pour afficher le total et le boutton pour fermer le repas
        self.footer_frame = ctk.CTkFrame(self.repas_items_frame, fg_color="transparent")
        self.footer_frame.grid(row=len(self.current_repas.items), column=0, sticky="w", pady=(10, 0))

        #etiquette qui affiche le total
        self.total_label = ctk.CTkLabel(
            self.footer_frame,
            text=f"Total: {self.current_repas.calories_total():.1f} calories",
            font=("Arial", 16, "bold"),
            text_color="white"
        )
        self.total_label.grid(row=0, column=0)

        #boutton pour fermer le repas
        self.fermer_repas_button = ctk.CTkButton(
            self.footer_frame,
            text="Fermer le repas",
            command=self.fermer_repas
        )
        self.fermer_repas_button.grid(row=0, column=1, padx=10, pady=10)

    #fonction pour fermer le repas
    def fermer_repas(self):
        self.current_repas = None
        self.refresh_current_repas_display()

    #fonction pour selectionner un aliment.
    def select_aliment(self, aliment):
        self.selected_aliment = aliment
        self.selected_aliment_label.configure(text=aliment.nom)

    



