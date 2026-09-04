## Description:

Helps agents use Apify actors to fetch TikTok videos, profiles, hashtags, music, comments, and location-based posts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and automation agents use this skill to configure Apify-based TikTok scraping workflows for posts, profiles, comments, hashtags, music, search, and location feeds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An Apify API token could be exposed in logs, shared chats, shell history, or committed files.

Mitigation: Treat APIFY_TOKEN as a secret, use environment variables or secret storage, and avoid pasting real tokens into shared outputs.

Risk: TikTok URLs, keywords, run metadata, and scraped results may be processed or retained by Apify.

Mitigation: Use the skill only when third-party processing by Apify is acceptable for the data being submitted and collected.

Risk: API calls may fail or return limited data without a paid Apify plan.

Mitigation: Confirm the Apify account plan before running production scraping workflows.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/apidojo-io/skills/tiktok-scraper)
- [Apify Account](https://apify.com/?fpr=yhdrb)
- [Apify Pricing](https://apify.com/pricing?fpr=yhdrb)
- [Apify API Token Settings](https://console.apify.com/account/integrations)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration, API Calls]

**Output Format:** [Markdown with shell commands, code examples, and JSON response shapes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an Apify API token and a paid Apify plan for real data.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
