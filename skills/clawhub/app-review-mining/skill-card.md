## Description:

Retrieves App Store and Google Play app details, reviews, ratings, rankings, and similar apps through the Crawlora API for app-review and ASO research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and app researchers use this skill to compare mobile-app ratings, analyze public reviews, monitor store rankings, and discover competing apps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: App lookup parameters and the API key are sent to Crawlora.

Mitigation: Use the skill only when that transfer is acceptable; keep CRAWLORA_API_KEY out of logs, commits, and shared shell history.

Risk: Implicit locale selection can make review and ranking comparisons misleading.

Mitigation: Pass country and language explicitly when locale matters, and account for paginated reviews.

## Reference(s):

- [App Store and Google Play endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/app-review-mining)

## Skill Output:

**Output Type(s):** [Text, Analysis]

**Output Format:** [JSON data or Markdown summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the selected store, locale, and review pagination.]

## Skill Version(s):

1.0.19 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
