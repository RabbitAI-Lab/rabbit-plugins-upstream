## Description:

Shipday enables an agent to read, create, update, and delete Shipday delivery data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to manage Shipday delivery orders and retrieve active orders, carriers, and real-time order progress through the oo CLI after connecting Shipday in OOMOL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded code directly.

Mitigation: Review the oo CLI installation path before installing and prefer official, versioned, signed, or checksum-verified installer options.

Risk: Create, edit, and delete actions can change or remove Shipday delivery data.

Mitigation: Confirm the exact payload, target, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-shipday)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Shipday Homepage](https://www.shipday.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent output may include oo CLI commands, connector JSON responses, and confirmation prompts for write or destructive actions.]

## Skill Version(s):

1.0.4 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
