## Description:

Finds trending Twitter topics and conversations for content ideation using apidojo's Twitter scrapers on Apify, returning trending topics, tweet volume signals, top engagement posts, and content angle suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External content marketers, social media managers, newsletter writers, and real-time content teams use this skill to research active Twitter/X conversations in a niche and turn them into prioritized content ideas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User search terms and Twitter/X research queries are sent to Apify/apidojo as a third-party service.

Mitigation: Avoid entering secrets, private customer lists, unreleased campaign terms, or sensitive personal data as search terms, and keep APIFY_TOKEN scoped and protected.

Risk: Trending Twitter/X topics can be short-lived, controversial, or misleading as content inputs.

Mitigation: Review topic clusters before publishing, qualify broad searches, and treat negative or news-reactive topics as higher-risk content opportunities.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/finding-trending-twitter-topics-for-content)
- [Apify tweet scraper REST endpoint](https://api.apify.com/v2/acts/apidojo~tweet-scraper/runs?token=$APIFY_TOKEN)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown brief with tables, ranked topic summaries, example tweet excerpts, and optional shell commands for running the Apify actor.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include topic velocity, engagement, freshness, opportunity scores, hashtag maps, and content angle recommendations.]

## Skill Version(s):

1.0.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
