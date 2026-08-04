## Description: <br>
Huawei Cloud CES ECS Monitoring helps an agent query and analyze Elastic Cloud Server CPU, memory, disk, network, and system metrics through Huawei Cloud Cloud Eye Service. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, cloud operators, and SREs use this skill to inspect Huawei Cloud ECS performance, troubleshoot resource bottlenecks, and produce monitoring recommendations from CES metrics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence flags broader Huawei Cloud permissions and credential handling than monitoring requires. <br>
Mitigation: Use a dedicated least-privilege Huawei Cloud identity limited to ECS list/get and CES metrics read, and avoid full-access, IAM-enumeration, or ECS-action permissions unless explicitly needed. <br>
Risk: The skill can lead an agent to use local Huawei Cloud CLI credentials and installer workflows. <br>
Mitigation: Inspect or verify the CLI installer before use, configure credentials outside the agent conversation, and do not mount normal ~/.hcloud credentials into containers. <br>


## Reference(s): <br>
- [Huawei Cloud ECS Monitoring Skill](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-ces-ecs-monitoring) <br>
- [Huawei Cloud ECS Monitoring Skill Acceptance Criteria](references/acceptance-criteria.md) <br>
- [Huawei Cloud ECS Monitoring Best Practices](references/best-practices.md) <br>
- [Huawei Cloud ECS Metrics Reference](references/ces-metrics-reference.md) <br>
- [Huawei Cloud CLI Installation Guide](references/cli-installation-guide.md) <br>
- [Huawei Cloud ECS Monitoring IAM Policies](references/iam-policies.md) <br>
- [Huawei Cloud ECS Monitoring Related Commands](references/related-commands.md) <br>
- [Huawei Cloud ECS Monitoring Troubleshooting Guide](references/troubleshooting-guide.md) <br>
- [Huawei Cloud ECS Monitoring Skill Verification Method](references/verification-method.md) <br>
- [Huawei Cloud ECS Monitoring Documentation](https://support.huaweicloud.com/usermanual-ecs/ecs_03_1001.html) <br>
- [Huawei Cloud CLI Reference Documentation](https://support.huaweicloud.com/function-hcli/index.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown monitoring reports with inline Huawei Cloud CLI commands and metric tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include CES metric summaries, trend analysis, troubleshooting recommendations, and Huawei Cloud CLI command examples.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
