## Description:

Mines App Store and Google Play data via the Crawlora API for app details, reviews, ratings, store rankings, and similar apps as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and ASO researchers use this skill to collect public App Store and Google Play app metadata, reviews, ratings, rankings, and competitor signals through Crawlora endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can send the Crawlora API key to an API destination selected through CRAWLORA_API_BASE.

Mitigation: Run it only in a trusted shell environment, clear untrusted inherited variables, and avoid setting CRAWLORA_API_BASE unless you intentionally control the destination.

Risk: Search terms, app IDs, and request bodies are sent to the Crawlora API.

Mitigation: Treat all request inputs as data shared with Crawlora and avoid submitting sensitive or confidential values.

Risk: The helper script supports broader Crawlora paths than the app-review examples.

Mitigation: Limit usage to the documented App Store and Google Play endpoints unless broader Crawlora access has been reviewed for the deployment.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY for authenticated Crawlora API requests; API responses are returned as JSON.]

## Skill Version(s):

1.0.9 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
