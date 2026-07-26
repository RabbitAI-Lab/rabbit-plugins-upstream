## Description: <br>
对承接率下降做阶段式归因分析，定位异常切片，并逐层判断下降原因是否来自结构迁移、资方总量或分布变化、资产维度异常，或敏感资方侧收缩。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mzhou1982](https://clawhub.ai/user/mzhou1982) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Business analysts and operations teams use this skill to investigate why acceptance rate declined across daily or weekly periods. It guides an agent through staged metric queries, slice analysis, funding-source checks, and Markdown reporting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a sensitive BIGDATA analytics cookie token and may persist it for later sessions. <br>
Mitigation: Use a short-lived token for the current session when possible and remove BIGDATA_ACCESS_TOKEN from shell profiles or user environment storage after use. <br>
Risk: The skill can send the token and internal query results to configurable endpoints. <br>
Mitigation: Avoid endpoint overrides unless the host is controlled and trusted. <br>
Risk: The release has a suspicious security verdict from the authoritative scan evidence. <br>
Mitigation: Install only if the publisher is trusted with internal analytics credentials and query results. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mzhou1982/acceptance-rate-analysis-new) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown summaries with tables, status blocks, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a BIGDATA_ACCESS_TOKEN credential and may query internal metric APIs.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
