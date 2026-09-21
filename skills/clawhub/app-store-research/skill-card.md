## Description:

Researches apps and browser extensions across the Apple App Store, Google Play, and Chrome Web Store using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, product researchers, and market analysts use this skill to gather public app and browser-extension listing evidence, compare publishers and products, inspect reviews and ratings, and review public privacy, permission, ranking, and release-history signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: App-store research queries and the Crawlora API key are sent to Crawlora.

Mitigation: Use only non-sensitive research terms, set the API key through CRAWLORA_API_KEY, and install only if that data flow is acceptable.

Risk: Returned publisher contact, trader, review, or listing details can include personal or business-contact data.

Mitigation: Handle returned data under applicable privacy and data-handling requirements, and treat store disclosures as listing evidence rather than an independent security audit.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/app-store-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples; the helper returns JSON from the Crawlora API.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and works with public app-store listing, review, privacy, permission, ranking, and release-history data.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
