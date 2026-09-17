## Description:

Checkout.com helps agents manage Checkout.com customer records through the OOMOL oo CLI, including reading, creating, updating, and deleting customers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to manage Checkout.com customer records through an OOMOL-connected Checkout.com account. It supports read, create, update, and delete workflows where state-changing actions require user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup uses a remote installer command that is not pinned or checksum-verified.

Mitigation: Prefer a pinned, signed, or checksum-verified oo CLI installation source before using the skill.

Risk: Write and destructive Checkout.com customer actions can change or delete customer records.

Mitigation: Confirm the exact action, customer target, and payload with the user before running write or delete commands.

Risk: Connector action payloads may be incorrect if built from stale assumptions.

Mitigation: Fetch the live connector schema with the oo CLI before constructing each action payload.

## Reference(s):

- [Checkout.com homepage](https://www.checkout.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-checkout-com)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches live connector schemas before building payloads; write and destructive customer actions require explicit user confirmation.]

## Skill Version(s):

1.0.2 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
