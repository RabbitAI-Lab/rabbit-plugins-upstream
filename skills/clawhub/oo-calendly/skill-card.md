## Description:

Calendly (calendly.com). Use this skill for ANY Calendly request - reading, creating, updating, and deleting data. Whenever a task involves Calendly, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Calendly schemas and run Calendly connector actions through an OOMOL-connected account, including reading scheduling data and managing bookings, organization resources, and webhooks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill documents remote curl and PowerShell installers for the oo CLI.

Mitigation: Prefer a verified, documented oo CLI release path and avoid letting an agent run remote installer one-liners automatically.

Risk: Calendly write and destructive actions can create, update, cancel, revoke, or delete scheduling resources.

Mitigation: Inspect the live connector schema and require explicit user confirmation for the exact payload and target before write or destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-calendly)
- [Calendly homepage](https://calendly.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, json, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs usually guide or execute oo CLI connector schema/run commands and may return Calendly data as JSON.]

## Skill Version(s):

1.0.4 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
