## Description: <br>
Manage Thermomix/Cookidoo meal planning via tmx-cli for recipe search, weekly meal plan management, shopping list generation, favorites, and recipe details. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lars147](https://clawhub.ai/user/lars147) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agents use this skill to operate tmx-cli for Cookidoo recipe lookup, meal planning, favorites management, and shopping-list maintenance. It is intended for users who have a Cookidoo account and want structured command-line or agent-mediated meal-planning workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access and modify Cookidoo account data, including meal plans, favorites, and shopping lists. <br>
Mitigation: Review proposed commands before execution, especially remove, move, clear, and favorite-changing actions. <br>
Risk: Session material and local cache files are stored on disk with limited safeguards. <br>
Mitigation: Prefer interactive login, avoid passing passwords on the command line, protect local skill and cache files, and clear cookies or tokens when the integration is no longer needed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/lars147/skills/tmx-cli) <br>
- [Full Command Reference](references/commands.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and optional JSON or Markdown CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports --json for machine-readable command output; shopping lists can be exported as text, Markdown, or JSON.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence and pyproject.toml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
