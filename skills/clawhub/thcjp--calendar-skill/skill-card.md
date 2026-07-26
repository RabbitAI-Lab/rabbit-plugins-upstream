## Description: <br>
Calendar Skill helps agents manage Google Calendar, Microsoft Outlook, and Exchange scheduling workflows, including calendar access, cross-platform views, and meeting scheduling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent operators use this skill to coordinate calendar actions across Google Calendar, Outlook, and Exchange. It is intended for account-backed scheduling workflows, not offline planning without calendar API access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may trigger real Google, Outlook, or Exchange calendar changes without enough scoped detail in the artifact. <br>
Mitigation: Confirm the account scopes before granting access and require explicit user confirmation before event creation, modification, or deletion. <br>
Risk: The artifact mixes calendar functionality with unrelated security-audit and grading claims. <br>
Mitigation: Use the skill only for reviewed calendar workflows and do not rely on unrelated audit, scoring, or compliance claims. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/calendar-skill) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with JSON examples and shell configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May describe calendar actions that should be reviewed before execution against real accounts.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
