## Description:

YouTube Reporting API integration with managed OAuth for scheduling and downloading bulk YouTube Analytics reports as CSV files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect a YouTube Reporting account through Maton, list report types, create or remove reporting jobs with approval, and download generated daily CSV reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can connect to a user's YouTube Reporting account through OAuth or an API key.

Mitigation: Install only when the user intends to connect YouTube Reporting through Maton, review OAuth scopes, and prefer OAuth with stored credentials over exposing API keys.

Risk: Reporting jobs, hosted functions, triggers, and destinations can create persistent automation.

Mitigation: Confirm the exact account, connection, operation, destination, and persistence with the user before writes, and clean up functions, triggers, destinations, and unused connections when they are no longer needed.

Risk: Generated reports and trigger payloads may contain business data or personal data.

Mitigation: Default to read and list operations, extract only fields needed for the task, avoid logging raw responses, and keep destinations on Maton-controlled hosts unless the user explicitly approves a third-party host.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/youtube-reporting)
- [Maton homepage](https://maton.ai)
- [YouTube Reporting API Overview](https://developers.google.com/youtube/reporting)
- [YouTube Reporting API Reference](https://developers.google.com/youtube/reporting/v1/reference/rest)
- [Bulk Reports](https://developers.google.com/youtube/reporting/v1/reports)
- [Report Types](https://developers.google.com/youtube/reporting/v1/reports/full_report_list)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time trigger catalog](references/time/triggers.md)
- [Google Mail trigger catalog](references/google-mail/triggers.md)
- [GitHub trigger catalog](references/github/triggers.md)
- [Slack trigger catalog](references/slack/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide authenticated API calls that return JSON metadata or CSV report downloads through the user's Maton connection.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
