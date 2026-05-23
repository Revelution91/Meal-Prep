# Weekly Meal Prep Generator & Planner

A comprehensive, stateful web application designed to help you discover, scale, and plan high-protein meals for the week. Say goodbye to spreadsheet meal planning and manual grocery math.

## Features
* **Smart Randomizer with Filters:** Don't know what to eat? Filter by specific proteins, carbs, or veggies, and let the app choose a matching meal.
* **Recipe Book:** Browse a growing database of 37+ diverse recipes in a clean, mobile-friendly card grid.
* **Persistent Favorites:** Save the meals you love. Your favorites are stored directly in your browser's Local Storage, meaning they'll still be there even after you close the tab.
* **Dynamic Portion Scaling:** Use the interactive slider to choose between 1 and 14 servings. The app automatically recalculates the ingredient amounts for you.
* **Interactive Grocery Planner:** Add meals directly to your cart. The app generates a unified, scaled grocery list with persistent checkboxes you can use at the store.
* **Stateful Navigation:** A custom 100% callback-driven architecture ensures you never lose your place or experience page-jumping while navigating.

## Built With
* **Python**
* **Streamlit** (Frontend framework)
* **Streamlit-Local-Storage** (Browser data persistence)
* **Regex** (Ingredient math and scaling)

## How to run locally
1. Clone this repository.
2. Install the required dependencies: `pip install -r requirements.txt` 
3. Run the app: `python -m streamlit run app.py`