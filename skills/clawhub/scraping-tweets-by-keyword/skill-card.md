## Description:

Scrapes tweets matching a keyword, hashtag, phrase, or boolean query using apidojo's Twitter Search scraper on Apify and returns tweet data for downstream analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, analysts, journalists, and social listening teams use this skill to collect tweets matching search terms and export the resulting dataset for analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and collected tweet datasets may contain sensitive information and are sent to a third-party service.

Mitigation: Confirm the collection scope with the user, avoid unnecessary personal or sensitive search terms, and review datasets before saving or sharing them.

Risk: Command examples can place APIFY_TOKEN in URLs, which may expose credentials through shell history, logs, or process listings.

Mitigation: Prefer environment variables, .env files, or Apify tooling that avoids embedding tokens directly in command URLs.

Risk: Large tweet collections can create unintended exported files or overly broad datasets.

Mitigation: Use explicit maxItems and date filters, confirm before writing CSV or JSON files, and keep exports scoped to the user's stated task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/scraping-tweets-by-keyword)
- [Apify actor: apidojo/tweet-scraper](https://apify.com/apidojo/tweet-scraper)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with command examples and optional JSON or CSV dataset exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tweet results include fields such as id, text, author, engagement counts, language, timestamp, tweet URL, and media metadata.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
