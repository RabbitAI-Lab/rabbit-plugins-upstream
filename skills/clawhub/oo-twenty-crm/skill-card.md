## Description:

Twenty CRM helps agents read, create, update, and delete Twenty CRM data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and external CRM users use this skill to manage Twenty CRM workspace records through OOMOL's connected CLI, including schema inspection and record create, retrieve, list, update, and delete workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands that run scripts directly.

Mitigation: Review before installing and prefer an official package or a downloaded, inspected, version-pinned installer with a verified checksum or signature.

Risk: Write and destructive CRM actions can change or delete workspace records.

Mitigation: Inspect the live action schema first and confirm the exact payload, target record, and intended effect with the user before execution.

## Reference(s):

- [Twenty CRM homepage](https://twenty.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live action schema inspection before payload construction; write and destructive operations require user confirmation.]

## Skill Version(s):

1.0.2 (source: release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
