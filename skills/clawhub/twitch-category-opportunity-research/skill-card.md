## Description:

Compares Twitch categories using Crawlora live snapshots and channel content to build a source-bounded streaming shortlist and content-planning brief.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and content planners compare Twitch categories and channel examples to choose streams worth testing, while preserving snapshot timing and limits on audience or revenue conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Crawlora API key and requested Twitch queries are sent to Crawlora.

Mitigation: Use a key scoped to Crawlora and avoid including unnecessary private or sensitive data in queries.

Risk: Repeated category queries may consume API credits.

Mitigation: Bound calls and page sizes to the requested scope and monitor credit usage.

Risk: Live snapshots and top-stream samples can be mistaken for complete market demand or income forecasts.

Mitigation: Report collection times, limits, and sample sizes; keep observed viewers separate from predictions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/twitch-category-opportunity-research)
- [Twitch endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown brief with snapshot ledger, comparison table, and testable content hypotheses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves source identifiers, observation times, sample sizes, and uncertainty; does not forecast audience or revenue.]

## Skill Version(s):

1.0.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
