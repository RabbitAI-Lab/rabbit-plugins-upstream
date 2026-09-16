## Description:

Use this skill to read, create, update, and delete Lemon Squeezy data through the OOMOL connector and oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Lemon Squeezy stores, customers, products, variants, orders, subscriptions, and webhooks through the OOMOL connector and oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands that run downloaded scripts in a shell.

Mitigation: Review the oo CLI installation source first and prefer a versioned, signed, or checksum-verified installation path.

Risk: Write and destructive actions can change or delete Lemon Squeezy account data.

Mitigation: Approve these actions only after checking the exact payload, target account data, and requested effect.

## Reference(s):

- [Lemon Squeezy homepage](https://www.lemonsqueezy.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-lemon-squeezy)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI commands that read from or modify Lemon Squeezy account data after schema inspection and user confirmation for write or destructive actions.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
