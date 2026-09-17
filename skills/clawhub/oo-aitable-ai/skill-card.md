## Description:

AITable lets agents read, create, update, and delete AITable data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent manage AITable spaces, datasheets, fields, views, and records through an authenticated OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that could execute arbitrary code if the installer source is not trusted or verified.

Mitigation: Review the skill before installing and prefer a documented, pinned, or signed oo CLI installation method where available.

Risk: Create, update, and delete actions can modify or remove AITable records.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions, and require explicit approval before destructive actions.

## Reference(s):

- [ClawHub AITable Skill](https://clawhub.ai/oomol/skills/oo-aitable-ai)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [AITable Homepage](https://aitable.ai)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return JSON responses from the oo CLI when run with --json.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
