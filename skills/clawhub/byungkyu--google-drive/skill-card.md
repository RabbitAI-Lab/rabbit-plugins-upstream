## Description:

Helps agents find, read, upload, share, and organize files and folders in a user's connected Google Drive.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams use this skill to find and manage files and folders in their own connected Google Drive, including downloads, uploads, and sharing. It also documents optional hosted functions and triggers for approved automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting Google Drive grants access to sensitive files within the authorized account.

Mitigation: Confirm account authorization and prefer read-only, least-privilege scopes when possible.

Risk: Uploads, edits, sharing, and deletions can expose or change files.

Mitigation: Confirm the target and effect of every write, share, or delete before execution.

Risk: API keys and hosted functions or triggers can enable persistent access or recurring actions.

Mitigation: Prefer the OAuth CLI over API-key mode, and review and separately approve any hosted automation before enabling it.

## Reference(s):

- [Google Drive skill release](https://clawhub.ai/byungkyu/skills/google-drive)
- [Maton](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Google Drive API overview](https://developers.google.com/drive/api/reference/rest/v3)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include file metadata and downloaded or exported file contents.]

## Skill Version(s):

1.2.10 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
