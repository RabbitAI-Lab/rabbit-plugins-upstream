## Description:

Helps agents retrieve Google Analytics reports and, with explicit approval, manage accounts, properties, and data streams through a Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and developers use this skill to summarize GA4 traffic and conversion reports, or to make explicitly approved changes to Analytics configuration. It also describes optional scheduled or event-driven automations using a connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Granting the connection access exposes Google Analytics data through Maton.

Mitigation: Authorize the connection only with user approval and prefer the read-only Data API for reporting.

Risk: Admin API changes can alter accounts, properties, or data streams.

Mitigation: Confirm the exact account or property identifier and obtain explicit approval before each change.

Risk: Hosted functions, triggers, or destinations may continue running or forwarding events after setup.

Mitigation: Review their actions and destinations before enabling them, and check ongoing automations after setup.

## Reference(s):

- [ClawHub Google Analytics skill](https://clawhub.ai/byungkyu/skills/google-analytics)
- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Google Analytics Data API](https://developers.google.com/analytics/devguides/reporting/data/v1)
- [Google Analytics Admin API](https://developers.google.com/analytics/devguides/config/admin/v1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with report summaries, API examples, and command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report output may contain visitor data; administrative changes require explicit approval.]

## Skill Version(s):

1.2.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
