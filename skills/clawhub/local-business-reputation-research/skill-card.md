## Description:

Researches public local-business profiles, ratings, reviews, complaints, scam-report patterns, menus, and photos across Yelp, BBB, Trustpilot, and OpenTable using the Crawlora API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

People evaluating local vendors or restaurants use this skill to compare public reputation signals and produce source-linked briefs, including bounded summaries of reported scam patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search details are sent to Crawlora as an intermediary service.

Mitigation: Use only public business information; do not provide secrets, private customer records, or sensitive personal data.

Risk: Public reviews and complaint narratives may identify individuals or contain unverified allegations.

Mitigation: Minimize identifying details and present allegations as reports, with source links and sampling limitations.

## Reference(s):

- [Skill endpoint reference](reference/endpoints.md)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/local-business-reputation-research)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown reputation brief with source links and selected excerpts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Separates sources, distinguishes reported allegations from verified facts, and notes sampling limits.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
