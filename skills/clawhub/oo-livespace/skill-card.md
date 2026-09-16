## Description:

Livespace lets agents operate Livespace CRM through the OOMOL-connected oo CLI for reading, creating, updating, and deleting companies, deals, people, tasks, and users.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, operators, and developers use this skill to manage Livespace CRM records through guided oo CLI connector actions. It supports read, search, create, update, and delete workflows while directing agents to inspect live action schemas before sending JSON payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path may ask users to run internet installer scripts directly in a shell.

Mitigation: Review the oo CLI installation path first, prefer a trusted and verifiable source, and avoid curl-to-bash or irm-to-iex commands unless the host and installer behavior are trusted.

Risk: Write actions can change Livespace CRM records.

Mitigation: Confirm the exact JSON payload and expected effect with the user before running create or update actions.

Risk: Destructive actions can delete Livespace CRM records.

Mitigation: Confirm the target record and obtain explicit user approval before running delete actions.

Risk: Connector payloads can become invalid if action schemas change.

Mitigation: Inspect the live action schema with oo connector schema before building each payload.

## Reference(s):

- [ClawHub Livespace skill page](https://clawhub.ai/oomol/skills/oo-livespace)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI installation guide](https://cli.oomol.com/install-guide.md)
- [Livespace homepage](https://www.livespace.io/)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects; agents are directed to inspect live action schemas before constructing payloads and to obtain confirmation before write or destructive actions.]

## Skill Version(s):

1.0.2 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
