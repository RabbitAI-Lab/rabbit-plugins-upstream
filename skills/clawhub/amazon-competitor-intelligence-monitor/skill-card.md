## Description:

Amazon competitor intelligence engine that produces focused one-shot competitor teardowns or ongoing per-competitor monitoring with alerts for a defined keyword, ASIN, brand, or competitor set.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apiclaw](https://clawhub.ai/user/apiclaw)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, brand operators, and marketplace analysts use this skill to compare identified Amazon competitors, monitor ASIN or brand changes, and generate battle-card style recommendations from ZooData API evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Amazon identifiers and market filters to the ZooData API.

Mitigation: Use it only when sharing ASINs, keywords, category paths, marketplace/date values, and numeric filters with ZooData is acceptable.

Risk: API calls consume ZooData account credits, and broad scans or scheduled monitoring can create recurring cost.

Mitigation: Review credit estimates before broad scans and enable scheduled monitoring only when recurring API use is intended.

Risk: Monitoring mode retains local baseline, history, and alert files.

Mitigation: Delete the skill's monitor-data folder when retained monitoring state should be reset or removed.

Risk: The skill requires a ZooData API key and can use an optional local config file.

Mitigation: Prefer setting ZOODATA_API_KEY in the environment over relying on ~/.zoodata/config.json.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/apiclaw/skills/amazon-competitor-intelligence-monitor)
- [Project Homepage](https://github.com/SerendipityOneInc/ZooData-Skills)
- [ZooData API Field Reference](references/reference.md)
- [ZooData CLI Contract](references/cli-contract.md)
- [ZooData API Keys](https://zoodata.ai/en/api-keys)
- [ZooData Pricing](https://zoodata.ai/en/pricing)
- [ZooData](https://zoodata.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with tables, alerts, disclaimers, data provenance, and API usage summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZOODATA_API_KEY, consumes ZooData API credits, and may retain local monitoring baselines, history, and alerts.]

## Skill Version(s):

1.1.9 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
