## Description:

Enables an agent to read, create, edit, reply to, and delete Reddit content through an authenticated OOMOL-connected Reddit account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let agents perform authenticated Reddit reading and content-management workflows, including profile lookup, post listing, search, comment retrieval, posting, replying, editing, and deletion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer scripts that execute directly.

Mitigation: Review the installer path first and prefer a verified package or inspected installer before installing the oo CLI.

Risk: Write, edit, and delete actions can change or remove Reddit content.

Mitigation: Confirm the exact payload, account context, target content, and intended effect with the user before running state-changing actions.

Risk: Connector payload contracts can change over time.

Mitigation: Inspect the live action schema before each run and construct payloads only from the current connector contract.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-reddit)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Reddit homepage](https://www.reddit.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live action schema inspection before constructing connector payloads; write and destructive actions require clear user confirmation.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
