## Description: <br>
Provides practical nutrition guidance for calorie and macro estimates, TDEE/BMR calculations, meal planning, food and hydration logging, restaurant meal estimation, cycle-aware nutrition, and related diet topics while excluding medical diagnosis and non-diet advice. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yamyeed](https://clawhub.ai/user/yamyeed) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill when they explicitly ask for nutrition or diet-related help, including calorie targets, macro planning, meal estimates, food substitutions, hydration tracking, and goal-aligned meal planning. It is not intended for diagnosis, treatment, urgent symptoms, or management of medical conditions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may process personal health-adjacent information, including weight, diet, allergies, and menstrual-cycle details. <br>
Mitigation: Collect only the information needed for the current task and use optional local logging only after the user confirms they are comfortable storing data under ~/nutrition-data. <br>
Risk: Nutrition estimates or meal guidance could be mistaken for medical advice in higher-risk situations. <br>
Mitigation: Keep outputs framed as estimates and direct users to a clinician or registered dietitian for medical conditions, pregnancy, eating disorder history, medication-related glucose issues, severe symptoms, or urgent concerns. <br>
Risk: Aggressive calorie restriction, unsafe fasting, or extreme diet targets could harm users. <br>
Mitigation: Use moderate calorie adjustments, avoid unsafe lower intake thresholds without professional supervision, and prioritize food-first, sustainable guidance. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/yamyeed/skills/nutrition-advisor-en) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Calculations, Configuration] <br>
**Output Format:** [Markdown with tables, concise dashboards, estimates, and JSON file structures when local logging is requested] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose optional local JSON storage under ~/nutrition-data only after user confirmation; nutrition numbers are framed as estimates.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
