## Description:

Searches Facebook Marketplace listings and looks up public Facebook Page details via the Crawlora API, returning clean JSON for location, category, or public Page research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and business users use this skill to query public Facebook Marketplace listings or public Facebook Page details through Crawlora instead of scraping Facebook directly. It supports local resale price checks, browse-feed checks, and public Page enrichment such as follower counts, category, and listed contact information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can send arbitrary Crawlora API paths with the user's API key, beyond the Facebook endpoints documented for this skill.

Mitigation: Review the script before use, use a limited Crawlora key, and prefer a version that restricts calls to /facebook/marketplace/search and /facebook/{page}.

Risk: Marketplace and Page queries may expose sensitive search intent or identifiers to the API provider.

Mitigation: Avoid sensitive searches or identifiers and limit use to public Facebook Marketplace listings and public Page information.

Risk: API credentials could be leaked if copied into commands, URLs, or committed files.

Mitigation: Provide the key only through CRAWLORA_API_KEY and do not hardcode, query-parametrize, or commit it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/facebook-research)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell command examples and raw JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; Marketplace results are single-page and Page lookups return public Facebook Page fields.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
