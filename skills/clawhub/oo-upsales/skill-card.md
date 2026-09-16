## Description:

Enables an agent to read, create, update, and delete Upsales companies, contacts, and users through an OOMOL-connected Upsales account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to manage Upsales account data through an agent, including listing, retrieving, creating, updating, and deleting companies, contacts, and users.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer commands for the oo CLI could execute changing remote code on a user's machine.

Mitigation: Install only after trusting OOMOL and verifying the installer through an official signed package or checksum when available.

Risk: Write and destructive actions can create, update, or delete Upsales data.

Mitigation: Require explicit user confirmation of the target, payload, and intended effect before running write or destructive actions.

## Reference(s):

- [ClawHub Upsales Skill Page](https://clawhub.ai/oomol/skills/oo-upsales)
- [Upsales Homepage](https://www.upsales.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing payloads; changing Upsales actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
