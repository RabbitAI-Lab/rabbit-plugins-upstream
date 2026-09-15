## Description:

Uses the OOMOL oo CLI to inspect ntfy connector schemas, retrieve account details, and publish notifications through an OOMOL-connected ntfy account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate ntfy through an OOMOL-connected account, including retrieving account profile, limits, and usage and publishing notifications to topics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Review the installer delivery path before installation and prefer a verified package, pinned release, checksum, or official process that allows inspection before execution.

Risk: The publish_message action changes ntfy state by sending a notification.

Mitigation: Confirm the exact topic, payload, and effect with the user before running the write action.

## Reference(s):

- [ntfy homepage](https://ntfy.sh)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ntfy)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live oo connector schema inspection before actions and user confirmation before publishing notifications.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
