## Description: <br>
Analyzes Amazon keyword expansion, bidding viability, ASIN keyword traffic, keyword health, and keyword traffic changes using ZooData keyword workflows that require ZOODATA_API_KEY. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External marketplace operators and developers use this skill to expand Amazon keyword ideas, assess keyword traffic and ASIN visibility, and produce bounded, evidence-labeled recommendations using ZooData API data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends keyword, ASIN, marketplace/date, and numeric research inputs to ZooData and can spend ZooData API credits. <br>
Mitigation: Use only necessary research inputs, estimate and confirm credit use for broad scans, and avoid sending unrelated sensitive business context. <br>
Risk: A persistent credential file can leave the ZooData API key available outside a single session. <br>
Mitigation: Prefer the ZOODATA_API_KEY environment variable over persistent config files. <br>
Risk: The bundled ZooData CLI exposes broader subcommands than this keyword-analysis workflow requires. <br>
Mitigation: Use runtime or tool controls to restrict execution to the documented keyword workflow subcommands when stricter enforcement is needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/apiclaw/skills/amazon-keyword-traffic-analysis) <br>
- [Project homepage](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [ZooData API keys](https://zoodata.ai/en/api-keys) <br>
- [ZooData Keyword API Reference](references/reference.md) <br>
- [Execution Guide - Amazon Keyword Intelligence](references/execution-guide.md) <br>
- [Keyword Expansion](references/scenarios-expand.md) <br>
- [Single Keyword Analysis](references/scenarios-keyword-analysis.md) <br>
- [Reverse ASIN Keyword Analysis](references/scenarios-reverse-asin.md) <br>
- [Keyword Traffic Diagnosis](references/scenarios-keyword-traffic-diagnosis.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports with API usage tables, evidence-level notes, and concise recommendations.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include ZooData CLI/API call summaries, credit usage when returned, and explicit boundaries for decisions requiring seller-real evidence.] <br>

## Skill Version(s): <br>
0.1.4 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
