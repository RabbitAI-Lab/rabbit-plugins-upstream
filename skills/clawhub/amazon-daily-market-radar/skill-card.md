## Description: <br>
Automates daily Amazon market monitoring for a user's ASINs and selected competitors, producing change-detection briefings on price moves, BSR shifts, new entrants, review waves, stockout signals, and tiered RED/YELLOW/GREEN alerts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Amazon sellers and commerce operators use this skill to schedule recurring market checks for their own products and competitor ASINs, then review a daily operational digest of material changes and recommended follow-up actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Amazon ASINs, keywords, category paths, and review-related data are sent to ZooData for scheduled monitoring. <br>
Mitigation: Install only when this data sharing is acceptable for the monitored products and business context. <br>
Risk: The bundled CLI uses credential and persistence patterns that should be reviewed before installation. <br>
Mitigation: Use ZOODATA_API_KEY from a controlled environment or secret manager and clear bundled sample data before first use. <br>
Risk: Unattended daily runs can keep transmitting watchlist data beyond the original setup moment. <br>
Mitigation: Tie scheduling to an explicit owner-approved ASIN watchlist and review the watchlist before enabling automation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/apiclaw/skills/amazon-daily-market-radar) <br>
- [ZooData-Skills GitHub repository](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [ZooData API documentation](https://api.zoodata.ai/api-docs) <br>
- [ZooData API base endpoint reference](https://api.zoodata.ai/openapi/v2) <br>
- [Local API field reference](references/reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown report with alert sections, KPI tables, data provenance, API usage, and inline shell commands for setup and execution.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Report language follows the user's input language; each conclusion is labeled as data-backed, inferred, or directional.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
