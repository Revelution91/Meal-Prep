import streamlit as st
import random

# --- RECIPE DATABASE ---
RECIPES = [
    {
        "name": "🍗 Healthy Chicken Bacon Ranch Bowls",
        "ingredients": [
            "2.5 lbs Boneless Skinless Chicken Breast, cubed",
            "10 slices Turkey Bacon (or center-cut pork bacon)",
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
        "name": "🥙 Cava-Inspired Mediterranean Bowls",
        "ingredients": [
            "2.5 lbs Boneless Skinless Chicken Thighs",
            "3 tbsp Harissa paste",
            "2.5 cups Brown Rice (dry measure)",
            "1 large English Cucumber, diced",
            "2 cups Cherry Tomatoes, halved",
            "1 Red Onion, finely diced",
            "1/2 cup Feta cheese, crumbled",
            "1/2 cup Tzatziki sauce"
        ],
        "instructions": (
            "1. Marinate chicken thighs in harissa paste, a splash of olive oil, salt, and pepper for 30 mins.\n"
            "2. Grill or bake chicken at 400°F (200°C) for 20-25 minutes. Let rest, then chop.\n"
            "3. Make the salad topping: Mix cucumber, tomatoes, and red onion with a squeeze of lemon juice.\n"
            "4. Cook the rice and divide among 5 containers.\n"
            "5. Add rice, harissa chicken, and the cucumber-tomato salad to containers.\n"
            "6. Keep tzatziki separate. Sprinkle bowls with feta cheese."
        )
    },
    {
        "name": "🍔 High-Protein Big Mac Casserole",
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
        "name": "🐔 BBQ Chicken & Roasted Carrots",
        "ingredients": [
            "2.5 lbs Boneless Skinless Chicken Breast",
            "1 cup Sugar-Free BBQ Sauce",
            "2 lbs Baby Potatoes, halved",
            "1 lb Baby Carrots",
            "1 tbsp Smoked paprika, garlic powder, salt, pepper",
            "2 tbsp Olive oil"
        ],
        "instructions": (
            "1. Toss potatoes and carrots in olive oil, salt, and pepper. You can roast these at 400°F (200°C) for 30 mins OR Air fry them in batches for 15-18 mins.\n"
            "2. Season chicken breasts with smoked paprika and garlic powder.\n"
            "3. Cook chicken in a skillet or bake until internal temp hits 165°F.\n"
            "4. Shred or chop the cooked chicken and toss it heavily in the BBQ sauce.\n"
            "5. Assemble containers: BBQ chicken alongside the roasted/air-fried potatoes and carrots."
        )
    },
    {
        "name": "🥩 Classic Beef & Broccoli",
        "ingredients": [
            "2.5 lbs Flank Steak, sliced very thin against the grain",
            "6 cups Broccoli florets",
            "2.5 cups Jasmine Rice (dry measure)",
            "1/2 cup Low-sodium Soy Sauce",
            "2 tbsp Sesame oil",
            "2 tbsp Cornstarch",
            "3 cloves Garlic, minced",
            "1 tbsp Ginger, minced"
        ],
        "instructions": (
            "1. Cook the rice and divide into 5 containers.\n"
            "2. Toss the thinly sliced steak in cornstarch and 1 tbsp soy sauce. Let sit 10 mins.\n"
            "3. Whisk remaining soy sauce, sesame oil, garlic, and ginger to make the sauce.\n"
            "4. Heat a wok or large skillet over high heat. Sear the steak in batches until browned. Remove and set aside.\n"
            "5. In the same pan, stir-fry the broccoli with a splash of water until tender-crisp.\n"
            "6. Return steak to the pan, pour the sauce over everything, and toss for 1-2 mins until thickened. Serve over rice."
        )
    },
    {
        "name": "🦃 Southwest Ground Turkey Skillet",
        "ingredients": [
            "2.5 lbs Lean Ground Turkey",
            "2 Bell Peppers, diced",
            "1 large Yellow Onion, diced",
            "1 cup Sweet Corn (frozen or canned)",
            "2.5 cups Rice (dry measure)",
            "1 packet Taco Seasoning",
            "1 cup Shredded Monterey Jack cheese"
        ],
        "instructions": (
            "1. Cook the rice and distribute into 5 containers.\n"
            "2. In a large skillet, brown the ground turkey, bell peppers, and diced onion until turkey is cooked.\n"
            "3. Drain any excess water/fat. Stir in the taco seasoning and 1/2 cup of water, simmering for 2 minutes.\n"
            "4. Stir in the sweet corn and cook for another 2 minutes until warmed through.\n"
            "5. Divide the turkey/veggie mixture over the rice.\n"
            "6. Top each serving with a sprinkle of cheese."
        )
    },
    {
        "name": "🍅 Creamy Tomato & Spinach Chicken Pasta",
        "ingredients": [
            "2.5 lbs Boneless Skinless Chicken Breast, cubed",
            "16 oz Protein Pasta (like Banza or Barilla Protein+)",
            "3 cups Fresh Baby Spinach",
            "1 jar (24 oz) Marinara Sauce",
            "1/2 cup Plain Greek Yogurt",
            "2 tbsp Olive oil",
            "Garlic powder, Italian seasoning, salt, pepper"
        ],
        "instructions": (
            "1. Boil the protein pasta in salted water according to package directions. Drain and divide into 5 containers.\n"
            "2. Heat olive oil in a large skillet. Cook the cubed chicken until browned and cooked through.\n"
            "3. Pour in the marinara sauce and season with Italian herbs. Simmer for 5 mins.\n"
            "4. Stir in the fresh spinach and let it wilt (about 2 mins).\n"
            "5. Turn off the heat. Stir in the Greek yogurt until the sauce becomes creamy (do not boil).\n"
            "6. Pour the creamy tomato spinach chicken over the pasta in each container."
        )
    },
    {
        "name": "🍗 Jalapeno Popper Chicken & Air Fried Potatoes",
        "ingredients": [
            "2.5 lbs Boneless Skinless Chicken Breast",
            "8 slices Turkey Bacon, cooked and crumbled",
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
    },
    {
        "name": "🥩 Steak Salad Bowls with Carrots & Cucumber",
        "ingredients": [
            "2.5 lbs Sirloin Steak",
            "1 large English Cucumber, sliced",
            "1 cup Shredded Carrots",
            "1 large bag Mixed Greens or Spinach",
            "1 cup Feta or Blue cheese, crumbled",
            "1/2 cup Balsamic Vinaigrette dressing",
            "Salt, pepper, garlic powder"
        ],
        "instructions": (
            "1. Season the sirloin steak heavily with salt, pepper, and garlic powder.\n"
            "2. Grill or pan-sear the steak (about 4-5 mins per side for medium-rare). Let rest 10 mins.\n"
            "3. Slice the steak thinly against the grain.\n"
            "4. In 5 large containers, build the salad base: Mixed greens, cucumber slices, and shredded carrots.\n"
            "5. Top with the sliced steak and crumbled cheese.\n"
            "6. Keep the balsamic vinaigrette in separate small cups until you're ready to eat."
        )
    },
    {
        "name": "🐔 Slow Cooker Salsa Chicken & Cauliflower Rice",
        "ingredients": [
            "2.5 lbs Boneless Skinless Chicken Breast",
            "1 jar (16 oz) Chunky Tomato Salsa",
            "2 Bell Peppers, sliced",
            "1 Yellow Onion, sliced",
            "2 bags (12 oz each) Frozen Cauliflower Rice",
            "1 cup Sweet Corn (frozen or canned)",
            "1 tbsp Cumin and Chili powder"
        ],
        "instructions": (
            "1. In a slow cooker, combine the chicken breasts, salsa, cumin, and chili powder. Cook on low for 4 hours.\n"
            "2. Shred the chicken directly in the salsa juices.\n"
            "3. In a large skillet, sauté the sliced bell peppers and onions until soft.\n"
            "4. Microwave or sauté the cauliflower rice according to package directions. Mix in the sweet corn.\n"
            "5. Divide the cauliflower rice and corn into 5 containers.\n"
            "6. Top with the sautéed peppers, onions, and shredded salsa chicken."
        )
    },
    {
        "name": "🥩 Garlic Butter Steak Bites & Zucchini",
        "ingredients": [
            "2.5 lbs Sirloin or Strip Steak, cut into 1-inch cubes",
            "3 medium Zucchini, sliced into half-moons",
            "2.5 cups Rice or Orzo (dry measure)",
            "3 tbsp Butter",
            "4 cloves Garlic, minced",
            "1 tbsp Fresh parsley, chopped",
            "Salt, pepper, and olive oil"
        ],
        "instructions": (
            "1. Cook the rice/orzo and divide into 5 containers.\n"
            "2. Season the steak cubes generously with salt and pepper.\n"
            "3. Heat a skillet over high heat. Sear steak bites in batches for 1-2 mins per side to get a crust. Remove from pan.\n"
            "4. In the same pan, add a drizzle of olive oil and sauté the zucchini until tender (about 4-5 mins). Remove from pan.\n"
            "5. Lower heat to medium. Add butter and minced garlic to the pan. Cook 1 min until fragrant.\n"
            "6. Return the steak and zucchini to the pan for 30 seconds just to coat in the garlic butter. Divide over the rice."
        )
    },
    {
        "name": "🐔 Lemon Herb Chicken & Roasted Veggies",
        "ingredients": [
            "2.5 lbs Boneless Skinless Chicken Breast",
            "2 medium Zucchini, chopped",
            "2 Bell Peppers, chopped",
            "1 Red Onion, cut into chunks",
            "2.5 cups Rice or Couscous (dry measure)",
            "Juice of 2 Lemons",
            "2 tbsp Olive oil",
            "1 tbsp Dried Oregano, salt, pepper"
        ],
        "instructions": (
            "1. Cook the carb base (rice or couscous) and divide into 5 containers.\n"
            "2. Preheat oven to 400°F (200°C).\n"
            "3. On a large sheet pan, spread out the chicken breasts, zucchini, bell peppers, and red onion.\n"
            "4. Whisk olive oil, lemon juice, oregano, salt, and pepper. Pour over the chicken and vegetables, tossing to coat evenly.\n"
            "5. Roast for 20-25 minutes until chicken is cooked through (165°F) and veggies are tender.\n"
            "6. Slice the chicken and divide everything evenly into the 5 meal prep containers."
        )
    }
]

# --- STREAMLIT UI ---
st.set_page_config(page_title="Weekly Meal Prep", page_icon="🍱", layout="centered")

st.title("🍽️ What are we prepping this week?")
st.write("Click the button below to randomly select your high-protein meal prep for the next 5 days.")

# The Generate Button
if st.button("🎲 Choose My Meal Prep", type="primary", use_container_width=True):
    # Pick a random recipe
    recipe = random.choice(RECIPES)
    
    # Store it in session state so it doesn't disappear if you click something else
    st.session_state['current_recipe'] = recipe

# Display the recipe if one is saved in the session state
if 'current_recipe' in st.session_state:
    recipe = st.session_state['current_recipe']
    
    st.divider()
    st.header(f"🏆 {recipe['name']}")
    
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        st.subheader("🛒 Ingredients")
        st.caption("Yields 5 servings")
        for item in recipe["ingredients"]:
            st.markdown(f"- {item}")
            
    with col2:
        st.subheader("🧑‍🍳 Instructions")
        # Replace newlines with double newlines so Markdown renders the list correctly
        formatted_instructions = recipe["instructions"].replace("\n", "\n\n")
        st.markdown(formatted_instructions)