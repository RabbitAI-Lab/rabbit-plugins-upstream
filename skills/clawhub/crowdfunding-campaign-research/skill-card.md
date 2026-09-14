## Description:

Compare Kickstarter campaigns through Crawlora using funding snapshots, reward tiers, creator updates, risks, and sampled backer comments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External researchers, marketers, founders, and analysts use this skill to compare Kickstarter campaign cohorts, inspect campaign details, summarize creator updates, and report sampled backer-comment themes with explicit evidence limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Campaign URLs, query terms, scrape requests, and related research inputs are sent to Crawlora under the user's Crawlora account.

Mitigation: Keep the Crawlora API key private, restrict optional web scraping to public pages relevant to the task, and bound collection sizes.

Risk: Incomplete or self-selected campaign collections can produce misleading benchmark conclusions.

Mitigation: State cohort rules, campaign states, collection bounds, and how many comments were collected versus the reported total.

Risk: Funding success, creator statements, comments, and reward delivery can be conflated into stronger claims than the evidence supports.

Mitigation: Separate funding snapshots, creator-reported milestones, sampled backer reports, and independently supported outcomes.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Kickstarter Project Basics](https://help.kickstarter.com/hc/en-us/articles/115005028514-What-are-the-basics)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/crowdfunding-campaign-research)
- [Crawlora Publisher Profile](https://clawhub.ai/user/crawlora-org)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown brief with campaign links, cohort rules, dated comparisons, sampled comment themes, disagreements, open questions, and optional shell command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include raw JSON from Crawlora API calls when useful for inspection.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
