## Description:

Reply.io lets an agent inspect live action schemas and run connected actions to read, create, and update Reply.io contacts and sequences through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Reply.io contacts and sequences from an agent through their connected OOMOL account. It supports read operations, contact creation and updates, and sequence start or pause workflows with user confirmation for write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that could be risky if run without review.

Mitigation: Review the installer path first and prefer a pinned, signed, or checksum-verified oo CLI release before installation.

Risk: Create, update, start, and pause actions can change Reply.io data.

Mitigation: Confirm the exact payload and intended effect with the user before running any write action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-reply-io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Reply.io Homepage](https://reply.io)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and meta.executionId when actions are run.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
