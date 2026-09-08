## Description:

Builds targeted B2B prospect lists from Twitter/X profiles and posts using apidojo's Twitter scrapers on Apify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External sales, growth, founder-led sales, and partnership teams use this skill to find and rank Twitter/X accounts that match an ideal customer profile for outreach. It helps collect profile, follower, location, bio, and recent tweet context for prospect lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill automates collection and export of identifiable Twitter/X prospect data.

Mitigation: Use it only where X/Twitter scraping, prospecting, and third-party Apify processing are permitted by organizational policy, platform terms, and applicable privacy obligations.

Risk: Prospecting filters could target sensitive categories or create overly broad exports.

Mitigation: Set list-size limits, avoid sensitive-category targeting, and review ICP filters before running collection.

Risk: Exported prospect files can create retention and access-control exposure.

Mitigation: Store exports only in approved locations and delete prospect files according to a defined retention policy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/building-twitter-prospect-lists)
- [API Dojo publisher profile](https://clawhub.ai/user/apidojo-io)
- [Apify tweet-scraper actor API endpoint](https://api.apify.com/v2/acts/apidojo~tweet-scraper/runs)
- [Apify twitter-user-scraper actor API endpoint](https://api.apify.com/v2/acts/apidojo~twitter-user-scraper/runs)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown prospect list with tables, notes, and optional CSV or JSON exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes identifiable Twitter/X profile data, follower counts, location fields, profile links, and recent tweet samples when available.]

## Skill Version(s):

1.0.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
