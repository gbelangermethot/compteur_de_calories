# Compteur de Calories 📊

Une application desktop pour suivre votre consommation de calories au quotidien. Construisez vos repas, gérez votre base d'aliments et consultez votre historique de repas.

## Fonctionnalités

### 🍽️ Construire votre repas
- Sélectionnez des aliments de votre base de données
- Ajustez les quantités en grammes
- Visualisez le total de calories instantanément
- Enregistrez votre repas avec la date et le type (dejeuner, diner, pouper, collation)

### 📜 Repas passés
- Consultez l'historique de tous vos repas
- Filtrez par date pour retrouver vos repas facilement
- Visualisez les détails de chaque repas et ses calories

### ➕ Ajouter un aliment
- Créez vos propres aliments
- Définissez les calories par gramme
- Ajoutez une image pour identifier facilement vos aliments

## Installation

### Prérequis
- Python 3.7+
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. Clonez le repository :
```bash
git clone https://github.com/yourusername/calorie_counter.git
cd calorie_counter
```

2. Installez les dépendances :
```bash
pip install customtkinter pillow tkcalendar
```

3. Lancez l'application :
```bash
python main.py
```

## Structure du projet

```
calorie_counter/
├── main.py                          # Fichier principal de l'application
├── aliment.py                       # Classe Aliment
├── repas.py                         # Classe Repas
├── item_repas.py                    # Classe ItemRepas
├── functions.py                     # Fonctions de gestion de la base de données
├── snippets.py                      # Fonctions utilitaires
├── tabs/
│   ├── creation_aliment_tab.py      # Onglet d'ajout d'aliment
│   ├── creation_repas_class.py      # Onglet de construction de repas
│   └── repas_passes_class.py        # Onglet d'affichage des repas passés
├── images/                          # Dossier des images d'aliments
└── compteur_calories.db             # Base de données SQLite
```

## Utilisation

### Créer un repas
1. Ouvrez l'onglet **"Construire votre repas"**
2. Sélectionnez les aliments que vous souhaitez ajouter
3. Indiquez la quantité en grammes
4. Consultez le total de calories
5. Enregistrez votre repas

### Consulter l'historique
1. Ouvrez l'onglet **"Repas passé"**
2. Utilisez le sélecteur de date pour filtrer
3. Cliquez sur un repas pour voir ses détails

### Ajouter un nouvel aliment
1. Ouvrez l'onglet **"Ajouter un aliment"**
2. Remplissez le nom de l'aliment
3. Indiquez les calories par gramme
4. Optionnel : ajoutez une image
5. Validez l'ajout

## Dépendances

- **customtkinter** - Interface graphique moderne
- **Pillow** - Gestion des images
- **tkcalendar** - Widget de sélection de date
- **sqlite3** - Base de données (inclus avec Python)

## Base de données

L'application utilise une base de données SQLite (`compteur_calories.db`) avec les tables :
- `aliments` - Contient les aliments disponibles
- `repas` - Contient les repas enregistrés
- Et autres tables de relations nécessaires

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
- Signaler des bugs
- Suggérer des améliorations
- Soumettre des pull requests

## Licence

Ce projet est libre d'utilisation et de modification.

## Auteur

Créé par Guillaume

---

**Bon suivi calorique! 💪**
