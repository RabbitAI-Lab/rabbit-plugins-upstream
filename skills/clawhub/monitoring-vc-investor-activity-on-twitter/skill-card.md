## Description:

Monitors VC investor activity and deal signals on Twitter using apidojo's Tweet scraper.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

Startup founders, co-investors, and startup ecosystem analysts use this skill to identify and rank VC investors showing sector interest, investment thesis signals, portfolio activity, and deal flow indicators on Twitter/X.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: APIFY_TOKEN can be exposed through URLs, shell history, or shared logs.

Mitigation: Store APIFY_TOKEN as a secret and prefer MCP, SDK, or header-based authentication over token-bearing URLs.

Risk: Unbounded Twitter/X scraping can increase cost and data volume.

Mitigation: Set reasonable maxItems limits and narrow search terms before running the actor.

Risk: The workflow depends on Apify-based Twitter/X scraping.

Mitigation: Install and run the skill only when Apify use and Twitter/X data collection are acceptable for the intended environment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/apidojo-io/skills/monitoring-vc-investor-activity-on-twitter)
- [Apify Tweet Scraper Actor](https://apify.com/apidojo/tweet-scraper)
- [Apify Twitter User Scraper Actor](https://apify.com/apidojo/twitter-user-scraper)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown table and summary with optional shell commands and JSON or CSV result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires APIFY_TOKEN; maxItems limits should be set to control cost and data volume.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
