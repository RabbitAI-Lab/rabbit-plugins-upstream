## Description: <br>
Amazon competitor intelligence engine that produces focused one-shot competitor teardowns or sustained per-competitor monitoring with alerts from a keyword, ASIN, or brand input. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, operators, and market analysts use this skill to analyze defined Amazon competitor sets, compare market position, and monitor tracked ASINs for pricing, listing, review, inventory, and trend changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a ZooData API key and can spend ZooData credits during competitor scans. <br>
Mitigation: Install only when API-key use and credit spending are acceptable; confirm estimated costs before broad or multi-call scans. <br>
Risk: Monitoring and review fallback workflows can retain local baselines, alerts, history, and temporary review-processing files. <br>
Mitigation: Review or delete the skill's monitor-data directory and any /tmp/review_* folders when retained local files are not desired. <br>
Risk: Competitor analysis is based on sampled ZooData API responses and may include lower-bound estimates or inferred recommendations. <br>
Mitigation: Keep the report disclaimer and confidence labels visible, and validate important business decisions with additional sources before acting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/apiclaw/skills/amazon-competitor-intelligence-monitor) <br>
- [Publisher profile](https://clawhub.ai/user/apiclaw) <br>
- [Project homepage](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [ZooData API field reference](references/reference.md) <br>
- [ZooData API documentation](https://api.zoodata.ai/api-docs) <br>
- [ZooData API key setup](https://zoodata.ai/en/api-keys) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports with tables, inline shell commands, confidence labels, data provenance, and API usage summaries.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should match the user's language and may persist monitoring baselines, history, alerts, and review-processing work files when monitoring or fallback review workflows are used.] <br>

## Skill Version(s): <br>
1.1.7 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
