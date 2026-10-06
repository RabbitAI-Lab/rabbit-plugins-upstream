## Description:

Compares indexed television coverage across stations and shows using Crawlora GDELT TV search, charts, timelines, and discovery while distinguishing match channels, coverage windows, and metric denominators.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and analysts use this skill to compare a topic's indexed television coverage across stations and shows, with query and coverage ledgers, metric-specific summaries, and attributed samples.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms are sent to Crawlora and may contain sensitive information.

Mitigation: Submit only terms you are comfortable transmitting to Crawlora and set the API key deliberately.

Risk: Broad searches can consume more API credits than intended.

Mitigation: Bound queries and pages by the requested scope and credit budget.

Risk: Indexed matches and machine-extracted signals may be mistaken for verified audience exposure or comparable coverage shares.

Mitigation: Keep match channels and metric denominators distinct, label coverage and processing gaps, and attribute sampled material.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/broadcast-coverage-comparison)
- [Crawlora GDELT TV endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown brief with tables, timelines, and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes query and coverage ledgers, sampled material, and processing or coverage gaps.]

## Skill Version(s):

1.0.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
