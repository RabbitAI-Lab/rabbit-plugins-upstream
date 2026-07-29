## Description: <br>
Automated daily Amazon market monitoring that tracks a seller's ASINs and selected competitors for price moves, BSR shifts, new entrants, review waves, stockout signals, and tiered RED/YELLOW/GREEN alerts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Amazon sellers and commerce operators use this skill to establish a daily baseline for their own ASINs, compare subsequent runs against prior snapshots, and receive prioritized market-change briefings for competitor, category, review, price, and stock signals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a ZooData API key and sends tracked ASINs, competitor ASINs, category paths, keywords, marketplace/date values, and numeric filters to ZooData. <br>
Mitigation: Install only when that data sharing is acceptable, keep ZOODATA_API_KEY scoped and private, and review configured ASINs and keywords before scheduled runs. <br>
Risk: Daily radar runs can spend roughly 15-30 ZooData credits, and broad or ambiguous monitoring requests can expand API usage. <br>
Mitigation: Estimate credit cost before multi-call scans, ask for explicit confirmation on broad requests, and use granular commands when a user needs tighter budget control. <br>
Risk: Bundled watchlist and last-run files may contain sample or previous-run ASIN/category data that could affect a real deployment baseline. <br>
Mitigation: Reset data/watchlist.json and data/last-run.json before production use so the first run establishes a clean user-specific baseline. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/apiclaw/skills/amazon-daily-market-radar) <br>
- [Project homepage](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [API Field Reference](references/reference.md) <br>
- [ZooData](https://zoodata.ai) <br>
- [ZooData API docs](https://api.zoodata.ai/api-docs) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown briefing with alert sections, KPI tables, competitor movement, market shifts, action items, data provenance, and API usage.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZOODATA_API_KEY and normally consumes about 15-30 ZooData credits per daily radar run.] <br>

## Skill Version(s): <br>
1.0.6 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
