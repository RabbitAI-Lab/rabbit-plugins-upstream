## Description: <br>
Persona Switcher routes an agent across asset-advisor, graduate-exam mentor, coding expert, graduation-project expert, and general personas with persistent state and self-improvement tagging. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xianggu-big](https://clawhub.ai/user/xianggu-big) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agent users and skill maintainers use this skill to let a single assistant detect conversation intent, switch between specialized persona rules, or manually override the active persona while keeping persona-specific learning records separated from shared improvements. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The asset-advisor persona can ask the agent to read local financial holdings for portfolio context. <br>
Mitigation: Require explicit user confirmation before reading financial files and avoid loading holdings unless they are needed for the current request. <br>
Risk: Persistent self-improvement records can carry user preferences or conversation details into future behavior. <br>
Mitigation: Review learning entries and proposed behavior-file promotions before adopting them, and keep sensitive details out of shared records. <br>
Risk: Automatic persona switching can apply an unintended persona or advice style to an ambiguous conversation. <br>
Mitigation: Confirm the active persona when the domain is unclear and keep manual override available for corrections. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xianggu-big/skills/persona-switcher) <br>
- [Self-improving-agent compatibility](references/compatibility.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON configuration updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May update persona state and append persona-tagged learning records when used by an agent.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
