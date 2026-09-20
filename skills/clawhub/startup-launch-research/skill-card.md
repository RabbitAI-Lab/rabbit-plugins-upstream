## Description:

Screens startup launches, public traction signals, verified revenue profiles, and crowdfunding campaigns using Product Hunt, TrustMRR, and Kickstarter through the Crawlora API. Use for launch research and acquisition screening, not investment guarantees or private diligence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and business researchers use this skill to build dated launch and market-signal briefs from public Product Hunt, TrustMRR, and Kickstarter data. It supports launch research and acquisition screening while keeping revenue, campaign, review, and ranking evidence separate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Startup research queries and target identifiers are sent to Crawlora with the user's Crawlora API key.

Mitigation: Avoid sending secrets or private diligence material in requests, and install only when third-party API use is acceptable.

Risk: Public Product Hunt, TrustMRR, and Kickstarter results can be incomplete, revised, self-reported, or only valid at collection time.

Mitigation: Preserve timestamps and source URLs, separate evidence types, and avoid treating public metrics as investment guarantees, valuation proof, or private diligence.

Risk: Broad public directory collection can create terms, consent, or policy concerns.

Mitigation: Keep collection within applicable terms and consent expectations, especially when enumerating directory or marketplace data.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora API](https://api.crawlora.net/api/v1)
- [Startup Launch Research on ClawHub](https://clawhub.ai/crawlora-org/skills/startup-launch-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown research brief with inline shell commands and JSON summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses public point-in-time source data and should preserve collection timestamps, source URLs, and evidence limits.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
