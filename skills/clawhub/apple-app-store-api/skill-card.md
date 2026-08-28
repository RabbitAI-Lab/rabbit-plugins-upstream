## Description:

Search the Apple App Store, read a full app listing by App Store id or bundle id, and pull user reviews as structured JSON. 3 endpoints, 1 credit each, any Apple storefront.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, app marketers, and analysts use this skill to search App Store listings, retrieve app metadata, and collect reviews for App Store Optimization, competitor research, and app-data exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: App Store lookup requests are sent to Scavio and consume API credits.

Mitigation: Confirm the intended app, country storefront, and page limits before making repeated calls; prefer one larger search over loops of app-detail calls when possible.

Risk: SCAVIO_API_KEY can grant access to the user's Scavio account and credits if exposed.

Mitigation: Keep SCAVIO_API_KEY in an environment variable or secret store and avoid committing it to source code or logs.

Risk: Review and search limits can make results incomplete or ambiguous.

Mitigation: State the queried storefront, respect the documented 500-review-per-storefront ceiling, and confirm app identity with the app endpoint before treating empty reviews as evidence that an app does not exist.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/apple-app-store-api)
- [Scavio App Store Search documentation](https://scavio.dev/docs/app-store-search)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands, code examples, and structured JSON API response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; uses Scavio network API calls; documented responses are structured JSON and each endpoint costs 1 credit.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
