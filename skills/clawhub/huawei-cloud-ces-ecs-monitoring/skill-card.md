## Description: <br>
Huawei Cloud CES ECS Monitoring helps agents query and analyze Huawei Cloud ECS instance metrics through Cloud Eye Service and Huawei Cloud CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, cloud operators, and site reliability engineers use this skill to inspect ECS performance, query CPU, memory, disk, network, and system metrics, and troubleshoot resource issues in Huawei Cloud environments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review found that the monitoring workflow can involve broader cloud or administrative permissions than ECS/CES read-only monitoring requires. <br>
Mitigation: Constrain use to the minimum read-only IAM policy needed for listing ECS instances and reading CES metrics; avoid full-access, remote console, instance action, alarm mutation, and IAM enumeration permissions unless a separate administrative workflow deliberately requires them. <br>
Risk: Setup and cleanup guidance may include local commands that change CLI configuration, install software, or remove files. <br>
Mitigation: Review sudo, curl-to-bash, and cleanup commands before execution, verify the source, understand which local configuration will change, and keep backups of any Huawei CLI profiles that may be needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-ces-ecs-monitoring) <br>
- [Huawei Cloud official ECS documentation](https://support.huaweicloud.com/usermanual-ecs/ecs_03_1001.html) <br>
- [Huawei Cloud CLI reference documentation](https://support.huaweicloud.com/function-hcli/index.html) <br>
- [Huawei Cloud CLI Commands for ECS Monitoring](artifact/references/related-commands.md) <br>
- [Huawei Cloud CES Metrics Reference for ECS](artifact/references/ces-metrics-reference.md) <br>
- [IAM Policies for Huawei Cloud ECS Monitoring](artifact/references/iam-policies.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, markdown, configuration] <br>
**Output Format:** [Markdown with Huawei Cloud CLI command examples and monitoring report guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include metric summaries, troubleshooting steps, and recommended next actions for ECS monitoring.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
