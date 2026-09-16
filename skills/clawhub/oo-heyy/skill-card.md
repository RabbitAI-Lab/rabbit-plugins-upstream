## Description:

Heyy (heyy.io). Use this skill for ANY Heyy request \u2014 reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Heyy through an OOMOL-connected account, including reading contacts, channels, labels, and attributes and creating or updating contacts, labels, and contact attribute definitions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may execute mutable remote installer scripts directly in a shell.

Mitigation: Review installer commands before use and prefer official, versioned, signed, or checksum-verified installation steps when available.

Risk: Write actions can create labels, contact attributes, and contacts or update existing Heyy contact data.

Mitigation: Confirm the exact payload and expected effect with the user before running actions tagged write.

## Reference(s):

- [Heyy homepage](https://heyy.io)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-heyy)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects with data and meta.executionId fields.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
