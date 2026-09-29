## Description:

Builds automation workflows from repetitive tasks. Use when user mentions "automate", "save time", "reduce manual work", or has repeated tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xaiohuangningde](https://clawhub.ai/user/xaiohuangningde)

### License/Terms of Use:


## Use Case:

Developers and automation-minded users use this skill to identify repetitive manual tasks and produce automation workflows, scripts, and configuration steps for small-scale validation and iteration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may proactively create scripts or workflows for repeated tasks, which can lead to unintended file, email, scheduling, or sensitive-data actions.

Mitigation: Constrain the agent to propose plans first and require explicit approval before writing files, running tests, sending email, using sensitive data, or creating recurring schedules.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xaiohuangningde/skills/auto-workflow)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with workflow steps, scripts, shell commands, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose automation plans and executable artifacts that should be reviewed before use.]

## Skill Version(s):

1.0.0 (source: skill.json and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
