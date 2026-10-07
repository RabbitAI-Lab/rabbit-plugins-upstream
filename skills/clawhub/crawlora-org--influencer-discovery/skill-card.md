## Description:

Find and shortlist TikTok, Instagram, YouTube, and Substack creators for campaigns using Crawlora creator datasets and public profile and content data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams and campaign planners use this skill to discover, compare, and shortlist creators and newsletter publishers using public profile and sampled content evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Campaign searches and creator lookup parameters are sent to Crawlora.

Mitigation: Use the skill only when sharing those queries with Crawlora is acceptable.

Risk: The API credential or retrieved contact emails could be disclosed or misused.

Mitigation: Keep CRAWLORA_API_KEY private and request contact emails only for legitimate outreach.

Risk: Stale profiles and incomplete audience signals can lead to misleading campaign choices.

Mitigation: Review public profile data, mark missing signals as unknown, and distinguish refreshed observations from dataset-only results.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/influencer-discovery)
- [Crawlora endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Text, Markdown, CSV]

**Output Format:** [Shortlist table or CSV with evidence and links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes platform identifiers, public audience signals, content samples, retrieval or refresh status, and campaign-fit rationale.]

## Skill Version(s):

1.0.13 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
