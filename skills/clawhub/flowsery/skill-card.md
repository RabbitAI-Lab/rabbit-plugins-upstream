## Description:

Openclaw Flowsery helps agents query Flowsery Analytics for website traffic, real-time visitors, trend and breakdown reports, revenue and conversion metrics, and AI-detected session issues, with documented confirmation rules for limited goal or payment writes and irreversible deletes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tarasshyn](https://clawhub.ai/user/tarasshyn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site owners, and analytics operators use this skill to let an agent answer questions about website traffic, visitor behavior, conversions, revenue, campaigns, and AI-detected user-experience issues in Flowsery-tracked sites. Direct API actions that create or delete goal and payment records require explicit user intent and confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Flowsery workspace API tokens provide access to analytics for the configured workspace.

Mitigation: Treat tokens like passwords, keep them out of logs and client-side code, and install only when the workspace access level is acceptable.

Risk: Analytics responses can include sensitive visitor, payment, location, revenue, and session-derived issue details.

Mitigation: Confirm authorization before retrieving individual-level data and return only the minimum detail needed to answer the user's question.

Risk: The documented API includes writes and irreversible deletes for goal and payment records.

Mitigation: Require explicit confirmation before delete operations, restating the website, filters, date range, and expected scope; prefer the bundled read-only OpenClaw tools for normal analytics queries.

Risk: Broad or repeated analytics queries can hit the 600 requests per minute rate limit or return excessive data.

Mitigation: Use date ranges, filters, pagination, and coarser time intervals, and honor Retry-After responses instead of retrying immediately.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/tarasshyn/skills/flowsery)
- [Flowsery](https://flowsery.com)
- [Flowsery Analytics API Reference](references/api-reference.md)
- [Breakdown Dimensions Reference](references/breakdown-dimensions.md)
- [Flowsery OpenAPI Specification](https://analytics.flowsery.com/analytics/api/v1/openapi.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API responses and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [OpenClaw plugin tools expose read-only analytics queries; API access requires a Flowsery workspace token and is rate-limited to 600 requests per minute per token.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
