## Description:

Megaventory connector skill for reading, creating, and updating Megaventory data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Megaventory through the OOMOL-connected oo CLI, including listing products, locations, suppliers/clients, sales orders, and purchase orders. It also guides confirmed write actions for creating or updating products and orders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can change products, sales orders, and purchase orders in Megaventory.

Mitigation: Confirm the exact payload and expected effect with the user before running any write action.

Risk: A stale or incorrect action schema can lead to malformed or unintended connector calls.

Mitigation: Inspect the live connector schema with the oo CLI before constructing each payload.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-megaventory)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Megaventory homepage](https://www.megaventory.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the OOMOL oo CLI and should inspect the live connector schema before building payloads.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
