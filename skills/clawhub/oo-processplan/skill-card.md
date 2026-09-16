## Description:

ProcessPlan connector for reading ProcessPlan data, listing tasks, instances, and templates, and starting processes through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations users use this skill to operate ProcessPlan through an OOMOL-connected account, including listing assigned tasks, reviewing process instances and templates, and starting a process from a template.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions ask users to run remote installer scripts directly in a shell.

Mitigation: Install the oo CLI through a verified official package or a downloaded installer with checksum or signature validation before using the skill.

Risk: The start_process action changes ProcessPlan state.

Mitigation: Inspect the live action schema and confirm the exact payload and expected effect with the user before starting a process.

## Reference(s):

- [ProcessPlan homepage](https://processplan.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub ProcessPlan skill](https://clawhub.ai/oomol/skills/oo-processplan)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill expects live connector schema inspection before action execution and JSON payloads for connector runs.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
