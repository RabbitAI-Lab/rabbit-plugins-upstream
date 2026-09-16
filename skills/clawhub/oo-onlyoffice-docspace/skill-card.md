## Description:

Helps agents search and read ONLYOFFICE DocSpace account, room, folder, and user data through OOMOL's oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect ONLYOFFICE DocSpace users, rooms, folders, and current-account data through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes one-line remote installer commands for the oo CLI.

Mitigation: Review the installer source first or use a verified, version-pinned installation method before running setup commands.

Risk: Future connector actions may write, overwrite, or remove ONLYOFFICE DocSpace data.

Mitigation: Keep execution to the listed read actions unless a write or destructive action is explicitly confirmed with the exact payload and expected effect.

Risk: Connector payloads can become invalid if the live action schema changes.

Mitigation: Inspect the current action schema before constructing or running each payload.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-onlyoffice-docspace)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ONLYOFFICE DocSpace](https://www.onlyoffice.com/docspace.aspx)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return JSON data from ONLYOFFICE DocSpace connector actions when executed.]

## Skill Version(s):

1.0.2 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
