## Description:

Skyvern (skyvern.com). Use this skill for ANY Skyvern request: reading, creating, updating, and deleting data through an OOMOL-connected Skyvern account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Skyvern browser automation through OOMOL, including starting tasks, listing runs, inspecting run outputs, and cancelling active runs with explicit approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional oo CLI installer is a remote shell or PowerShell command.

Mitigation: Review the install path and installer source before running it; run setup only when the oo CLI is missing.

Risk: Skyvern task creation and cancellation can change or stop browser automation work.

Mitigation: Confirm the exact payload and effect before write actions, and require explicit approval before cancelling runs.

## Reference(s):

- [ClawHub Skyvern skill page](https://clawhub.ai/oomol/skills/oo-skyvern)
- [Skyvern homepage](https://www.skyvern.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI to inspect live connector schemas before constructing payloads.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
