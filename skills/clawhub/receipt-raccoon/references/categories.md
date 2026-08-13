# Category Keyword Reference

Full list of keywords used for automatic categorisation of receipt items.

## Categories

### groceries
**Keywords:** milk, bread, eggs, cheese, butter, yogurt, cream, chicken, beef, pork, bacon, turkey, fish, salmon, shrimp, rice, pasta, flour, sugar, oil, salt, pepper, spice, onion, garlic, potato, tomato, carrot, lettuce, spinach, broccoli, apple, banana, orange, lemon, lime, berry, avocado, cucumber, mushroom, corn, juice, water, cereal, oats, granola, jam, honey, peanut butter, nut, almond, tofu, lentil, bean, soup, sauce, ketchup, mustard, mayo, vinegar, soy, noodle, tortilla, bun, bagel, pita, cracker, cookie, chocolate, candy, chip, wine, beer, frozen, ice cream, deli, ham, sausage, organic, kale, zucchini, cauliflower, grape, melon, pineapple, mango, peach, pear, plum, cherry, coconut, and many more.

### dining
**Keywords:** burger, pizza, sandwich, taco, burrito, sushi, ramen, curry, fried rice, coffee, espresso, latte, cappuccino, tea, smoothie, beer, draft, cocktail, margarita, appetizer, wings, nachos, fries, brunch, breakfast, pancake, steak, lobster, dessert, cake, cheesecake, restaurant, cafe, diner, bistro, grill, takeout, delivery, gratuity, tip, and more.

### electronics
**Keywords:** cable, charger, usb, hdmi, adapter, battery, phone, laptop, tablet, monitor, keyboard, mouse, headphone, speaker, webcam, router, ssd, hard drive, memory, ram, gpu, motherboard, cpu, screen protector, phone case, smartwatch, camera, lens, power bank, surge protector, light bulb, smart plug.

### clothing
**Keywords:** shirt, t-shirt, blouse, pants, jeans, trouser, short, skirt, dress, suit, blazer, jacket, coat, sweater, hoodie, shoe, sneaker, boot, sandal, sock, underwear, hat, cap, glove, scarf, tie, belt, wallet, purse, backpack, watch, ring, necklace.

### health
**Keywords:** pharmacy, drug, medicine, medication, prescription, vitamin, supplement, aspirin, ibuprofen, acetaminophen, bandage, antiseptic, ointment, thermometer, toothbrush, toothpaste, floss, deodorant, shampoo, conditioner, soap, lotion, sunscreen, tissue, razor, contact lens, first aid.

### household
**Keywords:** detergent, fabric softener, bleach, dish soap, dishwasher, sponge, paper towel, toilet paper, napkin, trash bag, cleaning spray, mop, broom, vacuum, candle, air freshener, laundry, light bulb, aluminum foil, plastic wrap, container, plate, bowl, cup, fork, knife, pan, pot.

### transport
**Keywords:** gas, fuel, diesel, unleaded, uber, lyft, taxi, bus, train, metro, transit, parking, meter, toll, oil change, tire, brake, wiper, car wash, bike, flight, airline.

### entertainment
**Keywords:** movie, cinema, theater, concert, game, video game, steam, book, magazine, streaming, netflix, spotify, board game, museum, zoo, amusement, bowling, sport, lottery.

### office
**Keywords:** pen, pencil, marker, paper, notebook, binder, stapler, tape, glue, scissors, printer, ink, toner, envelope, stamp, desk, chair, calendar, planner, whiteboard.

### other
Fallback for items that don't match any category. Often includes miscellaneous items, services, or unrecognised products.

## Scoring

Items are scored by summing the character length of all matching keywords. Longer keyword matches contribute more weight, which helps disambiguate items that could belong to multiple categories (e.g. "WINE GLASS" in dining vs. "WINE" bottle in groceries).

## Adding Custom Categories

Edit `CATEGORIES` in `scripts/receipt_parser.py` to add new categories or keywords:

```python
CATEGORIES["pets"] = [
    "dog food", "cat food", "leash", "collar", "litter", "toy",
    "treat", "kibble", "aquarium", "fish food",
]
```
