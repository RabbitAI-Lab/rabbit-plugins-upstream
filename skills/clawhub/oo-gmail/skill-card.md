## Description:

Uses the OOMOL Gmail connector through the oo CLI to read, create, update, send, organize, and delete Gmail data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to let an agent operate a connected Gmail mailbox for message retrieval, drafting, sending, labeling, filtering, settings review, and mailbox organization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate with broad Gmail mailbox authority, including send, update, delete, forwarding, filter, label, and settings changes.

Mitigation: Require explicit user approval for every write or destructive action, including the exact target, payload, and expected effect.

Risk: The setup instructions include remote-script CLI installer commands.

Mitigation: Do not run installer commands blindly; prefer reviewed or manual installation steps before using the skill.

Risk: Incorrect action payloads could change or remove Gmail data.

Mitigation: Inspect the live connector schema before constructing payloads and confirm destructive targets with the user.

## Reference(s):

- [ClawHub Gmail Skill](https://clawhub.ai/oomol/skills/oo-gmail)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Gmail Homepage](https://workspace.google.com/gmail/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.5 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
