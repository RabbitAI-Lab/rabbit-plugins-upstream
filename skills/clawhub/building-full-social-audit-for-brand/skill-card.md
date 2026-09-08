## Description:

Guides an agent through a brand social-media audit workflow using Apify, with concrete execution steps centered on apidojo's Twitter user scraper.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

Social media managers, brand strategists, and agency teams use this skill to request a brand or competitor audit, collect social-platform data through Apify, classify results, and summarize engagement and brand-health signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill claims broad multi-platform audit coverage, but the concrete workflow and commands are centered on the Twitter user scraper.

Mitigation: Treat the release as Twitter-focused unless platform-specific Instagram, TikTok, and YouTube execution steps are added and reviewed.

Risk: The REST fallback places APIFY_TOKEN in request URLs, which can expose credentials through command history, logs, or monitoring systems.

Mitigation: Use environment-based authentication or an approved Apify MCP/server-side runner, and avoid commands that include APIFY_TOKEN in URLs.

Risk: The skill sends brand handles and retrieves scraped social-media data through Apify.

Mitigation: Use only with data that is appropriate to process through Apify, and review applicable platform, privacy, and organizational data-handling requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/building-full-social-audit-for-brand)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, API Calls, Analysis, Files]

**Output Format:** [Markdown report with tables, summaries, and optional CSV or JSON result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Apify actor calls that retrieve scraped social-media profile data.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
