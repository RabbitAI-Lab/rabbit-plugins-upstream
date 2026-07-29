## Description: <br>
Amazon Competitor Intelligence Monitor helps agents run ZooData-powered Amazon competitor scans or ongoing ASIN monitoring for a defined competitor set. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze named Amazon competitors by keyword, ASIN, or brand, then generate competitive reports, battle cards, pricing and review breakdowns, and monitoring alerts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends Amazon product research inputs, such as keywords, ASINs, category paths, marketplace/date values, and numeric filters, to ZooData. <br>
Mitigation: Use the skill only for product research data you are comfortable processing through ZooData, and avoid adding unrelated sensitive user-profile text to scan inputs. <br>
Risk: Full scans and review fallbacks consume ZooData API credits and broad scans can trigger many API calls. <br>
Mitigation: Confirm estimated credit cost before multi-call scans, use quick checks or granular commands under a credit cap, and stop when credentials are invalid or credits are exhausted. <br>
Risk: The skill stores local monitoring baselines, history, alerts, and temporary review files that may contain competitor research details. <br>
Mitigation: Periodically clean monitor-data and /tmp review work directories when the analysis is sensitive. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/apiclaw/skills/amazon-competitor-intelligence-monitor) <br>
- [ZooData Skills homepage metadata](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [ZooData API documentation](https://api.zoodata.ai/api-docs) <br>
- [ZooData API key setup](https://zoodata.ai/en/api-keys) <br>
- [API field reference](references/reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports with tables, command snippets, confidence labels, data provenance, and API usage summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZOODATA_API_KEY and may create local monitor-data or temporary review work directories during analysis.] <br>

## Skill Version(s): <br>
1.1.6 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
