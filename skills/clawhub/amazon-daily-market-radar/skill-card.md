## Description:

Amazon Daily Market Radar produces ZooData-based daily Amazon seller monitoring briefings that compare tracked ASINs and competitors against prior baselines for price, BSR, entrant, review, and stockout changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apiclaw](https://clawhub.ai/user/apiclaw)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to opt in to daily monitoring for their own ASINs and competitors, then receive a ZooData-based change digest with alerts, KPI comparisons, market shifts, and action items.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tracked ASINs, competitor ASINs, keywords, category paths, and marketplace/date/filter values are sent to ZooData on each monitoring run.

Mitigation: Run the skill only after explicit monitoring opt-in and review the tracked product and market inputs before scheduled use.

Risk: Daily monitoring consumes ZooData account credits, with the composite daily radar documented at roughly 15 to 30 credits per run.

Mitigation: Monitor credit use for scheduled runs and use granular commands when a lower credit cap is required.

Risk: Local watchlist and last-run baseline snapshots persist under the skill data folder for day-over-day comparisons.

Mitigation: Delete the skill data folder when resetting monitoring or removing retained baseline data.

Risk: The skill requires a ZooData API key for API access.

Mitigation: Set ZOODATA_API_KEY through the environment or a secret manager and avoid embedding credentials in prompts or shared files.

## Reference(s):

- [ZooData API Field Reference](references/reference.md)
- [ZooData CLI Contract](references/cli-contract.md)
- [ClawHub Skill Page](https://clawhub.ai/apiclaw/skills/amazon-daily-market-radar)
- [Publisher Profile](https://clawhub.ai/user/apiclaw)
- [ZooData Skills Homepage](https://github.com/SerendipityOneInc/ZooData-Skills)
- [ZooData API Key Setup](https://zoodata.ai/en/api-keys)
- [ZooData](https://zoodata.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown briefing with alert sections, KPI tables, data provenance, API usage, and local JSON baseline updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Output language follows the user's input language; conclusions are labeled as data-backed, inferred, or directional.]

## Skill Version(s):

1.0.9 (source: SKILL.md metadata and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
