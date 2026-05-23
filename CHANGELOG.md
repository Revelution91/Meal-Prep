# Changelog

All notable changes to the Weekly Meal Prep Generator will be documented in this file.

## [1.4.0] - 2026-05-22

### Added
* **Interactive Grocery Planner:** Introduced a dedicated "Planner" cart that aggregates saved recipes and dynamically scales ingredient amounts based on user-defined serving sizes.
* **Persistent Checkboxes:** Added interactive checkboxes to the grocery list that save their checked/unchecked state directly to the browser, allowing users to use the app seamlessly at the grocery store.
* **15 New Recipes:** Expanded the database to 37 recipes, removing previous dietary restrictions to include pork, seafood, tofu, sweet potatoes, and beans.
* **Tagging & Filter System:** Implemented a backend metadata tagging system (`protein`, `carb`, `veggie`) to allow users to filter the Randomizer pool before rolling the dice.
* **Dynamic Ingredient Scaling:** Built a Regex helper function that parses ingredient strings and scales the physical quantities mathematically based on a UI slider.

### Changed
* **Data Architecture Migration:** Separated the massive recipe dictionary from `app.py` into a standalone `recipes.py` file to clean up the main application logic and improve modularity.
* **True Persistence Engine:** Replaced ephemeral Streamlit session states with `streamlit-local-storage` to save Favorites, Planners, and Checkbox states natively to the user's browser, preventing data loss on app refresh.
* **100% Callback Architecture:** Completely removed `st.rerun()` calls across the entire application, replacing them with `on_click` and `on_change` callbacks to eliminate the "emergency brake" saving bug.
* **Stateful Navigation Menu:** Decommissioned the stateless `st.tabs` component. Replaced it with a custom horizontal radio menu bound to session state to permanently fix the bug where the app would jump back to the first tab after a user action. 


## [1.3.0] - 2026-05-21

### Added
* **Tabbed Interface:** Introduced a clean main-page navigation system using tabs to separate the randomizer, complete recipe collection, and personal favorites.
* **Card Grid Layout:** Implemented a modern, 3-column responsive card layout to display recipes visually with their title and key macros at a glance.
* **Favorites System:** Added a session state-driven "Save Recipe" button to bookmark meals dynamically during use.
* **Mobile View Optimization:** Programmed the grid interface to completely hide when a specific recipe is opened, adding a dedicated `⬅️ Back` navigation button to remove vertical scrolling friction on phones.

### Changed
* **UI Architecture Overhaul:** Fully decommissioned the legacy sidebar selection scheme in favor of the new in-line tabbed layout.


## [1.2.0] - 2026-05-21

### Added

* **4 New Delish-Inspired Recipes:** 
  * Chicken Club Egg White Wraps
  * Italian Grinder Chicken Salad Wraps
  * Easy Peanut Chicken Protein Bowls
  * BBQ Chicken Power Bowls
* **3 New Burrito Recipes:** 
  * Chicken Bacon Ranch Burritos
  * Buffalo Chicken Burritos
  * Steak Fajita Burritos
* **Custom Condiment:** Added a custom Jalapeno Garlic Aioli (jalapeno, garlic, mayonnaise, honey, salt) to the database.
* **Custom Condiment:** Added an Authentic Mac Sauce recipe based on exact measurements (mayonnaise, sweet pickle relish, yellow mustard, white vinegar, paprika, garlic powder, onion powder).

### Changed
* **Global Rice Update:** Completely removed all instances of "brown rice" across the entire database. Replaced exclusively with "white rice" or "jasmine rice".
* **Recipe Swap:** Replaced "High-Protein Big Mac Casserole" with Oh Snap Macros-style "Big Mac Bowls" using the authentic Mac Sauce recipe.
* **Macro Adjustments:** Updated the nutritional macro profiles (Calories and Fat) for meals utilizing the new Jalapeno Garlic Aioli to account for the mayonnaise and honey.

### Updated
* **Recipe Enhancements:** Integrated the new Jalapeno Garlic Aioli blending instructions and ingredient lists into the following existing recipes to complement their flavor profiles:
  * Fajita Steak Bowls
  * Southwest Ground Beef Skillet
  * Slow Cooker Salsa Chicken
  * Steak Fajita Burritos


## [1.1.0] - 2026-05-21

### Added
- **Manual Recipe Navigator:** Added a sidebar dropdown selection menu (`st.selectbox`) allowing users to manually view recipes even after closing or refreshing the app.
- **Macronutrient Tracking:** Integrated a macro information section under selected recipes using Streamlit's metric cards (`st.metric`). Shows Calories, Protein, Carbs, and Fat per serving.
- **Big Mac Casserole:** Added a new high-protein burger casserole recipe to the database.

### Changed
- **Dietary Preferences:** Swapped all Turkey Bacon variants across all recipes to standard Pork Bacon.
- **Protein Swap:** Converted the Southwest Turkey Skillet into a Lean Ground Beef Skillet.

## [1.0.0] - 2026-05-21
### Added
- Initial release of the random meal prep picker app.
- 15 base high-protein recipes.
- Filtered out all beans and asparagus from the database, substituting air-fried potato sides.