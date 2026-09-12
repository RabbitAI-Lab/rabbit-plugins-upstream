## Description:

Manages Huawei Cloud SMN topics, subscriptions, message templates, and publishing, plus DMS Kafka, RabbitMQ, and RocketMQ instances and Kafka topics through KooCLI-backed query, diagnosis, management, and destructive-operation workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inspect, configure, publish to, and clean up Huawei Cloud SMN notification resources and DMS message-queue resources while following risk-gated confirmation steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation guidance includes a one-line KooCLI installer flow that can expose users to unsafe execution if the script is not independently verified.

Mitigation: Install KooCLI only from an official Huawei Cloud package or a signed/checksummed channel, and review the installer before execution.

Risk: The skill can create, publish to, confirm, and delete cloud messaging resources, which can cause cost, side effects, or data loss.

Mitigation: Use a dedicated least-privilege Huawei Cloud identity and require manual review plus explicit confirmation for all management and destructive operations.

Risk: Command-line passwords, subscription confirmation tokens, and resource identifiers may be exposed through shell history, logs, or process listings.

Mitigation: Avoid passing secrets or confirmation tokens on command lines; prefer an authenticated KooCLI profile, environment secrets set out of band, and manual handling for sensitive tokens.

## Reference(s):

- [IAM Policies](references/iam-policies.md)
- [KooCLI Installation & Authentication Guide](references/cli-installation-guide.md)
- [Engine & Operation Reference](references/engine-operation-reference.md)
- [Verification Method](references/verification-method.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [Huawei Cloud KooCLI Quick Start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, command previews, JSON command output summaries, and concise analysis text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Huawei Cloud resource identifiers and operation status; credential values should not be printed.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
