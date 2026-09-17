## Description:

Operate Photoroom through an OOMOL-connected account to edit ecommerce product images and return hosted result URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent inspect the live OOMOL Photoroom connector schema, run supported Photoroom actions, and produce edited product-image results for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer one-liners for the oo CLI.

Mitigation: Verify the installer source and prefer official installation steps before running any shell installer.

Risk: The product-image edit action is a write action that can create edited assets from a user-provided payload.

Mitigation: Confirm the live connector schema, exact payload, and intended effect with the user before execution; review relighting, text removal, or beautification outputs before publishing.

## Reference(s):

- [ClawHub Photoroom Skill](https://clawhub.ai/oomol/skills/oo-photoroom)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Photoroom Homepage](https://www.photoroom.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Photoroom result URLs from connector actions.]

## Skill Version(s):

1.0.2 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
