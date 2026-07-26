## Description: <br>
Helps agents assess micronutrient gaps, diet quality, lab context, supplements, and food-drug interactions while routing health red flags to clinicians. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and assistants use this skill for micronutrient coverage checks, supplement review, label and lab interpretation, food-drug interaction checks, and nutrition guidance for diet patterns, life stages, and relevant health conditions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may read and update sensitive nutrition and health records without a clear confirmation step. <br>
Mitigation: Require explicit user confirmation before writes to health/profile.md, config.yaml, contacts, due dates, or artifacts, especially for labs, medications, pregnancy or life stage, conditions, allergies, and clinician names. <br>
Risk: Nutrition, supplement, and lab guidance could affect health decisions if treated as a substitute for clinician care. <br>
Mitigation: Keep clinician-ordered or prescribed care advise-only, route red flags to a clinician, and require health profile checks before food, dose, or supplement recommendations. <br>


## Reference(s): <br>
- [ClawHub Nutrition Skill Page](https://clawhub.ai/ivangdavila/skills/nutrition) <br>
- [Clawic Nutrition Page](https://clawic.com/skills/nutrition) <br>
- [Nutrition Skill Definition](artifact/SKILL.md) <br>
- [Safety Guide](artifact/safety.md) <br>
- [Working File Templates](artifact/memory-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown guidance with structured local record updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May update local nutrition, health, contacts, due-date, and artifact records when durable user-specific information is produced.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
