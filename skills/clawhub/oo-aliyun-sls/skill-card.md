## Description: <br>
Alibaba Cloud SLS helps agents search and read Alibaba Cloud Simple Log Service projects, logstores, histograms, and logs through the OOMOL `oo` CLI connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and support engineers use this skill to inspect Alibaba Cloud SLS projects, logstores, histograms, and log query results from an OOMOL-connected account. It is intended for read-oriented log investigation with explicit project, region, logstore, time range, and query scope. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: SLS logs can contain sensitive operational or personal data. <br>
Mitigation: Provide explicit project, region, logstore, time range, and query scope, and review ambiguous requests before allowing log queries. <br>
Risk: The skill executes local `oo` CLI commands against an OOMOL-connected account. <br>
Mitigation: Inspect the live connector schema before constructing payloads and limit execution to the documented read actions unless the user explicitly confirms a state-changing action. <br>


## Reference(s): <br>
- [Alibaba Cloud Simple Log Service](https://www.alibabacloud.com/product/log-service) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-aliyun-sls) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before building action payloads; connector responses include data and an execution identifier.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
