import streamlit as st
import random

# --- RECIPE DATABASE (With Macros, Regular Bacon, and Beef Swaps) ---
RECIPES = [
    {
        "name": "🍗 Healthy Chicken Bacon Ranch Bowls",
        "macros": {"Calories": 610, "Protein": "52g", "Carbs": "45g", "Fat": "24g"},
        "ingredients": [
            "2.5 lbs Boneless Skinless Chicken Breast, cubed",
            "10 slices Regular Bacon (pork bacon)",
            "5 cups Broccoli florets",
            "2.5 cups Brown Rice or Jasmine Rice (dry measure)",
            "1 cup Greek Yogurt Ranch Dressing",
            "2 tbsp Olive oil",
            "Salt, pepper, garlic powder, and onion powder"
        ],
        "instructions": (
            "1. Cook the rice according to package instructions. Divide evenly into 5 containers.\n"
            "2. Preheat oven to 400°F (200°C). Toss broccoli with 1 tbsp olive oil, salt, and pepper. Roast for 15-20 minutes.\n"
            "3. In a large skillet, cook the chopped bacon until crisp. Remove and set aside.\n"
            "4. In the same skillet, cook the cubed chicken seasoned with garlic and onion powder until cooked through (165°F).\n"
            "5. Assemble: Add chicken, broccoli, and bacon to the rice bowls.\n"
            "6. Top each bowl with ~3 tbsp of Greek yogurt ranch just before eating."
        )
    },
    {
        "name": "🔥 Buffalo Chicken & Sweet Potato Prep",
        "macros": {"Calories": 540, "Protein": "48g", "Carbs": "42g", "Fat": "18g"},
        "ingredients": [
            "2.5 lbs Boneless Skinless Chicken Breast",
            "3 large Sweet Potatoes, cubed",
            "2 Bell Peppers, roughly chopped",
            "1 Red Onion, roughly chopped",
            "1 cup Frank's RedHot Buffalo Sauce",
            "2 tbsp Butter or Ghee (melted)",
            "2 tbsp Olive oil"
        ],
        "instructions": (
            "1. Preheat oven to 425°F (220°C) or use your Air Fryer at 400°F (200°C).\n"
            "2. Toss sweet potatoes, bell peppers, and red onion in olive oil, salt, and pepper. Roast or air fry for 20-25 mins until crispy.\n"
            "3. Cook chicken breasts in a skillet or bake until internal temp reaches 165°F.\n"
            "4. Shred or cube the cooked chicken.\n"
            "5. Whisk melted butter and buffalo sauce together. Toss the chicken in the sauce.\n"
            "6. Divide the roasted veggies and buffalo chicken evenly among 5 containers."
        )
    },
    {
        "name": "🥩 Chimichurri Steak & Air Fried Potatoes",
        "macros": {"Calories": 640, "Protein": "50g", "Carbs": "38g", "Fat": "32g"},
        "ingredients": [
            "2.5 lbs Flank Steak or Sirloin",
            "2 lbs Baby Yellow or Red Potatoes, halved",
            "1 cup Fresh parsley (finely chopped)",
            "1/4 cup Fresh oregano (finely chopped)",
            "4 cloves Garlic, minced",
            "1/3 cup Red wine vinegar",
            "1/2 cup Olive oil",
            "1 tsp Red pepper flakes, Salt and pepper",
            "Cooking spray or extra olive oil for the air fryer"
        ],
        "instructions": (
            "1. Make chimichurri: Mix parsley, oregano, garlic, vinegar, olive oil, red pepper flakes, salt, and pepper. Let sit.\n"
            "2. Toss halved potatoes with a little olive oil, salt, and pepper. Air fry at 400°F (200°C) for 18-20 minutes until golden and crispy. Divide into 5 containers.\n"
            "3. Season steak heavily with salt and pepper. Sear in a hot skillet for 4-5 mins per side. Rest 10 mins, then slice.\n"
            "4. Add sliced steak next to the air-fried potatoes.\n"
            "5. Store chimichurri separately to drizzle over steak and potatoes after reheating."
        )
    },
    {
        "name": "🍔 High-Protein Big Mac Casserole",
        "macros": {"Calories": 580, "Protein": "46g", "Carbs": "35g", "Fat": "28g"},
        "ingredients": [
            "2.5 lbs Lean Ground Beef (93/7)",
            "1 large White Onion, diced",
            "1 bag (20 oz) Frozen Shredded Hashbrowns (thawed)",
            "1.5 cups Reduced-fat Cheddar Cheese, shredded",
            "1 cup Plain Greek Yogurt",
            "3 tbsp Sugar-free Ketchup",
            "2 tbsp Dill Pickle Relish",
            "1 tsp Yellow Mustard",
            "Shredded Iceberg Lettuce and extra diced pickles (for topping)"
        ],
        "instructions": (
            "1. Preheat oven to 400°F (200°C). Spray a 9x13 baking dish.\n"
            "2. Press thawed hashbrowns into the bottom of the dish. Bake for 20 mins.\n"
            "3. Brown the ground beef and diced onion in a skillet. Drain excess fat. Season with salt/pepper.\n"
            "4. Layer beef/onion mixture over the hashbrown crust. Top with shredded cheddar.\n"
            "5. Bake for another 10-15 mins until cheese melts.\n"
            "6. Whisk Greek yogurt, ketchup, relish, and mustard to make the Mac Sauce.\n"
            "7. Divide into 5 portions. Top with fresh lettuce, pickles, and Mac Sauce after reheating."
        )
    },
    {
        "name": "🥩 Fajita Steak & Air Fried Potato Bowls",
        "macros": {"Calories": 620, "Protein": "48g", "Carbs": "40g", "Fat": "30g"},
        "ingredients": [
            "2.5 lbs Skirt Steak or Flank Steak, sliced into strips",
            "3 Bell Peppers (assorted colors), sliced",
            "2 Yellow Onions, sliced",
            "2 lbs Russet or Gold Potatoes, diced into small cubes",
            "2 tbsp Fajita Seasoning",
            "1/2 cup Pico de Gallo",
            "Olive oil"
        ],
        "instructions": (
            "1. Toss diced potatoes in olive oil and 1 tbsp of fajita seasoning. Air fry at 400°F (200°C) for 15-20 minutes, shaking the basket halfway, until crispy.\n"
            "2. Toss steak strips, bell peppers, and onions with remaining fajita seasoning and a drizzle of oil.\n"
            "3. Heat a large skillet over high heat. Cook steak and veggies in batches so they sear, not steam.\n"
            "4. Divide the air-fried potatoes into 5 containers as your base.\n"
            "5. Top with the steak and fajita veggies, and add a side of pico de gallo."
        )
    },
    {
        "name": "🍔 Southwest Ground Beef Skillet",
        "macros": {"Calories": 590, "Protein": "45g", "Carbs": "44g", "Fat": "26g"},
        "ingredients": [
            "2.5 lbs Lean Ground Beef (93/7)",
            "2 Bell Peppers, diced",
            "1 large Yellow Onion, diced",
            "1 cup Sweet Corn (frozen or canned)",
            "2.5 cups Rice (dry measure)",
            "1 packet Taco Seasoning",
            "1 cup Shredded Monterey Jack cheese"
        ],
        "instructions": (
            "1. Cook the rice and distribute into 5 containers.\n"
            "2. In a large skillet, brown the ground beef, bell peppers, and diced onion until fully cooked.\n"
            "3. Drain any excess fat. Stir in the taco seasoning and 1/2 cup of water, simmering for 2 minutes.\n"
            "4. Stir in the sweet corn and cook for another 2 minutes until warmed through.\n"
            "5. Divide the beef/veggie mixture over the rice.\n"
            "6. Top each serving with a sprinkle of cheese."
        )
    },
    {
        "name": "🍗 Jalapeno Popper Chicken & Air Fried Potatoes",
        "macros": {"Calories": 610, "Protein": "54g", "Carbs": "36g", "Fat": "26g"},
        "ingredients": [
            "2.5 lbs Boneless Skinless Chicken Breast",
            "8 slices Regular Bacon, cooked and crumbled",
            "4 oz Light Cream Cheese, softened",
            "1/4 cup Greek Yogurt",
            "1/2 cup canned diced jalapenos",
            "2 lbs Russet Potatoes, cubed",
            "Olive oil, salt, pepper"
        ],
        "instructions": (
            "1. Toss the cubed potatoes in olive oil, salt, and pepper. Air fry at 400°F (200°C) for 15-20 minutes until crispy and fork-tender. Divide into 5 containers.\n"
            "2. Mix the softened cream cheese, Greek yogurt, diced jalapenos, and crumbled bacon in a bowl.\n"
            "3. Place chicken breasts in a baking dish. Spread the cream cheese mixture evenly over each breast.\n"
            "4. Bake at 375°F (190°C) for 25-30 minutes until chicken reaches 165°F.\n"
            "5. Slice the chicken and serve alongside the air-fried potatoes."
        )
    }
]

# --- STREAMLIT UI SETUP ---
st.set_page_config(page_title="Weekly Meal Prep", page_icon="🍱", layout="centered")

st.title("🍽️ High-Protein Meal Prep Generator")

# --- SIDEBAR: BACKUP / MANUAL SELECTOR ---
st.sidebar.header("📁 Browse All Recipes")
st.sidebar.write("If you closed the app or want to pull up a specific meal manually, find it here:")

# Create a list of names for the dropdown list
recipe_names = [r["name"] for r in RECIPES]
selected_recipe_name = st.sidebar.selectbox("Choose a recipe directly:", ["-- Select to view manually --"] + recipe_names)

# --- MAIN PAGE BUTTON ---
st.write("Or let the app roll the dice for you:")
if st.button("🎲 Choose My Meal Prep", type="primary", use_container_width=True):
    # Select random, save to session state, reset the sidebar selector
    st.session_state['current_recipe'] = random.choice(RECIPES)
    if 'manual_selection' in st.session_state:
        del st.session_state['manual_selection']

# Determine which recipe to display based on user actions
display_recipe = None

if selected_recipe_name != "-- Select to view manually --":
    # User picked something from the sidebar menu
    display_recipe = next(r for r in RECIPES if r["name"] == selected_recipe_name)
elif 'current_recipe' in st.session_state:
    # User clicked the random button
    display_recipe = st.session_state['current_recipe']

# --- DISPLAY LOGIC ---
if display_recipe:
    st.divider()
    st.header(f"🏆 {display_recipe['name']}")
    
    # Nutritional Information Display Boxes
    st.subheader("📊 Nutritional Info (Per Serving)")
    m_col1, m_col2, m_col3, m_col4 = st.columns(4)
    with m_col1:
        st.metric(label="Calories", value=display_recipe["macros"]["Calories"])
    with m_col2:
        st.metric(label="Protein", value=display_recipe["macros"]["Protein"])
    with m_col3:
        st.metric(label="Carbs", value=display_recipe["macros"]["Carbs"])
    with m_col4:
        st.metric(label="Fat", value=display_recipe["macros"]["Fat"])
        
    st.divider()
    
    col1, col2 = st.columns([1, 1.4])
    
    with col1:
        st.subheader("🛒 Ingredients")
        st.caption("Yields 5 servings")
        for item in display_recipe["ingredients"]:
            st.markdown(f"- {item}")
            
    with col2:
        st.subheader("🧑‍🍳 Instructions")
        formatted_instructions = display_recipe["instructions"].replace("\n", "\n\n")
        st.markdown(formatted_instructions)