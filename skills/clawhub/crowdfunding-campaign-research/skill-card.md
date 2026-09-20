## Description:

Compare Kickstarter campaigns through Crawlora using funding snapshots, reward tiers, creator updates, risks, and sampled backer comments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to benchmark Kickstarter campaigns, compare funding and reward evidence, and prepare progress or fulfillment research briefs. It helps preserve lifecycle stage, currency, sample-size limits, and source uncertainty when reviewing campaign data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Campaign search terms, Kickstarter project identifiers, optional public scrape URLs, and the Crawlora API key are sent to Crawlora.

Mitigation: Use the skill only for user-requested campaign research, keep the API key in the environment, and avoid submitting private or sensitive URLs.

Risk: Kickstarter discovery and comment data can be incomplete, sampled, or biased by lifecycle filters and editorial selection.

Mitigation: State cohort rules, lifecycle filters, collection limits, and collected-versus-reported comment counts in the resulting brief.

## Reference(s):

- [Crowdfunding Campaign Research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Kickstarter project basics](https://help.kickstarter.com/hc/en-us/articles/115005028514-What-are-the-basics)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/crowdfunding-campaign-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown research briefs with inline shell commands and cited campaign evidence]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include campaign links, cohort rules, dated comparisons, update milestones, sampled comment themes, disagreements, and open questions.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
