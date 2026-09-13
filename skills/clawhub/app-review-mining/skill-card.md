## Description:

Mines App Store and Google Play data via the Crawlora API - app details, reviews, ratings, store rankings, and similar apps - as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, product teams, and ASO researchers use this skill to retrieve public mobile-app metadata, reviews, ratings, rankings, and similar-app lists for app review mining, competitive analysis, and monitoring workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper uses a Crawlora API key and sends app-store research queries to Crawlora.

Mitigation: Install only for trusted workflows, keep CRAWLORA_API_KEY in the environment, and avoid hardcoding, committing, or passing the key in query parameters.

Risk: Security evidence notes that the helper can make broader authenticated Crawlora API calls than the endpoint reference describes.

Mitigation: Review scripts/crawlora.sh before use, prefer documented GET endpoints, and do not let untrusted prompts supply raw paths, -X POST, or request bodies.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/app-review-mining)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns Crawlora JSON for public App Store and Google Play data.]

## Skill Version(s):

1.0.15 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
