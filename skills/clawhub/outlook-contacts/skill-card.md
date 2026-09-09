## Description:

Read and write the signed-in user's Microsoft 365 or Outlook.com personal contacts through Microsoft Graph without accessing mail, files, or directory data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guoxh](https://clawhub.ai/user/guoxh)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to list, search, create, update, and delete the signed-in user's personal Outlook or Microsoft 365 contacts after device-code authorization. It is suited for finding phone numbers, looking up email addresses, and maintaining contact records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can receive persistent read/write access to personal Outlook or Microsoft 365 contacts.

Mitigation: Install only when that access is acceptable, clear stored tokens with scripts/token.sh clear --yes-i-really-mean-it, or revoke the Microsoft app consent when access is no longer needed.

Risk: Stored contact tokens or configuration could expose contact access if copied into backups, repositories, or shared locations.

Mitigation: Keep ~/.outlook-contacts out of backups and repositories, preserve restrictive file permissions, and avoid sharing the token store.

Risk: Create, update, or delete operations can change personal contact records.

Mitigation: Review dry-run payloads before using --apply; delete operations show the contact first and require explicit confirmation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/guoxh/skills/outlook-contacts)
- [Microsoft Graph endpoint](https://graph.microsoft.com)
- [Microsoft identity platform endpoint](https://login.microsoftonline.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, json]

**Output Format:** [Markdown guidance with shell command examples; scripts return summary text or JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write operations default to dry-run. Token and config files are stored under ~/.outlook-contacts/.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
