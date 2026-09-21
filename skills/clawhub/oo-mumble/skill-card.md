## Description:

Mumble helps agents inspect live schemas and manage Mumble customer and label data through an OOMOL-connected oo CLI account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to read, create, update, and delete Mumble WhatsApp customer records and labels through OOMOL's oo CLI without handling raw credentials. It is intended for connected OOMOL accounts where the agent should inspect live action schemas before running connector actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can create or update Mumble customer and label data in the connected OOMOL account.

Mitigation: Confirm the exact action, target, and JSON payload with the user before running write-tagged connector actions.

Risk: Destructive actions can permanently delete Mumble customers or labels.

Mitigation: Require explicit approval for the specific delete target before running destructive connector actions.

Risk: CLI installation commands fetch remote scripts.

Mitigation: Use verified official oo CLI installation guidance and avoid blindly running remote install scripts.

## Reference(s):

- [ClawHub Mumble skill page](https://clawhub.ai/oomol/skills/oo-mumble)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Mumble homepage](https://mumble.co.il/)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and meta.executionId fields when actions run with --json.]

## Skill Version(s):

1.0.1 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
