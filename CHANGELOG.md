# Changelog

All notable changes to the Weekly Meal Prep Generator will be documented in this file.

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