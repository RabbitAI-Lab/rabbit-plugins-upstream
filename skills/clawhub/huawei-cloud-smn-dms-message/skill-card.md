## Description:

Manages Huawei Cloud SMN topics, subscriptions, message templates, message publishing, and DMS Kafka, RabbitMQ, and RocketMQ instances through KooCLI-backed guidance and commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inspect, diagnose, create, publish to, and delete Huawei Cloud SMN and DMS messaging resources while following KooCLI authentication and command-preview practices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Create, publish, confirm, and delete operations can change cloud resources, incur charges, or remove data if executed without adequate review.

Mitigation: Use the preview mode for R1/R2 actions, inspect the exact KooCLI command, and require explicit human approval before execution.

Risk: Overbroad Huawei IAM permissions can expand the impact of mistaken or destructive commands.

Mitigation: Use a least-privilege Huawei IAM principal and prefer read-only SMN/DMS permissions unless resource changes are required.

Risk: Credentials, RabbitMQ passwords, subscription tokens, and endpoint secrets may be exposed if passed through chat or logged command lines.

Mitigation: Configure credentials out of band with a local hcloud profile or environment variables, avoid printing secrets, and review command history and logs for sensitive arguments.

Risk: The KooCLI installer source and command parameters may drift over time.

Mitigation: Verify the installer through official Huawei Cloud documentation and run hcloud help for the target service and operation before executing non-trivial commands.

## Reference(s):

- [KooCLI Installation & Authentication Guide](references/cli-installation-guide.md)
- [IAM Policies for huawei-cloud-smn-dms-message](references/iam-policies.md)
- [Engine & Operation Reference - SMN + DMS](references/engine-operation-reference.md)
- [Verification Method](references/verification-method.md)
- [Security Audit Guide](references/security-audit-guide.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Huawei Cloud KooCLI Quick Start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Analysis, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON-oriented command output summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces KooCLI command previews for create, publish, confirm, and delete workflows; read-only queries may execute directly when configured.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
