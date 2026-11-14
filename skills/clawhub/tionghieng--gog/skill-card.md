## Description:

Google Workspace CLI for Gmail, Calendar, Drive, Contacts, Sheets, and Docs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tionghieng](https://clawhub.ai/user/tionghieng)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and Google Workspace users use this skill to set up OAuth and run gog commands for Gmail, Calendar, Drive, Contacts, Sheets, and Docs from an agent-assisted terminal workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Granting gog broad Google Workspace OAuth scopes can expose Gmail, Drive, Calendar, Contacts, Sheets, Docs, or Calendar data.

Mitigation: Authorize only the Google services needed for the workflow, review OAuth consent carefully, and remove access when it is no longer required.

Risk: Generated commands can change external Google Workspace data, including sending mail, updating sheets, clearing ranges, or creating calendar events.

Mitigation: Inspect write commands before execution, prefer scripting-safe JSON output where applicable, and require confirmation for destructive or externally visible actions.

Risk: The workflow depends on installing a third-party CLI through a Homebrew tap.

Mitigation: Verify the Homebrew tap and upstream gog project before installation, and pin or review versions in controlled environments.

## Reference(s):

- [Gog homepage](https://gogcli.sh)
- [ClawHub skill page](https://clawhub.ai/tionghieng/skills/gog)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may use JSON output for scripting; OAuth credentials and account selection are configured outside the skill.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
