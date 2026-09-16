## Description:

Moxie (withmoxie.com) helps an agent search and read Moxie workspace data through an OOMOL-connected account using the oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect live Moxie connector schemas and run read/search actions for clients, contacts, projects, pipeline stages, and task stages from a connected Moxie workspace.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands in setup guidance could execute unverified code on a user's machine.

Mitigation: Review the oo CLI installation path first, prefer a verified package manager or installer, and require explicit user approval before running installer commands.

Risk: Connector actions may access workspace data from the user's connected Moxie account.

Mitigation: Inspect the live action schema before each request and keep routine use to the listed read/search actions.

Risk: Future or unlisted connector actions could change or delete Moxie data.

Mitigation: Require explicit user confirmation of the target, payload, and expected effect before running any action tagged write or destructive.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-moxie)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Moxie Homepage](https://www.withmoxie.com/)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector schema and run commands; responses include connector data and execution metadata when actions run.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
