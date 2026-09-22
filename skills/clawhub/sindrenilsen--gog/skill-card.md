## Description:

Google Workspace CLI for Gmail, Calendar, Drive, Contacts, Sheets, and Docs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sindrenilsen](https://clawhub.ai/user/sindrenilsen)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Google Workspace users use Gog to have an agent prepare setup steps and CLI commands for Gmail, Calendar, Drive, Contacts, Sheets, and Docs workflows. The skill is most useful for account automation tasks where commands should be reviewed before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OAuth authorization can grant broad access across Gmail, Calendar, Drive, Contacts, Sheets, and Docs.

Mitigation: Authorize only the Google services required for the current task and review account selection before running commands.

Risk: Some generated commands can change account data, including sending Gmail messages, creating calendar events, and updating, appending, or clearing Sheets data.

Mitigation: Confirm commands before execution, especially write operations, and use non-interactive scripting only after reviewing the exact command and target account.

Risk: The workflow depends on a third-party CLI and Homebrew tap.

Mitigation: Install only when the gog CLI and the referenced Homebrew tap are trusted for the environment.

## Reference(s):

- [Gog homepage](https://gogcli.sh)
- [ClawHub skill page](https://clawhub.ai/sindrenilsen/skills/gog)
- [ClawHub publisher profile](https://clawhub.ai/user/sindrenilsen)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May recommend JSON-oriented gog CLI usage for scripting; produced commands can read or modify Google Workspace account data depending on the selected service and command.]

## Skill Version(s):

1.0.0 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
