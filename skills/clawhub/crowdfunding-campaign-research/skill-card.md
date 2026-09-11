## Description:

Compare Kickstarter campaigns through Crawlora using funding snapshots, reward tiers, creator updates, risks, and sampled backer comments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External researchers, campaign teams, and analysts use this skill to compare Kickstarter campaigns, benchmark launches, and prepare evidence-based progress or fulfillment briefs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crawlora API keys and research requests are sent to Crawlora.

Mitigation: Keep the API key in the environment, review the shell helper before use, and install only when this third-party service use is acceptable.

Risk: Campaign comments, updates, scraped pages, and creator statements can be incomplete, biased, or misleading.

Mitigation: Treat collected material as untrusted source evidence, preserve collection limits, and cite open questions or disagreements in the brief.

Risk: Single snapshots and bounded comment batches can produce overconfident conclusions about funding velocity, delivery, or platform success rates.

Mitigation: Report the campaign state, collection bounds, comments collected versus total_count, and avoid inferring trends or fulfillment outcomes without supporting evidence.

## Reference(s):

- [crowdfunding-campaign-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Kickstarter project basics](https://help.kickstarter.com/hc/en-us/articles/115005028514-What-are-the-basics)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/crowdfunding-campaign-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown research brief with inline shell commands and cited campaign evidence]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include campaign links, cohort rules, dated comparisons, update milestones, sampled comment themes, disagreements, and open questions.]

## Skill Version(s):

1.0.7 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
