import customtkinter as ctk
import sqlite3
from PIL import Image
from aliment import Aliment
from datetime import datetime
from item_repas import *
from repas import *

DB_NAME = "compteur_calories.db"

def get_all_aliments():
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM aliments ORDER BY nom")
        pulled_aliments= cursor.fetchall()
        aliments = []
        for pulled_aliment in pulled_aliments:
            aliment = Aliment(
                pulled_aliment[0],
                pulled_aliment[1],
                pulled_aliment[2],
                pulled_aliment[3]
            )
            aliments.append(aliment)
    return aliments

def get_aliments_by_nom(nom):
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM aliments WHERE nom like :nom ORDER BY nom",{'nom' : f"%{nom}%"})
        pulled_aliments= cursor.fetchall()
        aliments = []
        for pulled_aliment in pulled_aliments:
            aliment = Aliment(
                pulled_aliment[0],
                pulled_aliment[1],
                pulled_aliment[2],
                pulled_aliment[3]
            )
            aliments.append(aliment)
    return aliments


def get_all_repas():
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM repas ORDER BY ID DESC")
        pulled_repas= cursor.fetchall()
        repas = []
        for pulled_repa in pulled_repas:
            repa = get_repas_by_id(pulled_repa[0])
            cursor.execute("SELECT * FROM item_repas WHERE repasID = :repasID", {'repasID': repa.ID })
            pulled_items = cursor.fetchall()
            
            items = []

            for pulled_item in pulled_items:
                item = get_item_repas_by_id(pulled_item[0])
                items.append(item)

            repa.items = items
           
            repas.append(repa)
    return repas

def get_repas_by_date(date):
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM repas WHERE date(date) = :date ORDER BY ID DESC", {'date': date})
        pulled_repas= cursor.fetchall()
        repas = []
        for pulled_repa in pulled_repas:
            repa = get_repas_by_id(pulled_repa[0])
            cursor.execute("SELECT * FROM item_repas WHERE repasID = :repasID", {'repasID': repa.ID })
            pulled_items = cursor.fetchall()
            
            items = []

            for pulled_item in pulled_items:
                item = get_item_repas_by_id(pulled_item[0])
                items.append(item)

            repa.items = items
           
            repas.append(repa)
    return repas
        


def get_aliment_by_id(id):
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM aliments WHERE ID = :id", {'id':id})
        pulled_aliment = cursor.fetchone()
        aliment = Aliment(
            pulled_aliment[0],
            pulled_aliment[1],
            pulled_aliment[2],
            pulled_aliment[3]
        )
    return aliment

def get_repas_by_id(id):
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM repas WHERE ID = :id", {'id':id})
        pulled_repas = cursor.fetchone()
        repas = Repas(
            pulled_repas[0],
            pulled_repas[1],
            pulled_repas[2]
        )
    return repas

def get_item_repas_by_id(id):
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM item_repas WHERE ID = :id", {'id':id})
        pulled_item_repas = cursor.fetchone()
        repas = get_repas_by_id(pulled_item_repas[2])
        aliment =get_aliment_by_id(pulled_item_repas[1])
        item_repas = Item_repas(
            pulled_item_repas[0],
            repas,
            aliment,
            pulled_item_repas[3]
        )
    return item_repas

def create_repas(type_repas):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO repas (date, type)
            VALUES (?, ?)
        """, (date, type_repas))
        return cursor.lastrowid
    
def create_item_repas(aliment, poids, repas=None, type_repas=None):
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        if repas is not None:
            repasID = repas.ID
        else:
            repasID = create_repas(type_repas)
            repas = Repas(repasID, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), type_repas)

        cursor.execute("""
            INSERT INTO item_repas (alimentID, repasID, poids)
            VALUES (:alimentID, :repasID, :poids)
        """, {
            "alimentID": aliment.ID,
            "repasID": repasID,
            "poids": poids
        })
        item_id = cursor.lastrowid

    return Item_repas(item_id, repas, aliment, poids)

def create_aliment(nom, calories_par_gram, image):
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO aliments (nom, image, calories_par_gram)
                       VALUES(:nom, :image, :calories_par_gram)""", 
                       {'nom' : nom,
                        'image': image,
                        'calories_par_gram': calories_par_gram})
        return {'nom' : nom,
                'image': image,
                'calories_par_gram': calories_par_gram}

def create_aliment_card(parent, aliment, row, column, on_select):
    aliment_frame = ctk.CTkFrame(parent, corner_radius=20, fg_color="#FFFFFF")
    aliment_frame.grid(row=row, column=column, padx=5, pady=10, sticky="ew")
    aliment_frame.grid_columnconfigure(1, weight=1)
    aliment_frame.bind("<Button-1>", lambda event: on_select(aliment))

    image = ctk.CTkImage(
        light_image=Image.open(aliment.image),
        dark_image=Image.open(aliment.image),
        size=(80, 80)
    )

    image_label = ctk.CTkLabel(aliment_frame, image=image, text="")
    image_label.image = image
    image_label.grid(row=0, column=0, rowspan=2, padx=15, pady=15)
    image_label.bind("<Button-1>", lambda event: on_select(aliment))

    name_label = ctk.CTkLabel(
        aliment_frame, 
        text=aliment.nom, 
        font=("Arial", 18, "bold"),
        text_color="black")
    name_label.grid(row=0, column=1, sticky="w", padx=20, pady=(20, 5))
    name_label.bind("<Button-1>", lambda event: on_select(aliment))

    calories_label = ctk.CTkLabel(
        aliment_frame,
        text=f"{aliment.calories_par_gram} calories / gram",
        font=("Arial", 14),
        text_color="black"
    )
    calories_label.grid(row=1, column=1, sticky="w", padx=10, pady=(0, 20))
    calories_label.bind("<Button-1>", lambda event: on_select(aliment))

def create_repas_card(parent, repas, row, column, on_select):
    repas_frame = ctk.CTkFrame(parent, corner_radius=20, fg_color="#FFFFFF")
    repas_frame.grid(row=row, column=column, pady=10, sticky="ew")
    repas_frame.grid_columnconfigure(0, weight=1)
    repas_frame.grid_columnconfigure(1, weight=1)
    repas_frame.bind("<Button-1>", lambda event: on_select(repas))

    left_frame = ctk.CTkFrame(repas_frame, fg_color="transparent")
    left_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nw")
    left_frame.bind("<Button-1>", lambda event: on_select(repas))

    right_frame = ctk.CTkFrame(repas_frame, fg_color="transparent")
    right_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nw")
    right_frame.bind("<Button-1>", lambda event: on_select(repas))

    type_label = ctk.CTkLabel(
        left_frame,
        text=repas.type_repas,
        font=("Arial", 18, "bold"),
        text_color="black"
    )
    type_label.grid(row=0, column=0, sticky="w")
    type_label.bind("<Button-1>", lambda event: on_select(repas))

    date_label = ctk.CTkLabel(
        left_frame,
        text=repas.date,
        font=("Arial", 14),
        text_color="gray"
    )
    date_label.grid(row=1, column=0, sticky="w", pady=(10, 10))
    date_label.bind("<Button-1>", lambda event: on_select(repas))

    total_label = ctk.CTkLabel(
        left_frame,
        text=f"Total: {repas.calories_total():.1f} cal",
        font=("Arial", 14),
        text_color="black"
    )
    total_label.grid(row=2, column=0, sticky="w")
    total_label.bind("<Button-1>", lambda event: on_select(repas))

    for index, item in enumerate(repas.items):
        item_label = ctk.CTkLabel(
            right_frame,
            text=f"{item.aliment.nom} - {item.calories():.1f} cal",
            font=("Arial", 14),
            text_color="black"
        )
        item_label.grid(row=index, column=0, sticky="w", pady=2)
        item_label.bind("<Button-1>", lambda event: on_select(repas))

def create_repas_item_card(parent, repas_item, row, column):
    repas_item_frame = ctk.CTkFrame(parent, corner_radius=20, fg_color="#FFFFFF")
    repas_item_frame.grid(row=row, column=column, pady=10, sticky="ew")
    repas_item_frame.grid_columnconfigure(0, weight=0)
    repas_item_frame.grid_columnconfigure(1, weight=1)
    
    left_frame = ctk.CTkFrame(repas_item_frame, fg_color="transparent")
    left_frame.grid(row=0, column=0, padx=5, pady=20, sticky="nw")

    right_frame = ctk.CTkFrame(repas_item_frame, fg_color="transparent")
    right_frame.grid(row=0, column=1, padx=5, pady=20, sticky="nw")

    image = ctk.CTkImage(
        light_image=Image.open(repas_item.aliment.image),
        dark_image=Image.open(repas_item.aliment.image),
        size=(80, 80)
    )
    
    image_label = ctk.CTkLabel(left_frame, image=image, text="")
    image_label.image = image
    image_label.grid(row=0, column=0, padx=15, pady=15)

    aliment_label = ctk.CTkLabel(
        right_frame,
        text=repas_item.aliment.nom,
        font=("Arial", 14, "bold"),
        text_color="black"
    )
    aliment_label.grid(row=0, column=0, padx=5, sticky="w", pady=(10, 10))
    
    poids_label = ctk.CTkLabel(
        right_frame,
        text=f"Poids: {repas_item.poids:.1f} g",
        font=("Arial", 14),
        text_color="black"
    )
    poids_label.grid(row=1, column=0, padx=5, sticky="w")

    calories_label = ctk.CTkLabel(
        right_frame,
        text=f"Calories: {repas_item.calories():.1f} cal",
        font=("Arial", 14),
        text_color="black"
    )
    calories_label.grid(row=2, column=0, sticky="w")
        