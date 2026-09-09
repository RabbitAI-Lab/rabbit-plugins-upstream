## Description:

Manage Apple Calendar events from the command line on macOS, including create, update, delete, search, export, and availability workflows with JSON output for agent use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gopaljigaur](https://clawhub.ai/user/gopaljigaur)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, automation users, and agents use this skill to inspect and manage Apple Calendar events on macOS through the accli command-line tool. It supports structured calendar operations such as listing calendars, finding event IDs, creating or updating events, exporting event ranges, and checking free/busy windows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and relies on an external global npm package.

Mitigation: Install only if the npm package publisher is trusted, and review or pin the package version before use.

Risk: The macOS app responsible for execution requires Full Calendar access.

Mitigation: Grant Calendar access only to trusted local applications and revoke it when the tool is no longer needed.

Risk: Calendar update and delete operations can modify or remove real calendar data.

Mitigation: Use --dry-run before updates or deletes, prefer stable calendar IDs, and verify target event IDs before proceeding.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gopaljigaur/skills/accli-plus)
- [npm Package: @gopaljigaur/accli](https://www.npmjs.com/package/@gopaljigaur/accli)
- [Publisher Profile](https://clawhub.ai/user/gopaljigaur)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON response expectations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Most accli commands support --json for structured output; update and delete support --dry-run previews.]

## Skill Version(s):

1.2.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
