## Description:

Search the Apple App Store, read a full app listing by App Store id or bundle id, and pull user reviews as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, ASO analysts, and agent builders use this skill to search App Store apps, fetch listing metadata, and retrieve review pages through Scavio for app research, competitor analysis, and dataset building.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends App Store search terms, app IDs, country codes, and review-page requests to Scavio, and every API call can consume Scavio credits.

Mitigation: Keep SCAVIO_API_KEY in an environment variable or secret store, budget request volume, and prefer one large search over repeated single-app calls when that satisfies the task.

Risk: Using an invalid or ambiguous app identifier can produce empty or billed lookups, and review lookups cannot distinguish an unknown app from an app with no reviews.

Mitigation: Confirm app identity with the app listing endpoint before looping over IDs or interpreting empty review results.

Risk: Storefront choice changes price, currency, localized text, availability, and review pools.

Mitigation: Use explicit two-letter country codes and report the storefront used whenever results depend on price, availability, localization, or reviews.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/apple-app-store-api)
- [Scavio App Store Search documentation](https://scavio.dev/docs/app-store-search)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration, API calls, JSON]

**Output Format:** [Markdown guidance with shell, Python, and JavaScript examples; Scavio API responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY and consumes Scavio credits for API calls.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
