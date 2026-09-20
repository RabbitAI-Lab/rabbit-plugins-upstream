## Description:

Find and shortlist TikTok, Instagram, and YouTube creators for a campaign using Crawlora's creator datasets and live profile/content endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, and growth teams use this skill to source public social-media creators, refresh profile and content signals, and produce an evidence-backed influencer shortlist for a campaign.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends creator search terms, profile identifiers, and the user's Crawlora API key to Crawlora.

Mitigation: Use the skill only when that data sharing is acceptable, keep the API key in the environment, and avoid exposing it in shared logs or outputs.

Risk: Returned contact details, geography, creator metrics, and content-fit signals may be incomplete or stale.

Mitigation: Verify public-data signals before outreach or business decisions, label dataset-only candidates clearly, and record sample sizes, dates, and metric definitions.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/influencer-discovery)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown tables or CSV-style shortlist with optional shell command examples and API-response summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include platform identifiers, profile URLs, topic-fit evidence, follower counts, refresh status, sampled content URLs, metric definitions, and fit rationale.]

## Skill Version(s):

1.0.9 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
