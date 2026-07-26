## Description: <br>
Apple Health Skill Free helps agents retrieve daily workout plans, workout records, and athlete profile information from a configured health data API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to query basic workout plans, workout history, and athlete profile data through a health data synchronization service. It is intended for basic training data review, with coaching chat and performance analytics reserved for the full version. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can query sensitive workout history, heart-rate details, and athlete profile information through the configured health API. <br>
Mitigation: Install only when this health data access is acceptable, query only needed date ranges, and avoid pasting raw health data into unrelated chats or logs. <br>
Risk: The configured health API key could expose access to private training data if shared or committed. <br>
Mitigation: Keep the API key private, store it in the local environment, and do not commit it to version control. <br>


## Reference(s): <br>
- [SkillHub Homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include API endpoint examples, environment variable setup, date range constraints, quota notes, and structured JSON response examples.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
