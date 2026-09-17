## Description:

This skill lets agents operate Respond.io through the OOMOL respond_io connector to read, create, update, and delete workspace data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to manage Respond.io contacts, tags, users, channels, and conversations in an authenticated OOMOL-connected workspace.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer scripts that could execute unverified code.

Mitigation: Review the installer path before installing and prefer a versioned package or separately downloaded and verified installer.

Risk: The skill can read and change Respond.io workspace data, including write and destructive contact or tag actions.

Mitigation: Approve write or destructive actions only after checking the exact target and payload.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-respond-io)
- [Respond.io Homepage](https://respond.io/)
- [oo CLI Repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Respond.io connector results when actions are executed.]

## Skill Version(s):

1.0.2 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
