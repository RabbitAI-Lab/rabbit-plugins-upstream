## Description:

Uses published restaurant brand store snapshots to answer questions about openings and closures, regional expansion, competitive direction, sales targeting, and initial site screening.

This skill is ready for commercial/non-commercial use.

## Publisher:

[horacetu](https://clawhub.ai/user/horacetu)

### License/Terms of Use:

MIT-0

## Use Case:

Restaurant brand market, expansion, and sales teams use this skill to analyze published store-network snapshots, compare competitors, identify regional movement, and screen a small number of sales or site candidates. It emphasizes aggregate-first analysis and only uses limited store-level details when the user explicitly asks for them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Brand, address, and location queries are sent to the external DDT restaurant-network API.

Mitigation: Use the skill only when that API use is intended, avoid sending sensitive queries, and make the external data flow clear to users.

Risk: The skill depends on a user-provided DDT_API_KEY.

Mitigation: Store the key only in a local environment variable, never display it in responses, and stop on authentication failures instead of retrying with exposed credentials.

Risk: Store-level endpoints are previews and could be misused for bulk extraction or overbroad context stuffing.

Mitigation: Keep analysis aggregate-first, honor the documented result limits, avoid automatic pagination or region splitting, and ask users to narrow requests for specific store checks.

Risk: Observed opening and closure dates may be mistaken for official brand announcements or business outcomes.

Mitigation: Report the coverage period and data definitions, and state that observed openings, closure confirmations, closure rates, and spatial density are not official opening dates, failure rates, revenue, profit, or success predictions.

## Reference(s):

- [店店通餐饮分析 Homepage](https://gotoshop-ai.com/ddtclaw/)
- [DDT API Key Portal](https://gotoshop-ai.com/ddtclaw/open)
- [ClawHub Skill Page](https://clawhub.ai/horacetu/skills/ddtclaw-competitor-watch)

## Skill Output:

**Output Type(s):** [analysis, markdown, shell commands, guidance]

**Output Format:** [Markdown with concise conclusions, key metrics, coverage notes, limited details, and occasional bash API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses aggregate API results first; store-level previews are limited and should not be expanded into bulk exports.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
