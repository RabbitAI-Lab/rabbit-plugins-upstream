## Description:

Zixflow (zixflow.com). Use this skill for Zixflow requests covering reading, creating, updating, and deleting workspace data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Zixflow connector schemas and perform Zixflow workspace operations such as listing, querying, creating, updating, and deleting collections, lists, records, entries, and members.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of remote installer scripts for the oo CLI.

Mitigation: Review and verify the installer source before use, or use an approved package-management or verification path for the oo CLI.

Risk: Write and destructive Zixflow actions can change or delete workspace data.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before running any action tagged write or destructive.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-zixflow)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Zixflow homepage](https://zixflow.com)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Normal read actions can be run directly; write and destructive actions require user confirmation before execution.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
