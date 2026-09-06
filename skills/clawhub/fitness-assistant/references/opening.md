# Opening message and intake

The first time the user asks for a plan (or when no saved profile exists), send a short opening message in their language. It explains what the skill will do and what details the user should prepare, so the resulting diet and workout plan fits them. Then collect the missing profile fields (see profile.md) one or two questions at a time.

## Opening message template

English version below; write the entire message in the user's chosen language (see languages.md), keeping the same order and structure.

```text
Hi! I'm your fitness assistant. I'll build you a personalized one-day meal plan and workout. To make it fit you well, I'll ask a few questions first — you can answer all at once or one by one.

Please be ready to tell me:
1. Your basics and goal — age, sex, height, weight, how active your daily life is, and whether you want to lose, maintain, or gain weight.
2. Your food choices — anything you must avoid (allergies, vegetarian/vegan, halal, etc.), foods you dislike, and which ingredients you'd like for your meals (protein, carbs, vegetables, fats, snacks).
3. Your training — experience level, equipment (gym / home / none), how many days per week and at what time you prefer to train, how intense you want the session to be (light / moderate / high), and how long you can spend.
4. Where and when to deliver — your timezone, preferred language, and whether you want a one-time plan or a daily scheduled message.

For any item you don't care about, just say "you decide" and I'll pick sensible defaults.
```

## Rules

- Ask the profile fields in the order above, but no more than one or two questions at a time, and wait for answers before continuing.
- Ingredient choices come from the options in meal-planning.md; tell the user they can pick or say "you decide".
- Training time means preferred days and clock (e.g. "07:00, Mon/Wed/Fri") — it also decides how meals sit around the workout. Training intensity is light / moderate / high (or RPE 1-10) and maps to the intensity table in training.md.
- If a saved profile exists, do not repeat the full opening: give a one-line recap of the saved settings, ask only what changed or is missing, then build the plan.
- Save all answers to the user's profile/memory (never into the skill folder) so later scheduled runs reuse them.
- Deliver the opening in the user's chosen language only; never mix languages.
