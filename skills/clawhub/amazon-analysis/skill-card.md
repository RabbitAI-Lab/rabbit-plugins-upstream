## Description: <br>
Amazon Analysis is a ZooData-backed Amazon product, market, competitor, pricing, and ASIN research skill for broad or composite Amazon analysis workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and Amazon sellers use this skill to run ZooData-backed product, market, competitor, pricing, and ASIN research reports. It is intended for workflows that need multi-endpoint Amazon data exploration, product selection modes, or composite market reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Amazon research inputs and the ZooData API key are sent to ZooData during API-backed analysis. <br>
Mitigation: Install only if the user is comfortable sending those inputs and credentials to ZooData, and prefer environment-variable credential configuration. <br>
Risk: Fallback behavior, sampled data, or degraded analysis may make business recommendations appear stronger than the underlying evidence supports. <br>
Mitigation: Require reports to disclose fallbacks, data gaps, sampling limits, credit usage, and degraded analysis before using results for business decisions. <br>
Risk: The artifact includes a Chinese-seller profiling workflow that may be inappropriate for some deployments. <br>
Mitigation: Review or remove that workflow before deployment and avoid using nationality-based seller profiling unless it is lawful, necessary, and clearly disclosed. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/apiclaw/skills/amazon-analysis) <br>
- [Skill metadata homepage](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [ZooData](https://zoodata.ai) <br>
- [ZooData API key setup](https://zoodata.ai/en/api-keys) <br>
- [README](README.md) <br>
- [Execution Guide](references/execution-guide.md) <br>
- [API Field Reference](references/reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports with tables, confidence labels, data provenance, API usage summaries, and inline shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZOODATA_API_KEY. Broad workflows may consume ZooData credits, and reports should disclose estimated values, data gaps, and degraded analysis before business decisions.] <br>

## Skill Version(s): <br>
1.1.9 (source: release metadata and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
