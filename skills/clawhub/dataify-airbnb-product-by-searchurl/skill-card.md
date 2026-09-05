## Description:

Collect structured Airbnb listing results from a known Airbnb search-results URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to prepare and run Dataify Builder requests that collect Airbnb listing results from a supplied Airbnb search URL, then wait for and return the collected JSON result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill submits Airbnb target URLs and collection parameters to Dataify using the user's account token.

Mitigation: Install and use it only when Dataify collection is intended, avoid sharing tokens in chat, and prefer a session-scoped DATAIFY_API_TOKEN unless persistent setup is required.

Risk: The package exposes broader Airbnb scraping behavior than the search-URL-focused description suggests because it includes both search-URL and location-based collection options.

Mitigation: Review the selected tool before execution and confirm scope when a request could increase collection volume or credit usage.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-airbnb-product-by-searchurl)
- [Publisher profile](https://clawhub.ai/user/dataify-server)
- [Dataify dashboard](https://dashboard.dataify.com/login?utm_source=skill)
- [Tool parameter catalog](references/tool-params.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit paid external Dataify scraping tasks and return summarized collected JSON while preserving access to the raw result.]

## Skill Version(s):

1.3.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
