## Description:

BigCommerce (bigcommerce.com). Use this skill for ANY BigCommerce request -- reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and commerce operators use this skill to manage BigCommerce catalog products through an OOMOL-connected account, including create, retrieve, list, update, and delete workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer scripts executed directly in a shell.

Mitigation: Review the installer path before installing; prefer official documentation or a pinned release with checksum or signature checks.

Risk: BigCommerce write and delete actions can change or remove catalog products.

Mitigation: Confirm exact write payloads with the user and require explicit approval before destructive deletion actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-big-commerce)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [BigCommerce homepage](https://www.bigcommerce.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce BigCommerce connector commands that return JSON responses from the oo CLI.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
