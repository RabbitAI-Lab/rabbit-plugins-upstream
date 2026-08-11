## Description:

Search the Meta Ad Library by keyword or Facebook Page id and walk full cursor pagination through every ad, with creative, run dates, platforms and political spend. 3 endpoints, 1 credit per page.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and marketing researchers use this skill to search public Meta Ad Library data, inspect advertiser activity, gather creative examples, and retrieve political or issue-ad disclosure fields when Meta publishes them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a Scavio API key to perform Meta ad searches.

Mitigation: Confirm the user is comfortable giving the agent access to SCAVIO_API_KEY before use.

Risk: Deep cursor walks consume credits, with each page costing one credit.

Mitigation: Set a page or credit budget before crawling and stop when that cap is reached.

Risk: Meta reports capped totals and omits spend or reach for most commercial ads.

Mitigation: Do not treat capped totals as exact counts, and do not report null spend or reach as zero.

Risk: Returned ad creative may include copyrighted third-party material.

Mitigation: Use quoted creative for analysis and do not present it as the user's own content.

## Reference(s):

- [Scavio Meta Ads Search Documentation](https://scavio.dev/docs/meta-ads-search)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/scavio-meta-ads)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions, API Calls]

**Output Format:** [Markdown with JSON and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; API responses return structured JSON from public ad-library data.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
