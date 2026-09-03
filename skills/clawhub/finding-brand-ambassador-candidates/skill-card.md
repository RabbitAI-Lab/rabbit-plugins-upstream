## Description:

Finds brand ambassador candidates on Instagram and TikTok using apidojo's scrapers on Apify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External brand partnership managers, DTC brands, and ambassador program coordinators use this skill to find creators who already post organically about a brand or product category and rank them for potential ambassador outreach.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Apify token exposure through shared logs, transcripts, or token-bearing curl URLs.

Mitigation: Set APIFY_TOKEN through a secure environment or secret manager, avoid pasting token-bearing commands into shared contexts, and prefer the MCP/helper workflow or authorization-header pattern.

Risk: Brand, hashtag, and creator research inputs are sent to Apify scrapers.

Mitigation: Submit only research data the user is permitted to share with Apify and follow the organization's data-handling rules.

Risk: Candidate rankings may misclassify creators because the skill relies on scraped social signals and heuristic scoring.

Mitigation: Review source posts, engagement signals, and sponsorship context before outreach or program decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/finding-brand-ambassador-candidates)
- [Apify actor: apidojo/instagram-scraper](https://apify.com/apidojo/instagram-scraper)
- [Apify actor: apidojo/tiktok-scraper](https://apify.com/apidojo/tiktok-scraper)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, JSON, Guidance]

**Output Format:** [Markdown report with ranked tables, inline shell commands, and optional JSON or CSV artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires APIFY_TOKEN and sends brand, hashtag, and creator research inputs to Apify.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
