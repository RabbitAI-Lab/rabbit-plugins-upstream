## Description: <br>
Access Cookidoo (Thermomix) recipes, shopping lists, and meal planning via the unofficial cookidoo-api Python package. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thekie](https://clawhub.ai/user/thekie) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to query their Cookidoo account for recipes, shopping lists, account information, and meal-planning data from an agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires Cookidoo account email and password credentials. <br>
Mitigation: Use environment variables or a secure secrets store, avoid plaintext credential files when possible, and do not commit credentials into the skill folder. <br>
Risk: Cookidoo account-connected commands may expose account, recipe, shopping-list, or meal-planning data and may affect account state if write-capable behavior is added or used. <br>
Mitigation: Review commands before execution, especially any command that changes shopping lists or meal plans, and run the skill only for accounts where this access is acceptable. <br>
Risk: The skill depends on the unofficial cookidoo-api package, which may stop working if Cookidoo changes its service behavior. <br>
Mitigation: Confirm the dependency still works in the target environment before relying on the skill for recurring meal-planning or shopping-list workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thekie/skills/cookidoo) <br>
- [cookidoo-api Python package](https://pypi.org/project/cookidoo-api/) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Plain text or JSON returned by CLI commands, plus Markdown usage guidance with inline shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Cookidoo account credentials and an active Cookidoo subscription.] <br>

## Skill Version(s): <br>
1.0.1 (source: package.json and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
