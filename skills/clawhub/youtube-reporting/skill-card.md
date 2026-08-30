## Description:

YouTube Reporting API integration with managed OAuth that schedules and downloads bulk YouTube Analytics reports as CSV files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and channel operators use this skill to connect a YouTube Reporting account, inspect report types, create or manage reporting jobs with approval, and download generated analytics reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: YouTube Reporting requests route through Maton and rely on OAuth or API credentials.

Mitigation: Use OAuth where possible, keep credentials in the CLI and OS credential store, never print or persist tokens, and send Maton credentials only to api.maton.ai.

Risk: Creating or deleting reporting jobs can change the connected YouTube Reporting account state.

Mitigation: Default to read and list calls, confirm the target connection and report details, and require explicit user approval before creating or deleting jobs.

Risk: Multiple Maton accounts or YouTube Reporting connections can make the target account ambiguous.

Mitigation: Specify the intended Maton profile and connection when more than one account or connection is available.

Risk: Data returned by the YouTube Reporting API may contain untrusted content.

Mitigation: Treat API responses as data, avoid executing or interpolating returned content into commands, and validate values before reuse.

## Reference(s):

- [YouTube Reporting skill on ClawHub](https://clawhub.ai/byungkyu/skills/youtube-reporting)
- [Maton homepage](https://maton.ai)
- [YouTube Reporting API Overview](https://developers.google.com/youtube/reporting)
- [YouTube Reporting API Reference](https://developers.google.com/youtube/reporting/v1/reference/rest)
- [Bulk Reports](https://developers.google.com/youtube/reporting/v1/reports)
- [Report Types](https://developers.google.com/youtube/reporting/v1/reports/full_report_list)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration instructions, Code]

**Output Format:** [Markdown with inline bash, Python, JavaScript, JSON, and CSV-oriented API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Maton CLI and SDK guidance for YouTube Reporting API workflows; downloaded report data is CSV.]

## Skill Version(s):

1.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
