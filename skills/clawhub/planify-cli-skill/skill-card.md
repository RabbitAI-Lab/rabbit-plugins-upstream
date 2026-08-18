## Description:

Manage tasks and projects via planify-cli commands to add, list, update, and export tasks with JSON-formatted results for scripting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[elzorrorebelde](https://clawhub.ai/user/elzorrorebelde)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and task-management users use this skill to have an agent operate Planify through planify-cli: creating, listing, updating, completing, and exporting tasks with JSON output suitable for scripting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to create or update Planify tasks when the user requests those actions.

Mitigation: Use it only when you want the agent to operate Planify, and review task-changing requests before execution.

Risk: Backup commands can export task data to a chosen file path.

Mitigation: Run backups only on explicit user request and choose an output path appropriate for the sensitivity of the exported task data.

Risk: Task and project identifiers can be ambiguous if guessed or reused incorrectly.

Mitigation: Resolve IDs from prior add, list, list-projects, or cache lookup results in the current session rather than guessing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/elzorrorebelde/skills/planify-cli-skill)
- [Artifact SKILL.md](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell command examples and option tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands described by the skill emit JSON from planify-cli when executed.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
