## Description:

Analyzes U.S. stocks through quick data workflows or a structured investment committee using a shared evidence ledger.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use the skill to research U.S. stocks with SentiSense market data and structured, multi-perspective analysis. Its outputs are educational information, not personalized investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company searches are sent to the SentiSense data service.

Mitigation: Use the service only for searches the user intends to share with it.

Risk: Committee runs and broad screens can consume API quota.

Mitigation: Keep screens scoped to the requested universe and account for the active API plan's limits.

Risk: Delayed or preview data can leave an analysis incomplete or stale.

Mitigation: State data timestamps and preview limits, and label unavailable evidence instead of inferring from missing rows.

## Reference(s):

- [SentiSense skill and API reference](https://sentisense.ai/skill.md)
- [SentiSense API documentation: free-key sample responses](https://sentisense.ai/docs/api/#full-sample-responses-with-a-free-key)
- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/us-stocks-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Text, Markdown]

**Output Format:** [Plain-English Markdown briefs and structured investment committee analyses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Evidence-led outputs with sourced figures, freshness and preview caveats, and educational-use disclaimers.]

## Skill Version(s):

2.11.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
