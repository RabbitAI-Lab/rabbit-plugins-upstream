# User profile

Collect only what is needed. Reuse the saved profile when one exists (agent memory / user config) and ask only for missing fields, one or two at a time. Do not hardcode private health data into this skill's files; store it in the user's profile/memory or ask each time.

## Fields

| Field | Why it is needed | Notes / defaults |
|---|---|---|
| Age | BMR equation and safety | Required. If under 18 or over 65, add extra caution and recommend professional guidance. |
| Sex | BMR equation | male / female / other |
| Height | BMI and calorie math | cm or in |
| Weight | BMI and calorie math | kg or lb |
| Activity level | TDEE multiplier | sedentary / light / moderate / active / very active |
| Goal | Calorie target | lose / maintain / gain (muscle) |
| Health conditions & limitations | Safety and plan adaptation | e.g. diabetes, hypertension, joint/knee problems, injuries, pregnancy (refer to a professional — do not plan), medication affecting diet |
| Dietary preferences / restrictions | Meal planning | vegetarian / vegan, halal, allergies, intolerances, foods they dislike |
| Training experience & equipment | Workout plan | beginner / intermediate / advanced; gym / home / bodyweight; days available per week |
| Daily routine | Schedule and meal timing | wake time, meal times, preferred workout time, bedtime |
| Timezone | Scheduling | IANA name, e.g. `Asia/Shanghai`, `America/New_York` — never abbreviations like CST/PST |
| Language | Output | one of the 8 in languages.md |

## Collection tips

- Start with the minimum set (age, sex, height, weight, activity level, goal, language, timezone), then ask about health and restrictions, framed as optional but recommended: "Any conditions or injuries I should account for? Any foods to avoid?"
- If the user does not know their timezone, derive it from their device/OS, or ask for city/country and map it to an IANA name.
- If the user is a minor, has a chronic condition, is pregnant, or is on medication that affects diet/training, recommend professional medical or nutritional review before following the plan.
- Save the completed profile back to the user's profile/memory (not into the skill folder) so future runs can reuse it.
