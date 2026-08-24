## Description:

Search the Apple App Store, read a full app listing by App Store id or bundle id, and pull user reviews as structured JSON. 3 endpoints, 1 credit each, any Apple storefront.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, product teams, and App Store Optimization researchers use this skill to search App Store apps, retrieve full app listings, and collect user reviews as structured JSON for competitive research, publisher audits, and metadata datasets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to a Scavio API key and can spend Scavio credits when it queries App Store data.

Mitigation: Confirm the user is comfortable providing SCAVIO_API_KEY and monitor query volume before running bulk searches or multi-country review collection.

Risk: App Store review and search behavior has endpoint limits, including no search pagination and a 500-review ceiling per storefront.

Mitigation: Use the documented limit and country parameters, avoid looping nonexistent search pages, and disclose the storefront queried when price, availability, or localized text matters.

## Reference(s):

- [Scavio App Store Search documentation](https://scavio.dev/docs/app-store-search)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)
- [ClawHub skill listing](https://clawhub.ai/scavio-ai/skills/scavio-app-store)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration, JSON]

**Output Format:** [Markdown with inline shell, Python, JavaScript, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SCAVIO_API_KEY and may spend Scavio credits when queries are executed.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
