## Description: <br>
Automates daily Amazon market monitoring for tracked seller ASINs and competitors, producing change-detection briefings for price moves, BSR shifts, new entrants, review waves, stockout signals, and RED/YELLOW/GREEN alerts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Amazon sellers and operators use this skill for recurring operational monitoring of their own ASINs and competitor ASINs. It helps an agent run scheduled ZooData checks, compare today's market snapshot with the previous baseline, and produce an alert-prioritized market digest. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a ZooData API key and makes recurring third-party API calls using ASINs, keywords, category paths, marketplace values, and competitor-tracking inputs. <br>
Mitigation: Use the skill only when those inputs may be shared with ZooData, prefer ZOODATA_API_KEY in the environment, and avoid storing credentials in persistent config files. <br>
Risk: The bundled CLI exposes a broader set of ZooData subcommands than the daily-radar workflow needs. <br>
Mitigation: Limit automation and agent prompts to the documented daily-radar workflow or the listed granular commands needed for daily monitoring. <br>
Risk: Changing ZOODATA_BASE_URL can redirect calls away from the default ZooData API host. <br>
Mitigation: Do not set ZOODATA_BASE_URL to non-ZooData hosts unless the destination is explicitly trusted and reviewed. <br>
Risk: Daily-radar runs can consume account credits, especially for broad or ambiguous monitoring requests. <br>
Mitigation: Estimate credit use before multi-call scans, monitor remaining credits, and use granular commands when a credit cap is required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/apiclaw/skills/amazon-daily-market-radar) <br>
- [Publisher profile](https://clawhub.ai/user/apiclaw) <br>
- [ZooData-Skills homepage](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [ZooData API documentation](https://api.zoodata.ai/api-docs) <br>
- [ZooData API key setup](https://zoodata.ai/en/api-keys) <br>
- [Market Entry Analyzer API Field Reference](references/reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown report with alert sections, KPI dashboard, data provenance table, API usage table, and local JSON snapshots.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Output language follows the user's input language; conclusions are labeled as data-backed, inferred, or directional; reports include a ZooData sampling disclaimer.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
