## Description:

Evaluates data-source availability, quality, cost, and compliance, then produces a data acquisition strategy for product teams.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shiyan521](https://clawhub.ai/user/shiyan521)

### License/Terms of Use:

MIT-0

## Use Case:

Product builders, developers, and strategy teams use this skill to assess required data sources and plan compliant acquisition through APIs, third-party purchase, UGC, manual collection, or permitted crawling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crawler planning may encourage anti-scraping bypass recommendations.

Mitigation: Constrain use to lawful, permission-based collection and explicitly reject bypassing CAPTCHAs, authentication, IP blocks, rate limits, or other site protections.

Risk: Data-source recommendations may understate compliance or reliability issues.

Mitigation: Require review of licensing, privacy, terms of service, and source reliability before collection.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/shiyan521/skills/06-data-source-evaluator)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown data strategy document]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Names the final deliverable as `{product name}-data strategy.md` and includes source reliability, compliance, and collection efficiency estimates.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
