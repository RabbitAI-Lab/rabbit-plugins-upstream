## Description:

Mines App Store and Google Play data via the Crawlora API - app details, reviews, ratings, store rankings, and similar apps - as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, analysts, and ASO researchers use this skill to retrieve public App Store and Google Play metadata, reviews, ratings, rankings, and similar-app lists for app-review mining and competitive research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The included Crawlora helper can call arbitrary Crawlora API paths, which is broader than the app-review-mining purpose.

Mitigation: Review requested paths before execution and restrict routine use to the App Store and Google Play endpoints documented in reference/endpoints.md.

Risk: API keys or private workspace data could be exposed if placed in request bodies, query strings, code, or committed files.

Mitigation: Keep the Crawlora key in CRAWLORA_API_KEY, avoid passing secrets or private data as request payloads, and do not hardcode or commit credentials.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/app-review-mining)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands that return JSON from the Crawlora API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and emits raw JSON suitable for jq or downstream review-mining analysis.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
