## Description: <br>
绿灵·Blooming Elf-v4 is a plant and flower care assistant that helps users maintain local watering, fertilizing, reminder, pet-toxicity, and microclimate records with validation-backed persistence. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shirley1011](https://clawhub.ai/user/shirley1011) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External plant owners and care hobbyists use this skill to set up local plant records, receive concise care and reminder guidance, and keep watering, fertilizing, pet-toxicity, and microclimate state consistent across sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill persistently stores local plant records, logs, backups, and reminder state. <br>
Mitigation: Install it only when local plant-state management under ~/.workbuddy is desired, and keep user plant data outside the published skill package. <br>
Risk: Authorization can allow the skill or its tests to read a user's plants.json. <br>
Mitigation: Use the authorization flow only for the intended plants.json, require explicit user consent, and run validation on temporary copies when testing real data. <br>
Risk: Recurring reminders may be created or updated from user configuration. <br>
Mitigation: Review reminder time, location, and prompt content before confirming any scheduled reminder. <br>
Risk: Plant-care and pet-toxicity guidance can affect user decisions about plant placement and handling. <br>
Mitigation: Keep the artifact's pet-toxicity warnings visible, and direct users to veterinary or professional plant-care advice for urgent or uncertain cases. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/shirley1011/skills/blooming-elf-v4) <br>
- [Changelog](CHANGELOG.md) <br>
- [Authorization mechanism](references/authorization.md) <br>
- [State schema](references/state-schema.md) <br>
- [Onboarding and data entry flow](references/onboarding.md) <br>
- [Care quick reference](references/care-quickref.md) <br>
- [Plant library](references/plant-library.md) <br>
- [Pet toxicity reference](references/toxicity-reference.md) <br>
- [Care supplements](references/supplements.md) <br>
- [Expert audit map](references/expert-audit-map.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses with inline shell commands and JSON file changes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May update local plants.json state, logs, backups, and user-confirmed reminders.] <br>

## Skill Version(s): <br>
4.0.4 (source: frontmatter, server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
