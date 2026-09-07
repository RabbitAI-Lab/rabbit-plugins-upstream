## Description:

Mines App Store and Google Play data via the Crawlora API -- app details, reviews, ratings, store rankings, and similar apps -- as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, product analysts, and ASO researchers use this skill to retrieve public App Store and Google Play app details, reviews, ratings, rankings, and similar-app data for sentiment analysis, competitor tracking, and store research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can make broader authenticated Crawlora API requests than the app-review use case describes.

Mitigation: Use the documented App Store and Google Play GET endpoints for app-review workflows, and review any other requested path before running it.

Risk: The Crawlora API key and configurable API base affect where authenticated requests are sent.

Mitigation: Keep CRAWLORA_API_KEY scoped to trusted shells or projects, and set CRAWLORA_API_BASE only for destinations you control.

## Reference(s):

- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Endpoint reference](reference/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/app-review-mining)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides authenticated Crawlora API calls that return normalized JSON for public mobile-app store data.]

## Skill Version(s):

1.0.8 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
