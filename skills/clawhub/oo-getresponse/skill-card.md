## Description:

Use this skill for GetResponse requests that read, create, update, or delete account data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage GetResponse campaigns, contacts, newsletters, tags, and custom fields through an OOMOL-connected account. It supports read actions and confirmed write or destructive account changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write and destructive actions can change, overwrite, or delete GetResponse account data.

Mitigation: Confirm the exact campaign, contact, action, and payload with the user before running write or destructive commands.

Risk: The first-time setup flow may require installing the oo CLI through a remote installer.

Mitigation: Install the oo CLI only from trusted OOMOL guidance and prefer available checksum or package-manager verification.

## Reference(s):

- [GetResponse homepage](https://www.getresponse.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-getresponse)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads; connector responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before payload construction and requires confirmation before write or destructive actions.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
