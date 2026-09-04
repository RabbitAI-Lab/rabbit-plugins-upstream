## Description:

YouTube Reporting helps agents schedule and download bulk YouTube Analytics reports as CSV files through Maton-managed OAuth.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to list YouTube Reporting report types, manage reporting jobs, and download generated CSV analytics reports for a connected YouTube channel or playlist.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or delete YouTube Reporting jobs for the connected account.

Mitigation: Approve only the specific job creation or deletion action requested, and confirm the target connection, report type, and intended effect before write operations.

Risk: Using the wrong Maton or YouTube Reporting connection could expose or modify data for the wrong account.

Mitigation: Use OAuth where possible and specify the intended connection when multiple accounts exist.

Risk: Downloaded reports may contain sensitive YouTube analytics data.

Mitigation: Grant access only to the relevant YouTube Reporting account and handle downloaded CSV reports according to the user's data handling requirements.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/youtube-reporting)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [YouTube Reporting API Overview](https://developers.google.com/youtube/reporting)
- [YouTube Reporting API Reference](https://developers.google.com/youtube/reporting/v1/reference/rest)
- [YouTube Reporting Bulk Reports](https://developers.google.com/youtube/reporting/v1/reports)
- [YouTube Reporting Report Types](https://developers.google.com/youtube/reporting/v1/reports/full_report_list)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Maton CLI and SDK guidance for YouTube Reporting API calls; downloaded report content is CSV.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
