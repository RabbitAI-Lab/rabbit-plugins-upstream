## Description:

Photoroom (photoroom.com) helps agents handle Photoroom requests through an OOMOL-connected account, including reading, creating, and updating data via the supported connector workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Photoroom through an OOMOL-connected account, especially for composed ecommerce product-image edits from an image URL. The skill guides agents to inspect the live connector schema, run the Photoroom action with a JSON payload, and return the edited image URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer one-liners that execute downloaded scripts directly.

Mitigation: Use a trusted package source when available, or download, verify, inspect, and run the installer separately without elevated privileges.

Risk: The product-image edit action changes Photoroom state and can produce edited assets that may be misleading if published without review.

Mitigation: Confirm the exact action payload and expected effect with the user before execution, and review outputs that use relighting, text removal, or beautification before publishing.

Risk: Connector schemas may change over time, causing stale payload assumptions.

Mitigation: Inspect the live connector schema with `oo connector schema` before constructing each action payload.

## Reference(s):

- [ClawHub Photoroom Skill](https://clawhub.ai/oomol/skills/oo-photoroom)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Photoroom Homepage](https://www.photoroom.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return a Photoroom edited image URL from connector transit storage.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
