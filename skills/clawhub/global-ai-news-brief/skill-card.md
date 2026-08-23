## Description:

Global AI News Brief searches 11 social and news platforms from one keyword and helps an agent aggregate results, cluster topics, analyze sentiment, and produce terminal and HTML intelligence reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[redfox-data](https://clawhub.ai/user/redfox-data)

### License/Terms of Use:

MIT-0

## Use Case:

Market and sentiment analysts, media researchers, content teams, and operations staff use this skill to collect public cross-platform news signals, compare platform narratives, and produce briefings with source tables and an interactive report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search keywords and aggregated platform data are sent through RedFox using REDFOX_API_KEY.

Mitigation: Avoid sensitive internal investigation terms unless third-party API exposure is approved, and limit searches to a platform subset when appropriate.

Risk: The REDFOX_API_KEY could be exposed if it is hard-coded or included in prompts, logs, or output files.

Mitigation: Store the key in environment or agent configuration, verify its source and scope, and do not write the key into generated artifacts.

## Reference(s):

- [API Interface Reference](references/api-reference.md)
- [ClawHub Skill Page](https://clawhub.ai/redfox-data/skills/global-ai-news-brief)
- [RedFox API Service](https://redfox.hk)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Terminal Markdown tables, standardized JSON data, and an interactive HTML report.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires REDFOX_API_KEY; writes standardized JSON and an HTML report, with per-platform failures reported without blocking successful platforms.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
