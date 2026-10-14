## Description:

Queries Cue for listed-company equity incentive plans and share buybacks, and prepares sourced analyses of incentive designs and market trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Investors, analysts, and compensation teams use it to look up A-share listed-company equity incentive and buyback data, compare plans, and prepare sourced reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing a local runner from a mutable external repository may change executed code.

Mitigation: Review the runner and pin a trusted revision before installing or updating it.

Risk: Persistent AI-client configuration stores a Cue API key and sends it to Cue services.

Mitigation: Review configuration changes, limit access to the key, and rotate it if exposed in chat or logs.

Risk: Person-level executive data could be used for unwanted outreach or profiling.

Mitigation: Use executive-level details only for legitimate analysis and avoid unsolicited targeting.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/panting09266-ai/skills/cue-equity-incentive)
- [Cue API key management](https://cuecue.cn/api-key?src=clawhub-equity-incentive)
- [Cue MCP data catalog](https://cuecue.cn/api/mcp-catalog)

## Skill Output:

**Output Type(s):** [Structured data, Markdown, Text]

**Output Format:** [Tables for direct lookups; Markdown reports with source links for research questions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Direct lookups return data without a report; completed research reports link to the original Cue report.]

## Skill Version(s):

1.1.11 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
