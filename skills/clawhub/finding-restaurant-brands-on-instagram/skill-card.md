## Description:

Discovers restaurant brands, food businesses, and hospitality accounts on Instagram using apidojo's Instagram Scraper on Apify, returning account handles, follower counts, bios, post counts, and engagement data for prospecting and outreach.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External sales, marketing, and business development users use this skill to find and rank restaurant, cafe, food business, and hospitality Instagram accounts for B2B prospecting. It supports discovery by Instagram profile, hashtag, or location URL and helps prioritize accounts using follower, engagement, bio, and activity signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Instagram and Apify data collection may implicate platform terms, privacy law, and anti-spam or marketing rules.

Mitigation: Confirm compliance before use, collect only necessary public business information, set reasonable maxItems limits, and avoid processing personal or sensitive data unless there is a lawful basis.

Risk: Broad hashtags and mixed consumer accounts can produce irrelevant or misleading prospect lists.

Mitigation: Use niche restaurant or food-business tags, filter for business signals such as websites or phone details, require minimum follower and post thresholds, and deduplicate by username.

Risk: Private accounts or accounts with limited visible metadata can lead to incomplete rankings.

Mitigation: Skip private accounts without usable post data and treat missing engagement or bio fields as low-confidence signals during scoring.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/finding-restaurant-brands-on-instagram)
- [Apify Instagram Scraper run endpoint](https://api.apify.com/v2/acts/apidojo~instagram-scraper/runs)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with command examples, API request examples, scoring guidance, and optional CSV or JSON result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce ranked prospect lists with handles, follower counts, bios, post counts, engagement data, score tiers, and deduplication guidance.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
