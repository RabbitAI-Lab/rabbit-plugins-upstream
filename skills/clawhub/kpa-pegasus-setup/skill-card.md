## Description:

Guides users through installing, troubleshooting, and optimizing Pegasus, RetroArch, and PPSSPP on the KONKR Pocket ADVANCE handheld; it does not provide ROM or BIOS files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

MIT

## Use Case:

KONKR Pocket ADVANCE owners and technicians use this skill to install and tune Pegasus, RetroArch, and PPSSPP, troubleshoot setup issues, and validate game-library metadata and configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marks the skill suspicious for command and download risks and behavior beyond its stated setup purpose; its coverage is incomplete, so unreported behavior is not established as safe.

Mitigation: Review the scripts and fetched content before running them, start with the documented --dry-run mode, and proceed only if comfortable with the scanner-reported risks.

Risk: Setup scripts can change configuration on a connected handheld, and deleting ROM or CHD files can be irreversible.

Mitigation: Keep the documented rollback copies, review the planned changes, and make a separate backup before any game-file deletion.

## Reference(s):

- [Installation guide](INSTALL.md)
- [Setup and troubleshooting playbook](references/PLAYBOOK.md)
- [Safety and configuration rules](references/HARD_RULES.md)
- [Verification guide](references/VERIFICATION.md)
- [ClawHub release](https://clawhub.ai/lisong2003-lgtm/skills/kpa-pegasus-setup)
- [Publisher profile](https://clawhub.ai/user/lisong2003-lgtm)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown reports]

**Output Format:** [Markdown guidance with shell commands, configuration snippets, and verification reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include scripts that change settings on a connected handheld; hardware controls, visuals, and game launches require on-device confirmation.]

## Skill Version(s):

2.3.2 (source: server-resolved release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
