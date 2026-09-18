## Description:

Goody (ongoody.com) skill for reading, creating, and updating Goody data through an OOMOL-connected oo CLI workflow instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents with a connected OOMOL account use this skill to inspect Goody action schemas and retrieve Goody users, orders, products, payment methods, and workspaces. The skill can also support state-changing Goody actions when the user confirms the exact payload and effect.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer execution that should be reviewed before installation.

Mitigation: Install the oo CLI through a verified, version-pinned package or official instructions that can be inspected before execution.

Risk: The Goody activation scope includes operations that can change orders, payments, workspaces, or account state.

Mitigation: Require explicit user confirmation of the exact payload and expected effect before running any state-changing Goody action.

Risk: Connector payloads may drift from documented examples if the live Goody action schema changes.

Mitigation: Inspect the live action schema with the oo CLI before constructing each request.

## Reference(s):

- [ClawHub Goody Skill](https://clawhub.ai/oomol/skills/oo-goody)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Goody homepage](https://www.ongoody.com)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Goody action schemas before constructing connector requests.]

## Skill Version(s):

1.0.4 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
