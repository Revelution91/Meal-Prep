import streamlit as st
import random
import re
from streamlit_local_storage import LocalStorage

# --- Import your recipes ---
from recipes import RECIPES

# --- 1. PERSISTENCE SETUP ---
localS = LocalStorage()

def load_data(key, default):
    data = localS.getItem(key)
    return data if data is not None else default

def save_data(key, data):
    localS.setItem(key, data)

# --- 2. EXTRACT TAGS FOR FILTERS ---
all_proteins = sorted(list(set(r.get("tags", {}).get("protein", "Uncategorized") for r in RECIPES)))
all_carbs = sorted(list(set(r.get("tags", {}).get("carb", "Uncategorized") for r in RECIPES)))
all_veggies = sorted(list(set(r.get("tags", {}).get("veggie", "Uncategorized") for r in RECIPES)))

# --- 3. STREAMLIT APP SETUP ---
st.set_page_config(page_title="Weekly Meal Prep", page_icon="🍱", layout="centered")
st.title("🍽️ High-Protein Meal Prep Generator")

# Initialize Session State
if 'favorites' not in st.session_state:
    st.session_state['favorites'] = load_data("meal_prep_favorites", [])
if 'meal_plan' not in st.session_state:
    st.session_state['meal_plan'] = load_data("meal_prep_plan", [])
if 'checked_items' not in st.session_state:
    st.session_state['checked_items'] = load_data("shopping_checked", {})

# View routing states
if 'random_recipe' not in st.session_state:
    st.session_state['random_recipe'] = None
if 'manual_recipe' not in st.session_state:
    st.session_state['manual_recipe'] = None
if 'fav_recipe' not in st.session_state:
    st.session_state['fav_recipe'] = None


# --- 4. CALLBACK FUNCTIONS (No more st.rerun!) ---
def add_to_favorites(recipe):
    st.session_state['favorites'] = st.session_state['favorites'] + [recipe]
    save_data("meal_prep_favorites", st.session_state['favorites'])

def remove_from_favorites(recipe_name):
    st.session_state['favorites'] = [r for r in st.session_state['favorites'] if r['name'] != recipe_name]
    save_data("meal_prep_favorites", st.session_state['favorites'])

def add_to_planner(recipe, slider_key):
    servings = st.session_state[slider_key]
    st.session_state['meal_plan'] = st.session_state['meal_plan'] + [{"recipe": recipe, "servings": servings}]
    save_data("meal_prep_plan", st.session_state['meal_plan'])

def remove_from_planner(index):
    # List slicing creates a new object, guaranteeing the state updates correctly
    plan = st.session_state['meal_plan']
    st.session_state['meal_plan'] = plan[:index] + plan[index+1:]
    save_data("meal_prep_plan", st.session_state['meal_plan'])

def update_checkbox(key):
    st.session_state['checked_items'][key] = st.session_state[key]
    save_data("shopping_checked", st.session_state['checked_items'])

def set_view_state(state_key, value):
    st.session_state[state_key] = value


# --- 5. HELPERS ---
def scale_ingredient(ingredient_str, target_servings, base_servings=5):
    """Scales numbers and smartly converts units (including pinches and dashes) for smaller servings."""
    
    # 1. Define what makes an ingredient "wet"
    wet_keywords = ["oil", "sauce", "juice", "dressing", "honey", "water", "broth", "cream", "milk", "vinegar", "paste"]
    is_wet = any(word in ingredient_str.lower() for word in wet_keywords)
    
    # 2. Define the culinary term for micro-measurements
    micro_measure = "A dash of" if is_wet else "A pinch of"

    # 3. Regex now looks for cup, lb, tbsp, and tsp
    pattern = r'^([0-9]*\.?[0-9]+)(?:/([0-9]+))?\s*(cup|cups|lb|lbs|tbsp|tsp)?'

    def replacer(match):
        numerator = float(match.group(1))
        denominator = float(match.group(2)) if match.group(2) else 1.0
        unit = match.group(3)

        # Calculate base scaled value
        val = numerator / denominator
        new_val = (val / base_servings) * target_servings

        # 4. UNIT CONVERSION LOGIC
        if unit:
            unit = unit.lower()
            
            # --- CUP CONVERSIONS (Triggers if less than 1/4 cup) ---
            if "cup" in unit and new_val < 0.25:
                if is_wet:
                    oz_val = new_val * 8
                    return f"{round(oz_val, 1):g} oz"
                else:
                    tbsp_val = new_val * 16
                    if tbsp_val < 1:
                        tsp_val = tbsp_val * 3
                        if tsp_val <= 0.125:  # 1/8 tsp or less
                            return micro_measure
                        return f"{round(tsp_val, 1):g} tsp"
                    return f"{round(tbsp_val, 1):g} tbsp"

            # --- TABLESPOON CONVERSIONS (Triggers if less than 1 tbsp) ---
            elif "tbsp" in unit and new_val < 1:
                tsp_val = new_val * 3
                if tsp_val <= 0.125:  # 1/8 tsp or less
                    return micro_measure
                return f"{round(tsp_val, 1):g} tsp"

            # --- TEASPOON CONVERSIONS (Triggers if 1/8 tsp or less) ---
            elif "tsp" in unit and new_val <= 0.125:
                return micro_measure

            # --- POUND CONVERSIONS (Triggers if less than 0.5 lbs) ---
            elif "lb" in unit and new_val < 0.5:
                oz_val = new_val * 16
                return f"{round(oz_val, 1):g} oz"
            
            # If no conversion was triggered, put the original unit back
            return f"{round(new_val, 2):g} {unit}"

        # If there was no unit found in the regex match, just return the number
        return f"{round(new_val, 2):g}"

    return re.sub(pattern, replacer, ingredient_str, flags=re.IGNORECASE)

def render_recipe(recipe, tab_key):
    """Displays a recipe card with slider and action buttons."""
    st.divider()
    
    st.header(f"🏆 {recipe['name']}")

    # Macros Display
    m_col1, m_col2, m_col3, m_col4 = st.columns(4)
    m_col1.metric("Calories", recipe["macros"]["Calories"])
    m_col2.metric("Protein", recipe["macros"]["Protein"])
    m_col3.metric("Carbs", recipe["macros"]["Carbs"])
    m_col4.metric("Fat", recipe["macros"]["Fat"])
        
    st.divider()
    
    # Servings Slider
    slider_key = f"slider_{tab_key}_{recipe['name']}"
    servings = st.slider("Number of Servings", min_value=1, max_value=14, value=5, step=1, key=slider_key)
    
    col1, col2 = st.columns([1, 1.4])
    with col1:
        st.subheader("🛒 Ingredients")
        for item in recipe["ingredients"]:
            st.markdown(f"- {scale_ingredient(item, target_servings=servings)}")
    with col2:
        st.subheader("🧑‍🍳 Instructions")
        st.markdown(recipe["instructions"].replace("\n", "\n\n"))

    st.divider()

    # Action Buttons (Side-by-Side)
    c1, c2 = st.columns(2)
    with c1:
        is_saved = any(r['name'] == recipe['name'] for r in st.session_state['favorites'])
        if not is_saved:
            st.button("❤️ Save Recipe", 
                      key=f"save_{tab_key}_{recipe['name']}", 
                      on_click=add_to_favorites, 
                      args=(recipe,), 
                      use_container_width=True)
        else:
            st.button("✅ Saved", disabled=True, key=f"saved_{tab_key}_{recipe['name']}", use_container_width=True)
            
    with c2:
        st.button("➕ Add to Planner", 
                  key=f"plan_{tab_key}_{recipe['name']}", 
                  type="primary", 
                  on_click=add_to_planner, 
                  args=(recipe, slider_key), 
                  use_container_width=True)


# --- 6. STATEFUL NAVIGATION (Replaces st.tabs) ---
# We use a stateful radio button so Streamlit NEVER forgets which page you are on.
st.divider()
menu_options = ["🎲 Randomizer", "📖 Recipe Book", "⭐ Favorites", "🛒 Planner"]
current_page = st.radio("Navigation Menu", menu_options, horizontal=True, label_visibility="collapsed", key="active_page")
st.divider()

# PAGE 1: RANDOMIZER
if current_page == "🎲 Randomizer":
    st.write("Filter your preferences and let the app choose!")
    
    f_col1, f_col2, f_col3 = st.columns(3)
    with f_col1:
        sel_proteins = st.multiselect("Protein", all_proteins, placeholder="Any")
    with f_col2:
        sel_carbs = st.multiselect("Carb Base", all_carbs, placeholder="Any")
    with f_col3:
        sel_veggies = st.multiselect("Veggie", all_veggies, placeholder="Any")

    if st.button("🎲 Choose My Meal Prep", type="primary", use_container_width=True):
        filtered_recipes = [
            r for r in RECIPES 
            if (not sel_proteins or r.get("tags", {}).get("protein") in sel_proteins) and
               (not sel_carbs or r.get("tags", {}).get("carb") in sel_carbs) and
               (not sel_veggies or r.get("tags", {}).get("veggie") in sel_veggies)
        ]
        
        if filtered_recipes:
            st.session_state['random_recipe'] = random.choice(filtered_recipes)
        else:
            st.error("No recipes match those exact filters! Try removing a constraint.")
            st.session_state['random_recipe'] = None
            
    if st.session_state['random_recipe']:
        render_recipe(st.session_state['random_recipe'], "tab1")

# PAGE 2: RECIPE BOOK
elif current_page == "📖 Recipe Book":
    if st.session_state['manual_recipe']:
        st.button("⬅️ Back to Recipe Book", key="back_tab2", on_click=set_view_state, args=("manual_recipe", None))
        render_recipe(st.session_state['manual_recipe'], "tab2")
    else:
        st.write("Browse all available recipes below:")
        for i in range(0, len(RECIPES), 3):
            cols = st.columns(3)
            for j in range(3):
                if i + j < len(RECIPES):
                    recipe = RECIPES[i + j]
                    with cols[j]:
                        st.markdown(f"**{recipe['name']}**")
                        st.caption(f"{recipe['macros']['Calories']} Cal | {recipe['macros']['Protein']} Pro")
                        st.button("View", key=f"view_tab2_{recipe['name']}", on_click=set_view_state, args=("manual_recipe", recipe), use_container_width=True)

# PAGE 3: FAVORITES
elif current_page == "⭐ Favorites":
    if st.session_state['fav_recipe']:
        st.button("⬅️ Back to Favorites", key="back_tab3", on_click=set_view_state, args=("fav_recipe", None))
        render_recipe(st.session_state['fav_recipe'], "tab3")
    else:
        if not st.session_state['favorites']:
            st.info("You haven't saved any recipes yet! Click '❤️ Save Recipe' on any meal to add it here.")
        else:
            st.write("Your saved meals:")
            favs = st.session_state['favorites']
            for i in range(0, len(favs), 3):
                cols = st.columns(3)
                for j in range(3):
                    if i + j < len(favs):
                        recipe = favs[i + j]
                        with cols[j]:
                            st.markdown(f"**{recipe['name']}**")
                            st.caption(f"{recipe['macros']['Calories']} Cal | {recipe['macros']['Protein']} Pro")
                            
                            c1, c2 = st.columns(2)
                            with c1:
                                st.button("View", key=f"view_tab3_{recipe['name']}", on_click=set_view_state, args=("fav_recipe", recipe), use_container_width=True)
                            with c2:
                                st.button("Remove", key=f"remove_tab3_{recipe['name']}", on_click=remove_from_favorites, args=(recipe['name'],), use_container_width=True)

# PAGE 4: PLANNER & INTERACTIVE LIST
elif current_page == "🛒 Planner":
    st.header("🛒 Interactive Grocery List")
    if not st.session_state['meal_plan']:
        st.info("Add recipes to your planner to see your grocery list.")
    else:
        for idx, item in enumerate(st.session_state['meal_plan']):
            st.write(f"### {item['recipe']['name']} ({item['servings']} servings)")
            for ing in item['recipe']['ingredients']:
                scaled_ing = scale_ingredient(ing, item['servings'])
                
                # Unique key based on recipe index and ingredient text
                cb_key = f"cb_{idx}_{ing}"
                st.checkbox(scaled_ing, 
                            key=cb_key, 
                            value=st.session_state['checked_items'].get(cb_key, False),
                            on_change=update_checkbox,
                            args=(cb_key,))
            
            st.button("Remove from Planner", key=f"del_plan_{idx}", on_click=remove_from_planner, args=(idx,))
            st.divider()