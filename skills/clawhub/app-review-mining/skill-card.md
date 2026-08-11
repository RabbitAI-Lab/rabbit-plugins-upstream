## Description:

Mines App Store and Google Play data via the Crawlora API, including app details, reviews, ratings, store rankings, and similar apps, as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and ASO teams use this skill to retrieve public App Store and Google Play app metadata, reviews, ratings, rankings, and similar-app data for review mining, competitor tracking, and app store optimization research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can send arbitrary Crawlora API requests with the user's API key.

Mitigation: Review generated commands before running them and restrict use to intended app store endpoints and parameters.

Risk: App IDs, search terms, and request parameters are sent to Crawlora with the user's API key.

Mitigation: Avoid secrets and proprietary queries unless Crawlora's handling of that data has been assessed.

## Reference(s):

- [ClawHub app-review-mining release page](https://clawhub.ai/tonywangcn/skills/app-review-mining)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends selected request paths and parameters to the Crawlora API.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
