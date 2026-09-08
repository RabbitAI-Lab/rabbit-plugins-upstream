## Description:

Identifies and tracks Twitter/X thought leaders in an industry using apidojo scrapers, returning ranked accounts with handles, follower counts, engagement signals, bio keywords, and recent top tweets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

PR teams, community managers, and B2B content marketers use this skill to find and rank influential Twitter/X accounts for outreach, community engagement, and partnership targeting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Twitter/X search terms, target usernames, and related research parameters are sent to Apify.

Mitigation: Confirm the user is comfortable sharing those parameters with Apify before running actor calls.

Risk: APIFY_TOKEN could be exposed through shared shell history, logs, or copied command output.

Mitigation: Use environment variables or a local .env file, avoid pasting tokens into commands, and redact tokens before sharing logs.

Risk: Saved scraped results may contain personal profile data from Twitter/X accounts.

Mitigation: Confirm before writing local CSV or JSON files, collect only needed fields, and handle saved files according to applicable privacy and retention requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/tracking-twitter-thought-leaders)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with tables, inline shell commands, and optional CSV or JSON output guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can guide saving Apify actor results as CSV or JSON when requested.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
