## Description:

政府采购智能分析 helps suppliers, procurement agents, and purchasing organizations analyze public procurement opportunities, bid decisions, tender materials, competitor profiles, compliance risks, policy differences, contracts, and acceptance workflows using public procurement data and local analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Suppliers, procurement agents, and purchasing organizations use this skill to find Chinese government procurement opportunities, evaluate bid fit and pricing, draft or review tender materials, audit compliance, track competitors, and maintain local bidding knowledge.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill stores company profile, procurement, bidding history, collaboration, and knowledge-base data locally.

Mitigation: Install and run it only in an environment where local retention of business bidding data is approved, and periodically review or purge generated local databases.

Risk: Optional enterprise chat webhooks can send project details outside the local environment.

Mitigation: Enable webhook notifications only for approved enterprise chat endpoints and avoid sending sensitive bid content through notification cards.

Risk: The release evidence flags broad automation and self-updating behavior as requiring review.

Mitigation: Review the skill before installation and do not use any remote self-update flow unless the update source is trusted and the changes can be inspected.

Risk: Public procurement collection can be affected by website terms, rate limits, robots.txt, or platform changes.

Mitigation: Keep collection scoped to public information, respect documented rate limits and robots.txt behavior, and manually review high-impact procurement recommendations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/gov-procurement-analyst)
- [Data source platforms and compliance guide](artifact/references/procurement-platforms.md)
- [Anti-scraping best practices](artifact/references/anti-scraping-best-practices.md)
- [Enterprise profiling and matching algorithm](artifact/references/enterprise-profiling.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports, JSON files, and command-line script output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local SQLite-backed analysis artifacts and optional enterprise chat notification content when configured.]

## Skill Version(s):

5.2.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
