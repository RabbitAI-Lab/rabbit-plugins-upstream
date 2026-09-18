## Description:

Mailercloud lets agents operate Mailercloud through the OOMOL oo CLI to read, create, update, and delete contacts, recipient lists, and custom contact properties.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to manage Mailercloud contacts, recipient lists, and contact properties through an OOMOL-connected account. It supports read actions directly and requires confirmation before write or destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users to run a remote installer in a shell without verification.

Mitigation: Review the installer path before installing; prefer verified, versioned OOMOL CLI releases and check signatures or hashes where available.

Risk: Write and destructive Mailercloud actions can change or delete contact data.

Mitigation: Inspect the live action schema and confirm the exact payload, target, and effect with the user before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-mailercloud)
- [Mailercloud Homepage](https://www.mailercloud.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas before executing actions; connector responses are JSON.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
