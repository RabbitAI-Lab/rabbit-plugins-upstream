## Description:

Diagnoses GPU device status, driver issues, and hardware failures on Alibaba Cloud ECS GPU instances using ECS console diagnostics and Cloud Assistant commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud operators and infrastructure engineers use this skill to validate Alibaba Cloud ECS GPU instances, run immediate or scheduled GPU diagnoses, and interpret driver, device, and hardware findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use Alibaba Cloud credentials to run a fixed remote shell diagnostic command on ECS instances.

Mitigation: Review the decoded command before use, confirm target instance IDs and regions, and grant only the RAM permissions needed for diagnosis.

Risk: The skill can create recurring Cloud Assistant schedules when scheduled diagnosis is requested.

Mitigation: Confirm the schedule and target instance list before creation, and stop scheduled invocations when they are no longer needed.

Risk: The security assessment reports that the skill can run remote diagnostics and create recurring cloud tasks with too little explicit user confirmation.

Mitigation: Prefer explicitly choosing the diagnosis method, review commands before execution, and verify Alibaba Cloud CLI installation sources before any sudo install or update.

## Reference(s):

- [Alibaba Cloud CLI Installation Guide](references/cli-installation.md)
- [RAM Permission List](references/ram-policies.md)
- [Alibaba Cloud GPU Driver Installation Guide](https://help.aliyun.com/zh/egs/install-a-gpu-driver-on-a-gpu-accelerated-compute-optimized-linux-instance)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and diagnostic result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Streams results as available and groups findings by diagnosis method and instance.]

## Skill Version(s):

0.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
