## Description:

Researches products, variants, shops, and reviews on Shop.app using the Crawlora API, returning normalized JSON for cross-store product, merchant, and review research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to search Shop.app products, compare merchant offerings, retrieve product or shop reviews, and summarize public market snapshots without scraping Shop.app pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Use of a Crawlora API key with paid credits or broader account authority can increase account-impact risk.

Mitigation: Review the skill before installing and use a scoped Crawlora key appropriate for Shop.app research.

Risk: The security review reported that the helper can make broader authenticated Crawlora API calls than the documented read-only endpoints require.

Mitigation: Prefer exact documented endpoint shapes and tighten routine use to the Shop.app read-only endpoints described in the reference.

## Reference(s):

- [Shop.app Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API Base](https://api.crawlora.net/api/v1)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/shop-app-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns public Shop.app data through documented Crawlora endpoints.]

## Skill Version(s):

1.0.13 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
