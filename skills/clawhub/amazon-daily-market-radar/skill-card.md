## Description: <br>
Automates daily Amazon market monitoring for tracked ASINs and competitors, producing change-detection briefings for price moves, BSR shifts, new entrants, review spikes, and stockout signals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Amazon sellers and ecommerce operators use this skill to run scheduled daily monitoring for their own ASINs, selected competitors, and category movement. It helps agents produce alert-prioritized Markdown briefings with KPI comparisons, market shifts, action items, data provenance, and API usage. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a ZooData/APIClaw-compatible API key and spends ZooData credits during monitoring runs. <br>
Mitigation: Set ZOODATA_API_KEY explicitly, review configured legacy credential stores before use, and confirm expected credit cost before broad or ambiguous multi-call scans. <br>
Risk: The bundled CLI includes broader ZooData tooling than the Amazon daily radar workflow requires. <br>
Mitigation: Use only the documented daily radar and supporting subcommands needed for this skill, and avoid unrelated research or keyword commands unless intentionally requested. <br>
Risk: The skill keeps local monitoring baselines and may use temporary review-processing files. <br>
Mitigation: Review local data retention expectations for watchlist, last-run, and temporary review files before deploying scheduled automation. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/apiclaw/skills/amazon-daily-market-radar) <br>
- [Publisher Profile](https://clawhub.ai/user/apiclaw) <br>
- [ZooData Homepage](https://zoodata.ai) <br>
- [ZooData API Documentation](https://api.zoodata.ai/api-docs) <br>
- [ZooData API Key Setup](https://zoodata.ai/en/api-keys) <br>
- [CLI Contract](references/cli-contract.md) <br>
- [ZooData API Field Reference](references/reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown briefing with tables, alert sections, inline endpoint provenance, and API usage summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZOODATA_API_KEY and may write local watchlist and baseline JSON files for scheduled monitoring.] <br>

## Skill Version(s): <br>
1.0.8 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
