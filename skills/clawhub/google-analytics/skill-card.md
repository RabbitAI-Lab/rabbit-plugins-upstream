## Description:

Access Google Analytics through Maton managed OAuth for Admin API configuration tasks and Data API reporting, with read/list defaults and explicit approval before writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect a Maton-authenticated Google Analytics account, run GA reporting queries, and perform explicitly approved Admin API configuration changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Admin API calls can create, update, or delete Google Analytics accounts, properties, and data streams.

Mitigation: Prefer the read-only Data API for reporting and require explicit user approval with exact account, property, stream, or connection identifiers before any write.

Risk: Maton authorization can expose the connected Google Analytics account within the scopes the user grants.

Mitigation: Use OAuth where possible, select the narrowest available scopes, confirm the intended account and property before use, and avoid printing or persisting credentials such as MATON_API_KEY.

Risk: Persistent functions, triggers, destinations, or unused connections can continue accessing or forwarding data after the immediate task.

Mitigation: Deploy only user-reviewed automation, prefer DENY_ALL network policy for functions, minimize forwarded payload fields, and review or delete persistent resources when the task is complete.

Risk: Google Analytics responses may include business-sensitive analytics data or personal data.

Mitigation: Return only the fields needed for the user's request and avoid writing raw responses to logs, files, or shared destinations unless the user asked for that storage.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/google-analytics)
- [Maton homepage](https://maton.ai)
- [Maton docs](https://docs.maton.ai)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Google Analytics Admin API overview](https://developers.google.com/analytics/devguides/config/admin/v1)
- [Google Analytics Data API overview](https://developers.google.com/analytics/devguides/reporting/data/v1)
- [Run Report API](https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/properties/runReport)
- [Realtime Report API](https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/properties/runRealtimeReport)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown with inline shell and code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Google Analytics API response excerpts; output should be limited to fields needed for the user's task.]

## Skill Version(s):

1.2.6 (source: server release evidence; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
