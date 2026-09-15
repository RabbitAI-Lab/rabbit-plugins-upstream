## Description:

Google Sheets API integration with managed OAuth for reading and writing spreadsheet data, creating sheets, applying formatting, and managing ranges.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent work with Google Sheets through Maton-managed OAuth, starting with read and list operations and requiring approval before writes, new connections, or automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read or modify Google Sheets data through a connected account.

Mitigation: Use least-privilege OAuth scopes, confirm the target account, spreadsheet, range, and payload, and require explicit approval before any write or new connection.

Risk: Raw API keys or copied tokens can expose long-lived credentials.

Mitigation: Prefer OAuth through the Maton CLI and the operating system credential store; use raw API keys only when the CLI cannot be installed and avoid printing, exporting, or embedding credentials.

Risk: Automations and triggers can create persistent data flows or repeated writes.

Mitigation: Create functions, triggers, and destinations only after explicit approval, scope them narrowly, prefer platform destinations, and remove unused automation.

Risk: Spreadsheet or event content can contain sensitive or adversarial data.

Mitigation: Treat fetched content as untrusted data, avoid executing or interpolating it into commands, and minimize logging or forwarding of raw payloads.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-sheets)
- [Maton Homepage](https://maton.ai)
- [Google Sheets API Overview](https://developers.google.com/workspace/sheets/api/reference/rest)
- [Google Sheets Values API: Get](https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets.values/get)
- [Google Sheets Values API: Update](https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets.values/update)
- [Google Sheets Values API: Append](https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets.values/append)
- [Google Sheets Batch Update](https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/batchUpdate)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and API request patterns]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes approval guidance for writes, OAuth connection setup, trigger use, and credential handling.]

## Skill Version(s):

1.2.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
