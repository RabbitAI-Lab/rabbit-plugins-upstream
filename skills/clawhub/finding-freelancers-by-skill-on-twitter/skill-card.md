## Description:

Finds freelancers and independent contractors to recruit using apidojo's Twitter scrapers on Apify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

Agencies, startup operators, recruiters, and project managers use this skill to find and prioritize freelance or independent talent on Twitter/X by skill area and availability signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sourcing queries, Twitter/X handles, and resulting public profile data are sent to Apify-powered scraping workflows.

Mitigation: Do not include confidential candidate lists, regulated personal data, or sensitive business targeting criteria unless organizational policy permits that processing.

Risk: Candidate availability and fit signals are inferred from public Twitter/X bios, tweets, and profile metrics and may be incomplete or stale.

Mitigation: Manually review candidates before outreach and verify availability, identity, and suitability using current public information.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/apidojo-io/skills/finding-freelancers-by-skill-on-twitter)
- [Apify Twitter User Scraper Actor](https://apify.com/apidojo/twitter-user-scraper)
- [Apify Tweet Scraper Actor](https://apify.com/apidojo/tweet-scraper)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown tables with candidate summaries and optional JSON or CSV files from Apify actor runs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include Twitter/X handles, names, specialties, locations, follower counts, activity, availability indicators, scores, and bio highlights.]

## Skill Version(s):

1.0.0 (source: server release evidence; artifact frontmatter metadata reports 1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
