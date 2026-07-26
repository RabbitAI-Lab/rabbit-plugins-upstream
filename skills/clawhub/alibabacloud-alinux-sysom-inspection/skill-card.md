## Description: <br>
Inspect ECS instance health, detect anomalies in memory, disk, CPU, load, and resource leaks, and trigger memory-focused diagnosis when critical memory issues are detected. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sdk-team](https://clawhub.ai/user/sdk-team) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operations engineers use this skill to run Alibaba Cloud SysOM inspections on ECS instances, review anomalies, and optionally trigger memory diagnosis for troubleshooting and risk warning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use Alibaba Cloud credentials for SysOM operations including activation, agent installation, inspection, and diagnosis. <br>
Mitigation: Use a least-privilege RAM policy, review interactive prompts, and run only for intended ECS instances. <br>
Risk: Broad instance listing can expose more infrastructure scope than needed. <br>
Mitigation: Pass --instance-id when possible and limit RAM permissions to the required SysOM actions. <br>
Risk: Automatic memory diagnosis may start follow-up diagnosis after a memory anomaly is detected. <br>
Mitigation: Use --disable-memgraph-diagnosis when automatic diagnosis is not desired. <br>


## Reference(s): <br>
- [RAM Policies](references/ram-policies.md) <br>
- [Inspection Report Template](references/report-template.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/sdk-team/skills/alibabacloud-alinux-sysom-inspection) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance] <br>
**Output Format:** [Terminal text, optional JSON, and Markdown inspection reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write inspection reports under inspection-reports/ and can prompt before SysOM activation or agent installation.] <br>

## Skill Version(s): <br>
0.0.3 (source: server release metadata; artifact frontmatter and pyproject.toml show 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
