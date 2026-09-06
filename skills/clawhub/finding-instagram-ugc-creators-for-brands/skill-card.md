## Description:

Finds Instagram UGC creators for brand campaigns using apidojo's Instagram scraper on Apify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External brand, e-commerce, and influencer marketing teams use this skill to discover, enrich, and score Instagram nano and micro UGC creators for product campaigns, paid partnerships, or product seeding.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses Apify with an APIFY_TOKEN for Instagram scraping.

Mitigation: Confirm the Apify dependency and token handling are acceptable before installation, and avoid exposing tokens in shared commands, logs, or exported files.

Risk: Exported creator lists can contain third-party Instagram profile data.

Mitigation: Store and share creator exports carefully and handle them in line with applicable platform terms and privacy requirements.

Risk: Private accounts cannot be assessed for content quality.

Mitigation: Skip private accounts or mark them out of scope instead of estimating creator fit from unavailable profile content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/finding-instagram-ugc-creators-for-brands)
- [Apify Instagram scraper actor](https://apify.com/apidojo/instagram-scraper)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with tables and inline shell, REST API, and MCP examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce creator lists with handles, follower counts, engagement metrics, niche hashtags, bio links, and UGC fit tiers.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
