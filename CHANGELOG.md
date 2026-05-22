# Changelog

All notable changes to the Weekly Meal Prep Generator will be documented in this file.

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