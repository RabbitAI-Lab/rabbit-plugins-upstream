## Description: <br>
Automated daily Amazon market digest for ASIN watchlists that compares current ZooData API snapshots against prior baselines to surface price, BSR, competitor, review, and stockout changes as RED/YELLOW/GREEN alerts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Amazon sellers and operators use this skill to schedule recurring market monitoring for their own ASINs and selected competitors. It produces alert-prioritized change-detection briefings for daily operational decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tracked ASINs, competitor ASINs, keywords, category paths, and related Amazon market parameters are sent to ZooData on each run. <br>
Mitigation: Install only when this data sharing is acceptable for the monitored products and market; avoid adding sensitive business context that is not needed for the API request. <br>
Risk: Scheduled runs can consume ZooData account credits, especially when the composite daily-radar workflow fans out across multiple endpoints. <br>
Mitigation: Monitor credit usage for scheduled runs and use narrower granular commands when operating under a credit cap. <br>
Risk: Local watchlist and last-run snapshot files retain product identifiers and monitoring history. <br>
Mitigation: Store the skill in an access-controlled workspace and remove stale snapshots or temporary review-analysis directories when they are no longer needed. <br>
Risk: Credentials may be available from environment variables or a user-home ZooData config file. <br>
Mitigation: Prefer ZOODATA_API_KEY in the scheduler environment and rotate the key if a local credential file is exposed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/apiclaw/skills/amazon-daily-market-radar) <br>
- [Publisher profile](https://clawhub.ai/user/apiclaw) <br>
- [ZooData Skills homepage](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [ZooData API Field Reference](artifact/references/reference.md) <br>
- [ZooData API documentation](https://api.zoodata.ai/api-docs) <br>
- [ZooData API key setup](https://zoodata.ai/en/api-keys) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown daily alert digest with KPI tables, API usage and provenance tables, and optional shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZOODATA_API_KEY; sends tracked ASINs, competitor ASINs, keywords, category paths, marketplace/date values, and numeric filters to ZooData; persists watchlist and last-run JSON snapshots.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release evidence; bundled frontmatter reports 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
