## Description:

KrispCall helps an agent read workspace, member, and contact data and perform confirmed contact create, update, and delete actions through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent manage KrispCall workspace information and contacts from a connected OOMOL account while requiring confirmation for write and destructive contact changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that can execute arbitrary code under the user's account.

Mitigation: Review and trust the OOMOL installer source before running setup commands; avoid running remote installer commands automatically.

Risk: Write and destructive contact actions can modify or delete KrispCall data.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-krispcall)
- [KrispCall homepage](https://krispcall.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL KrispCall connection console](https://console.oomol.com/app-connections?provider=krispcall)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches live connector schemas before actions; write and destructive operations require user confirmation.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
