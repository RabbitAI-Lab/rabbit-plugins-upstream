# Default Shelf Life & Category Detection

## How Categories Work

The tracker automatically categorizes items based on keyword matching against the item name. Each category has a default shelf life in days.

## Category → Shelf Life Table

| Category | Default Days | Keywords |
|----------|-------------|----------|
| Dairy | 7 | milk, yogurt, cheese, cream, butter, kefir, sour cream, cottage cheese |
| Meat | 3 | chicken, beef, pork, fish, turkey, bacon, sausage, ham, steak, ground, lamb, duck, shrimp, salmon |
| Produce-Leafy | 4 | spinach, lettuce, salad, kale, arugula, herbs, cilantro, parsley, basil, spring onion |
| Produce-Root | 14 | carrot, potato, onion, garlic, ginger, beet, turnip, radish, sweet potato, leek |
| Produce-Fruit | 7 | berry, banana, apple, orange, lemon, lime, grape, mango, pineapple, peach, plum, pear, avocado, tomato, strawberry, blueberry |
| Bakery | 5 | bread, bagel, tortilla, bun, roll, pastry, cake, muffin, croissant, pancake, naan, pita |
| Deli | 5 | cold cut, salami, prosciutto, ham slice, prepared salad, coleslaw, hummus, tzatziki |
| Eggs | 21 | egg |
| Condiments | 180 | sauce, dressing, ketchup, mustard, mayo, relish, chutney, jam, jelly |
| Tofu | 7 | tofu, tempeh, seitan |
| Other | 7 | (fallback for unrecognized items) |

## Real-World Shelf Life Notes

These are **conservative estimates** for fridge storage at 4°C:

### Dairy
- Milk: 7 days opened, 10+ days unopened
- Yogurt: 7-14 days (smell test is reliable)
- Hard cheese: 3-4 weeks (mold on surface is OK for hard cheeses, cut 1cm around)
- Soft cheese: 7-10 days
- Butter: 2-3 weeks in fridge, months in freezer

### Meat (refrigerated, not frozen)
- Chicken: 1-2 days raw, 3-4 days cooked
- Beef/Pork: 3-5 days raw
- Fish: 1-2 days raw
- Bacon: 7 days opened

### Produce
- Berries: 3-5 days (mold spreads fast — check daily)
- Bananas: 3-5 days on counter, freeze when ripe
- Leafy greens: 3-5 days (spinach goes fast, kale lasts longer)
- Root veg: 2-4 weeks (potatoes need dark+cool, not fridge)
- Tomatoes: 3-5 days on counter (fridge kills flavor but extends life)

### Tips for Extending Life
- **Freeze** meat on day of purchase if not cooking within 2 days
- **Store herbs** like flowers in water (basil, cilantro)
- **Wrap greens** in paper towel to absorb moisture
- **Keep bananas** away from other fruit (ethylene gas)
- **Don't wash berries** until ready to eat

## Adding Custom Categories

To add a custom category, simply use `--days` when adding:

```bash
python expiry_tracker.py add "kimchi" --days 30
python expiry_tracker.py add "sourdough starter" --days 365
```

The tracker will still try to categorize for reporting, but the expiry date is what matters for alerts.
