## Description:

YouTube Reporting API integration with managed OAuth for scheduling and downloading bulk YouTube Analytics reports as CSV files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to connect to YouTube Reporting through Maton, list report types, manage reporting jobs, and retrieve daily CSV analytics reports for an authorized YouTube channel.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill routes YouTube Reporting access through Maton and requires trust in Maton as the gateway and package publisher.

Mitigation: Confirm trust in Maton before installation, use reviewed pinned client versions, and avoid unverified upgrades.

Risk: API keys and raw HTTP usage can expose long-lived credentials if handled broadly.

Mitigation: Prefer OAuth login, store credentials in the operating system credential store, send Maton API keys only to api.maton.ai, and avoid exporting keys into child-process environments.

Risk: Reporting jobs, functions, triggers, and destinations can create or delete resources or establish persistent automation.

Mitigation: Require explicit user confirmation for connection creation, job creation or deletion, hosted function actions, trigger setup, and destination changes; disclose scope, destination host, and persistence before execution.

Risk: Broad connections or trigger destinations may expose analytics data or third-party event payloads beyond the intended task.

Mitigation: Keep connections scoped to the needed YouTube account, prefer read/list operations first, minimize forwarded payload fields, and remove unused connections, functions, triggers, or destinations when work is complete.

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

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, markdown]

**Output Format:** [Markdown with bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent-facing instructions for authenticated Maton CLI, raw HTTP, and SDK workflows; downloaded reports are CSV files returned by the YouTube Reporting API.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
