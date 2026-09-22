## Description:

Huawei Cloud ECS monitoring skill using Cloud Eye Service (CES) for querying and analyzing Elastic Cloud Server CPU, memory, disk, network, and system metrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud operators, and support engineers use this skill to inspect Huawei Cloud ECS performance, query CES metrics, analyze trends, and troubleshoot resource bottlenecks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad CLI installation guidance includes remote installer commands, including non-interactive execution.

Mitigation: Review the CLI setup steps before use, verify the download source, and prefer a least-privilege local installation path.

Risk: Optional cloud permissions and actions go beyond read-only ECS and CES monitoring.

Mitigation: Use a read-only, project-scoped IAM policy for ECS list/get and CES metrics access; avoid remote console, instance action, tagging, and scaling permissions unless they are explicitly required.

Risk: The skill depends on Huawei Cloud credentials and IAM permissions.

Mitigation: Configure credentials outside the agent session, avoid exposing AK/SK values, and verify access with credential-status and least-privilege permission checks before running metric queries.

## Reference(s):

- [Huawei Cloud ECS Monitoring Skill](artifact/SKILL.md)
- [Huawei Cloud CES Metrics Reference for ECS](artifact/references/ces-metrics-reference.md)
- [Huawei Cloud CLI Commands for ECS Monitoring](artifact/references/related-commands.md)
- [IAM Policies for Huawei Cloud ECS Monitoring](artifact/references/iam-policies.md)
- [Huawei Cloud ECS Monitoring Best Practices](artifact/references/best-practices.md)
- [Huawei Cloud KooCLI Installation Guide](artifact/references/cli-installation-guide.md)
- [Huawei Cloud ECS Monitoring Troubleshooting Guide](artifact/references/troubleshooting-guide.md)
- [Huawei Cloud ECS User Guide](https://support.huaweicloud.com/usermanual-ecs/ecs_03_1001.html)
- [Huawei Cloud CLI Reference Documentation](https://support.huaweicloud.com/function-hcli/index.html)
- [Huawei Cloud CLI Version Information](https://support.huaweicloud.com/wtsnew-hcli/index.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown monitoring reports with inline Huawei Cloud CLI commands and metric tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CES metric summaries, trend analysis, troubleshooting recommendations, and credential or IAM setup guidance.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
