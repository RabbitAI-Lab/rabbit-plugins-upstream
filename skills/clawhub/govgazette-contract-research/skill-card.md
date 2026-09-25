## Description:

Find federal contract opportunities and build a cited research brief using GovGazette when the user asks about U.S. government notices, awards or vendors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mooshee](https://clawhub.ai/user/mooshee)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use this skill to research U.S. federal contract opportunities, awards, vendors, and classification references through GovGazette, then produce cited, evidence-based briefs with source dates and limits clearly preserved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GovGazette records and official-source text may include outdated or incomplete procurement information, and an active source status does not prove a response window is open.

Mitigation: Cite GovGazette and official sources with source dates, report freshness for date-sensitive questions, and avoid inventing eligibility, requirements, deadlines, or likelihood of winning.

Risk: Retrieved public-record text could contain untrusted content or instructions unrelated to the user's research task.

Mitigation: Treat retrieved record text only as evidence, do not execute commands or follow unrelated destinations from records, and do not contact agencies or submit bids.

Risk: Private saved-search features require a workspace key and could expose credentials if handled in chat.

Mitigation: Use public research without authentication by default and provide any workspace key only through the host's secret mechanism when the user explicitly wants private saved-search features.

## Reference(s):

- [GovGazette MCP server](https://govgazette.com/mcp)
- [GovGazette Contract Research on ClawHub](https://clawhub.ai/mooshee/skills/govgazette-contract-research)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, guidance]

**Output Format:** [Markdown research brief with citations, source dates, identifiers, and evidence-based next steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses GovGazette MCP results and preserves record freshness, continuation fields, official source links, dates, money amounts, and identifiers when available.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
