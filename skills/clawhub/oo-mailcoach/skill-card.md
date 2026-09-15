## Description:

Mailcoach (mailcoach.app) lets an agent read, create, update, and delete Mailcoach data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Mailcoach email lists and subscribers through validated oo CLI connector actions, including read, write, and destructive workflows that require confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can run an unverified internet installer with local code execution capability.

Mitigation: Review the installer source and prefer a verified official oo CLI release or package source with integrity checks before installation.

Risk: Write and destructive Mailcoach actions can change or remove email lists and subscriber records.

Mitigation: Fetch the live action schema, verify the exact target and payload, and require explicit user confirmation before executing write or destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-mailcoach)
- [Mailcoach Homepage](https://www.mailcoach.app)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before running actions and returns oo CLI JSON responses when commands are executed.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
