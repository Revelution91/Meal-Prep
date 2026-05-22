import streamlit as st
import random

# --- RECIPE DATABASE (22 Recipes) ---
# Constraints Applied: NO Beans, NO Asparagus, NO Sweet Potatoes, NO Brown Rice, NO Turkey
RECIPES = [
    {
        "name": "🍗 Healthy Chicken Bacon Ranch Bowls",
        "macros": {"Calories": 610, "Protein": "52g", "Carbs": "45g", "Fat": "24g"},
        "ingredients": [
            "2.5 lbs Boneless Skinless Chicken Breast, cubed",
            "10 slices Regular Bacon (pork bacon)",
            "5 cups Broccoli florets",
            "2.5 cups White Rice or Jasmine Rice (dry measure)",
            "1 cup Greek Yogurt Ranch Dressing",
            "2 tbsp Olive oil",
            "Salt, pepper, garlic powder, and onion powder"
        ],
        "instructions": (
            "1. Cook the white rice according to package instructions. Divide evenly into 5 containers.\n"
            "2. Preheat oven to 400°F (200°C). Toss broccoli with 1 tbsp olive oil, salt, and pepper. Roast for 15-20 minutes.\n"
            "3. In a large skillet, cook the chopped bacon until crisp. Remove and set aside.\n"
            "4. In the same skillet, cook the cubed chicken seasoned with garlic and onion powder until cooked through (165°F).\n"
            "5. Assemble: Add chicken, broccoli, and bacon to the rice bowls.\n"
            "6. Top each bowl with ~3 tbsp of Greek yogurt ranch just before eating."
        )
    },
    {
        "name": "🔥 Buffalo Chicken & Roasted Potato Prep",
        "macros": {"Calories": 540, "Protein": "48g", "Carbs": "42g", "Fat": "18g"},
        "ingredients": [
            "2.5 lbs Boneless Skinless Chicken Breast",
            "3 large Russet or Gold Potatoes, cubed",
            "2 Bell Peppers, roughly chopped",
            "1 Red Onion, roughly chopped",
            "1 cup Frank's RedHot Buffalo Sauce",
            "2 tbsp Butter or Ghee (melted)",
            "2 tbsp Olive oil"
        ],
        "instructions": (
            "1. Preheat oven to 425°F (220°C) or use your Air Fryer at 400°F (200°C).\n"
            "2. Toss cubed potatoes, bell peppers, and red onion in olive oil, salt, and pepper. Roast or air fry for 20-25 mins until crispy.\n"
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
        "name": "🍔 Big Mac Bowls",
        "macros": {"Calories": 680, "Protein": "50g", "Carbs": "12g", "Fat": "48g"},
        "ingredients": [
            "2.5 lbs Lean Ground Beef (93/7)",
            "1 large head Iceberg Lettuce, shredded",
            "1 large White Onion, finely diced",
            "1 cup Dill Pickles, diced",
            "1.5 cups Reduced-fat Cheddar Cheese, shredded",
            "Salt, pepper, and garlic powder (for the beef)",
            "-- AUTHENTIC MAC SAUCE --",
            "2/3 Cup Mayonnaise",
            "1/3 Cup Sweet Pickle Relish",
            "2 tsp Yellow Mustard",
            "3/4 tsp White Vinegar",
            "1/2 tsp Paprika",
            "1/4 tsp Garlic powder",
            "1/4 tsp Onion powder"
        ],
        "instructions": (
            "1. In a large skillet over medium-high heat, brown the ground beef. Drain any excess fat and season generously with salt, pepper, and garlic powder.\n"
            "2. Divide the cooked ground beef evenly into 5 containers. Top the warm beef with shredded cheddar cheese so it slightly melts.\n"
            "3. Make the Mac Sauce: In a small bowl, whisk together the mayonnaise, sweet pickle relish, yellow mustard, white vinegar, paprika, garlic powder, and onion powder. Divide into 5 small condiment cups.\n"
            "4. Store the shredded lettuce, diced white onion, and diced pickles in separate baggies or compartmentalized containers to keep them crisp in the fridge.\n"
            "5. To serve, reheat the beef and cheese, then top with the fresh cold veggies and drizzle heavily with the Mac Sauce."
        )
    },
    {
        "name": "🥩 Fajita Steak Bowls with Jalapeno Garlic Aioli",
        "macros": {"Calories": 910, "Protein": "48g", "Carbs": "41g", "Fat": "62g"},
        "ingredients": [
            "2.5 lbs Skirt Steak or Flank Steak, sliced into strips",
            "3 Bell Peppers (assorted colors), sliced",
            "2 Yellow Onions, sliced",
            "2 lbs Russet or Gold Potatoes, diced into small cubes",
            "2 tbsp Fajita Seasoning",
            "1/2 cup Pico de Gallo",
            "Olive oil",
            "-- JALAPENO GARLIC AIOLI --",
            "2 Jalapenos",
            "1 Garlic Clove",
            "1 cup Mayonnaise",
            "1 tsp Honey",
            "1 tsp Salt"
        ],
        "instructions": (
            "1. Toss diced potatoes in olive oil and 1 tbsp of fajita seasoning. Air fry at 400°F (200°C) for 15-20 minutes, shaking the basket halfway, until crispy.\n"
            "2. Toss steak strips, bell peppers, and onions with remaining fajita seasoning and a drizzle of oil.\n"
            "3. Heat a large skillet over high heat. Cook steak and veggies in batches so they sear, not steam.\n"
            "4. Divide the air-fried potatoes into 5 containers as your base, topping with steak, veggies, and pico de gallo.\n"
            "5. Make the Aioli: Add the jalapenos, garlic clove, mayonnaise, honey, and salt to a blender. Blend until perfectly smooth.\n"
            "6. Drizzle the jalapeno garlic aioli heavily over each bowl, or portion into 5 small cups for serving."
        )
    },
    {
        "name": "🍔 Southwest Ground Beef Skillet with Jalapeno Aioli",
        "macros": {"Calories": 880, "Protein": "45g", "Carbs": "45g", "Fat": "58g"},
        "ingredients": [
            "2.5 lbs Lean Ground Beef (93/7)",
            "2 Bell Peppers, diced",
            "1 large Yellow Onion, diced",
            "1 cup Sweet Corn (frozen or canned)",
            "2.5 cups White Rice (dry measure)",
            "1 packet Taco Seasoning",
            "1 cup Shredded Monterey Jack cheese",
            "-- JALAPENO GARLIC AIOLI --",
            "2 Jalapenos",
            "1 Garlic Clove",
            "1 cup Mayonnaise",
            "1 tsp Honey",
            "1 tsp Salt"
        ],
        "instructions": (
            "1. Cook the white rice and distribute into 5 containers.\n"
            "2. In a large skillet, brown the ground beef, bell peppers, and diced onion until fully cooked.\n"
            "3. Drain any excess fat. Stir in the taco seasoning and 1/2 cup of water, simmering for 2 minutes.\n"
            "4. Stir in the sweet corn and cook for another 2 minutes until warmed through.\n"
            "5. Divide the beef/veggie mixture over the rice and top with cheese.\n"
            "6. Make the Aioli: Add the jalapenos, garlic clove, mayonnaise, honey, and salt to a blender. Blend until smooth.\n"
            "7. Drizzle the aioli over the bowls just before eating."
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
    },
    {
        "name": "🥙 Cava-Inspired Mediterranean Bowls",
        "macros": {"Calories": 580, "Protein": "42g", "Carbs": "45g", "Fat": "24g"},
        "ingredients": [
            "2.5 lbs Boneless Skinless Chicken Thighs",
            "3 tbsp Harissa paste",
            "2.5 cups White Rice (dry measure)",
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
            "4. Cook the white rice and divide among 5 containers.\n"
            "5. Add rice, harissa chicken, and the cucumber-tomato salad to containers.\n"
            "6. Keep tzatziki separate. Sprinkle bowls with feta cheese."
        )
    },
    {
        "name": "🐔 BBQ Chicken & Roasted Carrots & Potatoes",
        "macros": {"Calories": 520, "Protein": "50g", "Carbs": "55g", "Fat": "10g"},
        "ingredients": [
            "2.5 lbs Boneless Skinless Chicken Breast",
            "1 cup Sugar-Free BBQ Sauce",
            "2 lbs Baby Gold Potatoes, halved",
            "1 lb Baby Carrots",
            "1 tbsp Smoked paprika, garlic powder, salt, pepper",
            "2 tbsp Olive oil"
        ],
        "instructions": (
            "1. Toss potatoes and carrots in olive oil, salt, and pepper. Air fry in batches for 15-18 mins, OR roast at 400°F (200°C) for 30 mins.\n"
            "2. Season chicken breasts with smoked paprika and garlic powder.\n"
            "3. Cook chicken in a skillet or bake until internal temp hits 165°F.\n"
            "4. Shred or chop the cooked chicken and toss it heavily in the BBQ sauce.\n"
            "5. Assemble containers: BBQ chicken alongside the roasted/air-fried potatoes and carrots."
        )
    },
    {
        "name": "🥩 Classic Beef & Broccoli",
        "macros": {"Calories": 590, "Protein": "48g", "Carbs": "52g", "Fat": "18g"},
        "ingredients": [
            "2.5 lbs Flank Steak, sliced very thin against the grain",
            "6 cups Broccoli florets",
            "2.5 cups Jasmine Rice or White Rice (dry measure)",
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
        "name": "🍅 Creamy Tomato & Spinach Chicken Pasta",
        "macros": {"Calories": 560, "Protein": "55g", "Carbs": "50g", "Fat": "14g"},
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
        "name": "🥩 Steak Salad Bowls with Carrots & Cucumber",
        "macros": {"Calories": 510, "Protein": "45g", "Carbs": "15g", "Fat": "28g"},
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
        "name": "🐔 Slow Cooker Salsa Chicken with Jalapeno Aioli",
        "macros": {"Calories": 710, "Protein": "48g", "Carbs": "36g", "Fat": "40g"},
        "ingredients": [
            "2.5 lbs Boneless Skinless Chicken Breast",
            "1 jar (16 oz) Chunky Tomato Salsa",
            "2 Bell Peppers, sliced",
            "1 Yellow Onion, sliced",
            "2 bags (12 oz each) Frozen Cauliflower Rice",
            "1 cup Sweet Corn (frozen or canned)",
            "1 tbsp Cumin and Chili powder",
            "-- JALAPENO GARLIC AIOLI --",
            "2 Jalapenos",
            "1 Garlic Clove",
            "1 cup Mayonnaise",
            "1 tsp Honey",
            "1 tsp Salt"
        ],
        "instructions": (
            "1. In a slow cooker, combine the chicken breasts, salsa, cumin, and chili powder. Cook on low for 4 hours.\n"
            "2. Shred the chicken directly in the salsa juices.\n"
            "3. In a large skillet, sauté the sliced bell peppers and onions until soft.\n"
            "4. Microwave or sauté the cauliflower rice according to package directions. Mix in the sweet corn.\n"
            "5. Divide the cauliflower rice and corn into 5 containers. Top with the sautéed peppers, onions, and shredded salsa chicken.\n"
            "6. Make the Aioli: Blend the jalapenos, garlic clove, mayonnaise, honey, and salt until smooth.\n"
            "7. Top each bowl with the aioli, or store in small side cups."
        )
    },
    {
        "name": "🥩 Garlic Butter Steak Bites & Zucchini",
        "macros": {"Calories": 610, "Protein": "45g", "Carbs": "45g", "Fat": "25g"},
        "ingredients": [
            "2.5 lbs Sirloin or Strip Steak, cut into 1-inch cubes",
            "3 medium Zucchini, sliced into half-moons",
            "2.5 cups White Rice or Orzo (dry measure)",
            "3 tbsp Butter",
            "4 cloves Garlic, minced",
            "1 tbsp Fresh parsley, chopped",
            "Salt, pepper, and olive oil"
        ],
        "instructions": (
            "1. Cook the white rice/orzo and divide into 5 containers.\n"
            "2. Season the steak cubes generously with salt and pepper.\n"
            "3. Heat a skillet over high heat. Sear steak bites in batches for 1-2 mins per side to get a crust. Remove from pan.\n"
            "4. In the same pan, add a drizzle of olive oil and sauté the zucchini until tender (about 4-5 mins). Remove from pan.\n"
            "5. Lower heat to medium. Add butter and minced garlic to the pan. Cook 1 min until fragrant.\n"
            "6. Return the steak and zucchini to the pan for 30 seconds just to coat in the garlic butter. Divide over the rice."
        )
    },
    {
        "name": "🐔 Lemon Herb Chicken & Roasted Veggies",
        "macros": {"Calories": 490, "Protein": "48g", "Carbs": "40g", "Fat": "15g"},
        "ingredients": [
            "2.5 lbs Boneless Skinless Chicken Breast",
            "2 medium Zucchini, chopped",
            "2 Bell Peppers, chopped",
            "1 Red Onion, cut into chunks",
            "2.5 cups White Rice or Couscous (dry measure)",
            "Juice of 2 Lemons",
            "2 tbsp Olive oil",
            "1 tbsp Dried Oregano, salt, pepper"
        ],
        "instructions": (
            "1. Cook the carb base (white rice or couscous) and divide into 5 containers.\n"
            "2. Preheat oven to 400°F (200°C).\n"
            "3. On a large sheet pan, spread out the chicken breasts, zucchini, bell peppers, and red onion.\n"
            "4. Whisk olive oil, lemon juice, oregano, salt, and pepper. Pour over the chicken and vegetables, tossing to coat evenly.\n"
            "5. Roast for 20-25 minutes until chicken is cooked through (165°F) and veggies are tender.\n"
            "6. Slice the chicken and divide everything evenly into the 5 meal prep containers."
        )
    },
    {
        "name": "🥓 Chicken Club Egg White Wraps",
        "macros": {"Calories": 420, "Protein": "48g", "Carbs": "8g", "Fat": "22g"},
        "ingredients": [
            "2.5 lbs Boneless Skinless Chicken Breast (cooked and sliced)",
            "10 Large Egg White Wraps (e.g., Egglife)",
            "10 slices Regular Bacon (pork bacon), cooked and halved",
            "2 cups Shredded Iceberg or Romaine Lettuce",
            "2 Roma Tomatoes, thinly sliced",
            "1/2 cup Greek Yogurt Ranch or Light Mayo"
        ],
        "instructions": (
            "1. Cook chicken in a skillet or bake until internal temp reaches 165°F, then slice thinly.\n"
            "2. Cook bacon until crispy and cut slices in half.\n"
            "3. Assemble 5 meal prep containers: Place 2 egg white wraps in each.\n"
            "4. Divide the sliced chicken, bacon halves, lettuce, and tomatoes evenly into the containers (you can keep the veggies in a separate baggies if you prefer to keep the wraps dry).\n"
            "5. Keep the dressing in 5 separate small containers. Assemble the wraps right before eating."
        )
    },
    {
        "name": "🥪 Italian Grinder Chicken Salad Wraps",
        "macros": {"Calories": 480, "Protein": "45g", "Carbs": "28g", "Fat": "20g"},
        "ingredients": [
            "2.5 lbs Boneless Skinless Chicken Breast (cooked and shredded)",
            "5 Large Flour Tortillas or Wraps",
            "3 cups Shredded Iceberg Lettuce",
            "1/2 Red Onion, very thinly sliced",
            "1/4 cup Sliced Pepperoncini or Banana Peppers",
            "1/2 cup Light Mayo",
            "2 tbsp Red Wine Vinegar",
            "1/4 cup Grated Parmesan Cheese",
            "1 tsp Dried Oregano, salt, and pepper"
        ],
        "instructions": (
            "1. Cook the chicken breasts (boil, bake, or slow-cook) and shred thoroughly with two forks.\n"
            "2. In a large bowl, whisk together the light mayo, red wine vinegar, parmesan cheese, oregano, salt, and pepper to create the grinder dressing.\n"
            "3. Toss the shredded chicken, shredded lettuce, red onion, and pepperoncini directly into the dressing until well coated.\n"
            "4. Divide the chicken grinder salad evenly among the 5 tortillas and roll them up tightly like burritos.\n"
            "5. Wrap each in foil or parchment paper and store in the fridge."
        )
    },
    {
        "name": "🥜 Easy Peanut Chicken Protein Bowls",
        "macros": {"Calories": 560, "Protein": "48g", "Carbs": "45g", "Fat": "21g"},
        "ingredients": [
            "2.5 lbs Boneless Skinless Chicken Breast, cubed",
            "2.5 cups White Rice (dry measure)",
            "4 cups Broccoli florets",
            "1/2 cup Creamy Peanut Butter (unsweetened)",
            "1/4 cup Low-sodium Soy Sauce",
            "2 tbsp Lime juice",
            "1 tbsp Fresh Ginger, minced",
            "1 tbsp Sriracha (optional, for heat)",
            "1/4 cup Warm water (to thin sauce)"
        ],
        "instructions": (
            "1. Cook the white rice according to package instructions. Divide into 5 containers.\n"
            "2. Steam or roast the broccoli florets until tender-crisp. Divide into the containers.\n"
            "3. Cook the cubed chicken in a large skillet over medium-high heat until cooked through (165°F).\n"
            "4. While chicken cooks, whisk peanut butter, soy sauce, lime juice, ginger, Sriracha, and warm water in a bowl until smooth.\n"
            "5. Toss the cooked chicken in the peanut sauce until fully coated.\n"
            "6. Add the saucy peanut chicken to the rice and broccoli bowls."
        )
    },
    {
        "name": "🍗 BBQ Chicken Power Bowls",
        "macros": {"Calories": 540, "Protein": "48g", "Carbs": "55g", "Fat": "14g"},
        "ingredients": [
            "2.5 lbs Boneless Skinless Chicken Breast",
            "1 cup Sugar-Free BBQ Sauce",
            "2.5 cups White Rice (dry measure)",
            "2 cups Sweet Corn (frozen or canned)",
            "1 Red Onion, diced",
            "1 Bell Pepper, diced",
            "1 tbsp Olive oil"
        ],
        "instructions": (
            "1. Cook the white rice according to package instructions. Divide into 5 containers.\n"
            "2. Heat olive oil in a skillet and sauté the diced red onion, bell pepper, and sweet corn until lightly charred. Divide among the bowls.\n"
            "3. Cook the chicken breasts in a skillet or bake until internal temp reaches 165°F.\n"
            "4. Shred or dice the cooked chicken and toss heavily in the sugar-free BBQ sauce.\n"
            "5. Add the BBQ chicken to the meal prep containers over the rice and veggies."
        )
    },
    {
        "name": "🌯 Chicken Bacon Ranch Burritos",
        "macros": {"Calories": 620, "Protein": "46g", "Carbs": "48g", "Fat": "26g"},
        "ingredients": [
            "5 Large Burrito-Size Flour Tortillas",
            "2.5 lbs Boneless Skinless Chicken Breast (cooked and cubed)",
            "10 slices Regular Bacon (cooked and chopped)",
            "1.5 cups White Rice (dry measure)",
            "1 cup Shredded Cheddar or Monterey Jack cheese",
            "1/2 cup Greek Yogurt Ranch"
        ],
        "instructions": (
            "1. Cook the white rice and set aside.\n"
            "2. Cook the chicken and bacon. Chop both into bite-sized pieces.\n"
            "3. Lay out the 5 large tortillas. To each tortilla, add an equal scoop of white rice, chicken, chopped bacon, and shredded cheese.\n"
            "4. Drizzle about 1.5 tbsp of Greek yogurt ranch into each burrito.\n"
            "5. Roll the burritos tightly, tucking in the sides. Wrap in foil for easy grab-and-go storage.\n"
            "6. (Optional) Sear the folded burritos in a dry skillet for 1 minute per side to seal the seam before wrapping."
        )
    },
    {
        "name": "🌯 Buffalo Chicken Burritos",
        "macros": {"Calories": 580, "Protein": "44g", "Carbs": "50g", "Fat": "22g"},
        "ingredients": [
            "5 Large Burrito-Size Flour Tortillas",
            "2.5 lbs Boneless Skinless Chicken Breast",
            "1 cup Frank's RedHot Buffalo Sauce",
            "1.5 cups White Rice (dry measure)",
            "1 cup Shredded Mozzarella or Cheddar cheese",
            "1/4 cup Light Blue Cheese or Ranch dressing"
        ],
        "instructions": (
            "1. Cook the white rice and set aside.\n"
            "2. Cook the chicken (bake, boil, or skillet) and shred it completely.\n"
            "3. Toss the shredded chicken in the buffalo sauce until well coated.\n"
            "4. Lay out the 5 tortillas. Layer white rice, buffalo chicken, a sprinkle of cheese, and a small drizzle of dressing.\n"
            "5. Fold the sides in and roll tightly into a burrito. Wrap in foil.\n"
            "6. Warm in the microwave or air fryer (unwrapped) before eating."
        )
    },
    {
        "name": "🌯 Steak Fajita Burritos with Jalapeno Aioli",
        "macros": {"Calories": 930, "Protein": "48g", "Carbs": "49g", "Fat": "60g"},
        "ingredients": [
            "5 Large Burrito-Size Flour Tortillas",
            "2.5 lbs Skirt Steak or Flank Steak, sliced thin",
            "2 Bell Peppers, sliced into strips",
            "1 Yellow Onion, sliced into strips",
            "1.5 cups White Rice (dry measure)",
            "2 tbsp Fajita Seasoning",
            "1 cup Shredded Mexican Blend cheese",
            "Olive oil",
            "-- JALAPENO GARLIC AIOLI --",
            "2 Jalapenos",
            "1 Garlic Clove",
            "1 cup Mayonnaise",
            "1 tsp Honey",
            "1 tsp Salt"
        ],
        "instructions": (
            "1. Cook the white rice and set aside.\n"
            "2. Toss the sliced steak, peppers, and onions in a bowl with a drizzle of olive oil and the fajita seasoning.\n"
            "3. Heat a large skillet over high heat. Cook the steak and veggies in batches until the steak is browned and veggies are soft. Let slightly cool.\n"
            "4. Make the Aioli: Add the jalapenos, garlic clove, mayonnaise, honey, and salt to a blender. Blend until perfectly smooth.\n"
            "5. Assemble the 5 burritos: Layer white rice, steak and fajita veggies, shredded cheese, and a drizzle of the jalapeno aioli.\n"
            "6. Roll tightly and wrap in foil for storage. Toast the outside in a skillet when you reheat it for the best texture."
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