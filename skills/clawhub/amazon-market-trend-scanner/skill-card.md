## Description:

Scans Amazon category landscapes to identify trending subcategories, emerging niches, and market shifts such as demand surges, brand consolidation, new entrant waves, price band migration, and margin changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apiclaw](https://clawhub.ai/user/apiclaw)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, market researchers, and agent users use this skill to scan Amazon parent categories, compare subcategory movement over time, and identify promising or risky market directions. It supports full discovery scans and scheduled quick checks that can update local baselines and alert on notable trend shifts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Amazon category, keyword, ASIN, marketplace/date, and numeric filter data is sent to ZooData during scans.

Mitigation: Install and run the skill only when that data sharing is acceptable; avoid entering sensitive seller-profile text because the skill does not need it for API calls.

Risk: Bundled scan history and baselines can retain prior monitored categories locally.

Mitigation: Review, clear, or prune the scan-data folder before scheduled monitoring so checks begin from the user's intended categories.

Risk: Broad scans and optional endpoint probes can consume ZooData API credits.

Mitigation: Review estimated credit use before multi-call scans and avoid optional check endpoint probes unless spending credits is intended.

Risk: Scheduled monitoring can run recurring scans without direct supervision.

Mitigation: Enable scheduled monitoring only after confirming the watchlist, alert thresholds, and retained local state.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/apiclaw/skills/amazon-market-trend-scanner)
- [Publisher Profile](https://clawhub.ai/user/apiclaw)
- [Metadata Homepage: ZooData Skills](https://github.com/SerendipityOneInc/ZooData-Skills)
- [ZooData API Documentation](https://api.zoodata.ai/api-docs)
- [ZooData API Key Setup](https://zoodata.ai/en/api-keys)
- [ZooData Pricing](https://zoodata.ai/en/pricing)
- [ZooData CLI Contract](references/cli-contract.md)
- [Market Trend Scanner API Field Reference](references/reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with trend tables, API usage and data provenance sections, optional shell or scheduler configuration, and local JSON scan state.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports match the user's language and label conclusions as data-backed, inferred, or directional.]

## Skill Version(s):

1.0.8 (source: evidence release version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
