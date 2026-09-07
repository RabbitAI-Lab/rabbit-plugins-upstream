## Description:

Builds a curated Twitter industry watchlist of key voices using apidojo's Twitter scrapers on Apify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

Business analysts, investors, executives, and professionals use this skill to identify and score high-signal Twitter/X accounts in an industry for market monitoring and list creation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Apify-based Twitter/X research can collect or process social profile data at larger volume than intended.

Mitigation: Keep APIFY_TOKEN private, set maxItems deliberately, and avoid broad follower, following, or retweeter harvesting unless it is necessary and approved.

Risk: Watchlist scoring can include bot-like, promotional, or low-signal accounts.

Mitigation: Review candidate accounts before use, filter accounts with disproportionate retweet activity or heavy external-link promotion, and keep the final list small enough for reliable monitoring.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/building-twitter-industry-watchlist)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API calls, Guidance]

**Output Format:** [Markdown with tables and inline shell or API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include account handles, follower counts, engagement metrics, topic focus, influence scores, and instructions for creating a Twitter/X list.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
