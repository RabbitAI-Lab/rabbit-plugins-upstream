## Description: <br>
Indonesian kitchen companion skill that turns leftover ingredients or food photos into safety-checked Indonesian recipe recommendations, guided cooking steps, and food-waste reduction tracking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jrrqd](https://clawhub.ai/user/jrrqd) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to turn leftover ingredients or food photos into Indonesian recipe recommendations, safety checks, and step-by-step cooking guidance. It also helps track local cooking sessions and food-waste reduction history. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can save cooking history and food images in its local workspace. <br>
Mitigation: Install only if local storage of those records is acceptable for the user and environment. <br>
Risk: The /clear command deletes saved history, stats, and workspace data without an extra confirmation step. <br>
Mitigation: Use /clear only after confirming the saved data is no longer needed. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/jrrqd/skills/dont-waste-food) <br>
- [Indonesian recipe database](references/resep_indonesia.json) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Conversational Markdown with inline shell commands and local session data] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save cooking history and food images in a local workspace; the /clear command deletes saved history, stats, and workspace data without an extra confirmation step.] <br>

## Skill Version(s): <br>
1.1.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
