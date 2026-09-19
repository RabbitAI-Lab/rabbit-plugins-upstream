## Description:

Researches apps and browser extensions across the Apple App Store, Google Play, and Chrome Web Store using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and market analysts use this skill to discover and compare public app and browser-extension listings, reviews, rankings, permissions, privacy disclosures, and release history across major app stores.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends app-store search terms, app IDs, extension IDs, and similar query parameters to the Crawlora API.

Mitigation: Avoid private or unrelated personal data in queries and use the skill only when sharing those public-research parameters with Crawlora is acceptable.

Risk: The skill requires a Crawlora API key.

Mitigation: Keep CRAWLORA_API_KEY secret, store it in the environment, and do not paste it into prompts, command arguments, logs, or shared outputs.

Risk: Returned reviews, permissions, privacy disclosures, rankings, and data-safety statements are public listing evidence, not independent audits or full market measurements.

Mitigation: Preserve source, country, language, sort, and page context; report missing or partial sources; and avoid inferring downloads, revenue, retention, market share, or security posture from these fields alone.

Risk: Publisher contact details may appear in returned public store metadata.

Mitigation: Handle returned contact details according to privacy expectations and applicable rules.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API service](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends documented public app-store query parameters to Crawlora.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
