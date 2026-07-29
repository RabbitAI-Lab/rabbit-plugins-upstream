## Description: <br>
Helps an agent assess micronutrient gaps, diet quality, supplements, food-drug interactions, relevant lab markers, and nutrition safety boundaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to reason about nutrient sufficiency, diet quality, supplements, interactions, nutrition-relevant labs, and when to route health questions to a clinician. It is suited to food-first nutrition guidance and local tracking, not diagnosis, calorie counting, meal planning, or medication changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can persist sensitive health, nutrition, lab, medication, and contact information in local notes across sessions. <br>
Mitigation: Install only when this persistence is desired, review the configured Clawic health, nutrition, and contacts folders before and after use, and avoid sharing medical details that should not be stored locally. <br>
Risk: Nutrition and supplement guidance can be unsafe when allergies, conditions, medications, pregnancy, kidney disease, disordered eating signals, or lab context are missing. <br>
Mitigation: Review recommendations before acting, keep the shared health profile current, and route red-flag symptoms, medication changes, high-risk supplements, and clinician-directed plans to an appropriate professional. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ivangdavila/skills/nutrition) <br>
- [Clawic Nutrition Skill](https://clawic.com/skills/nutrition) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown and plain-language guidance, with local note updates when persistent nutrition or health facts are produced] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May maintain local nutrition, health, and contacts notes under configured Clawic data paths.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
