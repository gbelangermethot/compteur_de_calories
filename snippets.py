import sqlite3
from aliment import *

connection = sqlite3.connect('compteur_calories.db')

cursor = connection.cursor()

# cursor.execute("""CREATE TABLE aliments (
#                 ID integer PRIMARY KEY AUTOINCREMENT,
#                 name text NOT NULL,
#                 picture text,
#                 caloriesPerGram real  NOT NULL
#                 )""")

aliments = []

aliment_1 = Aliment(1, 'Cereal croque nature', 'images/croque_nature.png', 1.7)
aliment_2 = Aliment(2, 'Toast au beurre de peanut', 'images/peanut_butter_toast.png', 4.2)
aliment_3 = Aliment(3, 'Spaghetti bolognaise', 'images/spaghetti_bolognaise.png', 1.6)
aliment_4 = Aliment(4, 'Poitrine de poulet marinee', 'images/poitrine_poulet.png', 1.8)

aliments.append(aliment_1)
aliments.append(aliment_2)
aliments.append(aliment_3)
aliments.append(aliment_4)

for aliment in aliments:
    cursor.execute("""
    INSERT INTO aliments (
        nom,
        image,
        calories_par_gram
    )
    VALUES (:nom, :image, :calories_par_gram)""", 
    {'nom': aliment.nom, 'image': aliment.image, 'calories_par_gram': aliment.calories_par_gram })

cursor.execute("SELECT * FROM aliments")
        

# cursor.execute("""
# INSERT INTO aliments (
#     name,
#     picture,
#     caloriesPerGram
# )
# VALUES (?, ?, ?)""", 
# (aliment_1.name, aliment_1.picture, aliment_1.caloriesPerGram))



connection.commit()

print(cursor.fetchall())

connection.close()