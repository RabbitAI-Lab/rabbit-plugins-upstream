## Description:

Paperform (paperform.co). Use this skill for ANY Paperform request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to read Paperform forms, fields, products, coupons, submissions, and partial submissions through an OOMOL-connected Paperform account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes a remote shell installer for the oo CLI.

Mitigation: Review the installer path before installation and prefer a trusted, versioned release or package manager with checksum or signature verification.

Risk: The connected Paperform account may expose accessible forms and submissions through the connector.

Mitigation: Connect only a Paperform account whose accessible forms and submissions are appropriate for agent access.

## Reference(s):

- [Paperform homepage](https://paperform.co)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-paperform)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas to shape action payloads before execution.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
