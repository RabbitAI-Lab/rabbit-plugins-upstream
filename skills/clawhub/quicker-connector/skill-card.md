## Description:

Connects an AI assistant to Quicker to find and run local actions, inspect CSV or database action lists, and manage exported Quicker settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[awamwang](https://clawhub.ai/user/awamwang)

### License/Terms of Use:

MIT

## Use Case:

Quicker users and developers use this skill to search and execute Windows automations, export action lists and icons, and inspect or edit backed-up Quicker configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local Quicker actions can execute commands or change the user's environment.

Mitigation: Require explicit confirmation before execution and review third-party actions before importing or running them.

Risk: Maintenance features can modify backed-up Quicker settings and exports.

Mitigation: Confirm intended changes and keep a backup before editing configuration.

Risk: Icon retrieval may download images from remote URLs.

Mitigation: Disable or restrict icon URL downloads on restricted networks.

Risk: Stored Quicker push credentials may expose access if mishandled.

Mitigation: Avoid storing push credentials unless needed.

## Reference(s):

- [Quicker documentation: basic tools settings](https://getquicker.net/KC/Manual/Doc/settings-BasicToolsSettingPage)
- [OpenClaw documentation](https://docs.openclaw.ai)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance, Files]

**Output Format:** [Markdown guidance and commands; JSON, CSV, XLSX, or PNG exports when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Windows and a local Quicker installation for action execution.]

## Skill Version(s):

1.5.0 (source: frontmatter, release metadata, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
