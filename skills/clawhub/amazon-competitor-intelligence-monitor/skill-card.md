## Description: <br>
Amazon competitor intelligence engine for one-shot competitor teardowns and recurring per-competitor monitoring with alerts using ZooData API data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, brand operators, and commerce analysts use this skill to analyze identified Amazon competitors by keyword, ASIN, or brand and to monitor tracked ASINs for price, ranking, listing, review, and fulfillment changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bundled monitor-data includes a pre-filled collagen peptides configuration and baseline with tracked ASINs. <br>
Mitigation: Inspect or clear monitor-data before installing, then create monitoring state only for competitors selected by the user. <br>
Risk: Recurring Quick Checks may spend ZooData API credits or continue tracking products that are not relevant to the user's current task. <br>
Mitigation: Enable scheduled checks only after explicit user selection, review tracked ASINs, and monitor API credit usage. <br>
Risk: Keywords, ASINs, categories, and review requests are sent to ZooData for analysis. <br>
Mitigation: Treat those inputs as third-party API data and avoid submitting sensitive or unauthorized competitor lists. <br>
Risk: API credentials may be exposed if entered directly into prompts or persisted in local files. <br>
Mitigation: Prefer the ZOODATA_API_KEY environment variable and avoid embedding keys in generated reports or shared configuration. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/apiclaw/skills/amazon-competitor-intelligence-monitor) <br>
- [Publisher Profile](https://clawhub.ai/user/apiclaw) <br>
- [ZooData Skills Homepage](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [ZooData](https://zoodata.ai) <br>
- [ZooData API Documentation](https://api.zoodata.ai/api-docs) <br>
- [API Key Setup](https://zoodata.ai/en/api-keys) <br>
- [API Field Reference](references/reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, API calls, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown reports with tables, alerts, data provenance, API usage summaries, and inline shell commands when setup or scheduled checks are needed.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZOODATA_API_KEY; full scans consume about 28-35 credits and quick checks consume about 5-10 credits.] <br>

## Skill Version(s): <br>
1.1.4 (source: evidence release, artifact frontmatter, target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
