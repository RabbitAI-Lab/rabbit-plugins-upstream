## Description:

Compare Kickstarter campaigns through Crawlora using funding snapshots, reward tiers, creator updates, risks, and sampled backer comments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Campaign researchers, creators, and analysts use this skill to benchmark Kickstarter campaigns and prepare evidence-based progress and fulfillment briefs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research queries, optional public URLs, and the Crawlora API key are sent to Crawlora.

Mitigation: Use only an authorized key and relevant public campaign evidence; do not send private or sensitive URLs or text.

Risk: Partial comment samples and missing campaign details can make funding or fulfillment conclusions misleading.

Mitigation: Report sample size and missing fields, verify snapshots across sources, and distinguish funding success from reward delivery.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/crowdfunding-campaign-research)
- [Kickstarter endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Kickstarter project basics](https://help.kickstarter.com/hc/en-us/articles/115005028514-What-are-the-basics)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown research brief with campaign links and comparisons]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes dated snapshots, cohort criteria, sampled comment counts, evidence gaps, and open questions.]

## Skill Version(s):

1.0.10 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
