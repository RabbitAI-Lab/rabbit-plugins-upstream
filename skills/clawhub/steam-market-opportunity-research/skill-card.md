## Description:

Evaluate Steam game niches using Crawlora's game catalog, chart and player-count history, live pricing, reviews, and release news.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, product teams, and market researchers use this skill to compare Steam game concepts against similar titles, activity history, pricing, reviews, release news, and positioning evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends user-selected Steam research queries, app IDs, regions, filters, and a Crawlora API key to Crawlora.

Mitigation: Treat CRAWLORA_API_KEY as a secret, keep it in environment configuration, and avoid sharing outputs that expose sensitive research queries or account details.

Risk: SteamSpy owner ranges, chart entries, review samples, and concurrent-player data can be mistaken for audited sales, retention, or revenue evidence.

Mitigation: Keep observed metrics, third-party estimates, and commercial hypotheses separate, and add validation steps for each opportunity hypothesis.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/steam-market-opportunity-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands and evidence-backed analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include comparable-title tables, activity series, pricing notes, review themes, positioning gaps, conflicting evidence, and validation steps.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
