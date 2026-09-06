## Description:

Finds gaming content creators on TikTok and YouTube using apidojo's scrapers on Apify and returns creator handles, platform metrics, game focus, and engagement signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External teams, brands, agencies, game publishers, and esports organizations use this skill to discover and prioritize gaming creators for sponsorship, outreach, and partnership campaigns by game, genre, region, and creator stage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an Apify token and networked scraper actors to collect creator data.

Mitigation: Run it only in environments where Apify token use is approved, keep the token out of shared outputs, and review actor inputs before execution.

Risk: Exported creator lists may contain contact, engagement, or targeting data that requires responsible handling.

Mitigation: Choose export paths deliberately, restrict access to saved CSV or JSON files, and handle creator data according to the campaign team's privacy and compliance requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/finding-gaming-content-creators)
- [API Dojo ClawHub profile](https://clawhub.ai/user/apidojo-io)
- [TikTok scraper actor run endpoint](https://api.apify.com/v2/acts/apidojo~tiktok-scraper/runs?token=$APIFY_TOKEN)
- [YouTube scraper actor run endpoint](https://api.apify.com/v2/acts/apidojo~youtube-scraper/runs?token=$APIFY_TOKEN)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with tables and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May optionally save Apify results as CSV or JSON files when the user requests an export.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact metadata version 1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
