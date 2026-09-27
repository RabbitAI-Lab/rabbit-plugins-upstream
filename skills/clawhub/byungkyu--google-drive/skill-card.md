## Description:

Google Drive API integration with managed OAuth for listing, searching, creating, sharing, uploading, downloading, and managing files and folders in a user's own Google Drive.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, developers, and agents use this skill to access a connected Google Drive account through Maton for file discovery, metadata retrieval, exports, uploads, organization, sharing, and approved automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide actions that read, write, delete, share, upload, download, or automate access to Google Drive content.

Mitigation: Install only if the user trusts Maton with the connected Google Drive account, default to read/list actions, and require explicit user approval for write, delete, share, connection, function, trigger, and destination changes.

Risk: Long-lived API keys or broad OAuth scopes can increase exposure if credentials are mishandled or over-authorized.

Mitigation: Prefer OAuth, use the minimum Google Drive scopes available for the task, avoid exporting API keys to child processes, and store credentials only through the documented Maton profile and credential-store flow.

Risk: Triggers and destinations can create ongoing data flows from the connected account.

Mitigation: Review the trigger source, destination, schedule or event type, exact target function, and expected data flow before enabling automation, and remove unused functions or triggers after the task is complete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/google-drive)
- [Publisher profile](https://clawhub.ai/user/byungkyu)
- [Maton homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Google Drive API Overview](https://developers.google.com/drive/api/reference/rest/v3)
- [Google Drive Files: list](https://developers.google.com/drive/api/reference/rest/v3/files/list)
- [Google Drive Files: get](https://developers.google.com/drive/api/reference/rest/v3/files/get)
- [Google Drive Files: create](https://developers.google.com/drive/api/reference/rest/v3/files/create)
- [Google Drive Files: update](https://developers.google.com/drive/api/reference/rest/v3/files/update)
- [Google Drive Files: delete](https://developers.google.com/drive/api/reference/rest/v3/files/delete)
- [Google Drive Files: export](https://developers.google.com/drive/api/reference/rest/v3/files/export)
- [Google Drive uploads](https://developers.google.com/drive/api/guides/manage-uploads)
- [Google Drive search syntax](https://developers.google.com/drive/api/guides/search-files)
- [Time Trigger Reference](artifact/references/time/triggers.md)
- [Gmail Trigger Reference](artifact/references/google-mail/triggers.md)
- [GitHub Trigger Reference](artifact/references/github/triggers.md)
- [Slack Trigger Reference](artifact/references/slack/triggers.md)
- [Stripe Trigger Reference](artifact/references/stripe/triggers.md)
- [HubSpot Trigger Reference](artifact/references/hubspot/triggers.md)
- [Linear Trigger Reference](artifact/references/linear/triggers.md)
- [Notion Trigger Reference](artifact/references/notion/triggers.md)
- [Calendly Trigger Reference](artifact/references/calendly/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, Python snippets, configuration notes, and API call patterns.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include proposed Maton CLI commands, raw HTTP forms, OAuth connection steps, hosted function examples, trigger setup guidance, and Google Drive API request examples.]

## Skill Version(s):

1.2.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
