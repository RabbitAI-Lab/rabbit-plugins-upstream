## Description:

Search the Apple App Store, read a full app listing by App Store id or bundle id, and pull user reviews as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to find iOS, iPadOS, and macOS apps, retrieve app listings, compare publisher catalogues, and collect App Store reviews as structured data for research, ASO, and competitive analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Scavio as a third-party API provider and requires a SCAVIO_API_KEY.

Mitigation: Store SCAVIO_API_KEY in the runtime environment or a secret manager, and install only when use of Scavio as a provider is acceptable.

Risk: API calls spend Scavio credits, and broad review collection can multiply calls across countries and pages.

Mitigation: Review expected call volume before bulk searches or multi-country review collection, and prefer a single larger search request where appropriate.

Risk: App Store search and reviews have documented limits, including no search pagination and a maximum of 500 reviews per storefront.

Mitigation: Raise the search limit instead of paging search results, and use additional storefront countries only when broader review coverage is needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/apple-app-store-api)
- [Scavio App Store Search documentation](https://scavio.dev/docs/app-store-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=apple-app-store-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=apple-app-store-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API request patterns and Python or JavaScript code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance centers on Scavio API calls that return structured JSON from App Store search, app listing, and review endpoints.]

## Skill Version(s):

1.0.3 (source: server release evidence; artifact frontmatter version is 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
