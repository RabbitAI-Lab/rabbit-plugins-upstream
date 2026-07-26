## Description: <br>
Log and track daily calorie intake, macronutrients, body weight, and waist measurements locally in a SQLite database. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[patello](https://clawhub.ai/user/patello) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents and users use this skill to maintain a local food, macronutrient, weight, and body-measurement log and generate daily, weekly, and trend reports for personal tracking. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores personal health and nutrition data in a local SQLite database file. <br>
Mitigation: Use a protected database path, restrict access to the file, and avoid placing the database in shared or broadly synced locations unless that is intended. <br>
Risk: Update and delete commands intentionally modify or remove local tracker records. <br>
Mitigation: Review entry IDs with list or stats commands before changing records, and keep a backup when preserving history matters. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/patello/skills/caloric-intake-tracker) <br>
- [README.md](README.md) <br>
- [SKILL.md](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and plain-text CLI reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and uses a local SQLite database file; evidence reports no network access or hidden behavior.] <br>

## Skill Version(s): <br>
1.4.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
