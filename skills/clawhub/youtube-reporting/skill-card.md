## Description:

Helps agents manage YouTube Reporting jobs and download bulk channel or playlist analytics reports through a Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

YouTube channel owners and their agents use this skill to list report types, schedule or manage reporting jobs, and download daily analytics reports as CSV files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting an account lets Maton mediate access to its YouTube Reporting data.

Mitigation: Approve the connection explicitly and review the requested OAuth scopes; use only the accounts and scopes needed.

Risk: Creating or deleting reporting jobs or changing connections can affect report availability.

Mitigation: Confirm the exact job, connection, and intended effect with the user before making changes.

Risk: API-key fallback can expose a long-lived credential.

Mitigation: Prefer device-flow login through the CLI; use the API key only when the CLI cannot be installed, and never log or persist it.

Risk: Hosted functions, triggers, and destinations can continue operating after the immediate task.

Mitigation: Require explicit approval, narrowly scope the automation, and remove it when no longer needed.

## Reference(s):

- [YouTube Reporting skill release](https://clawhub.ai/byungkyu/skills/youtube-reporting)
- [YouTube Reporting API overview](https://developers.google.com/youtube/reporting)
- [YouTube Reporting API reference](https://developers.google.com/youtube/reporting/v1/reference/rest)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, CSV files]

**Output Format:** [Markdown guidance and downloadable CSV reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Daily reports require an authorized connection and an active reporting job.]

## Skill Version(s):

1.2.4 (source: ClawHub release metadata; skill frontmatter states 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
