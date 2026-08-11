## Description:

Huawei Cloud RDS Troubleshoot guides agents through MySQL and PostgreSQL RDS diagnostics, slow-log analysis, parameter tuning, and user-confirmed remediation using KooCLI first with SDK and REST fallbacks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations engineers use this skill to troubleshoot Huawei Cloud RDS MySQL and PostgreSQL incidents, inspect instance health, analyze slow or error logs, and plan confirmed remediation steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide operational RDS changes such as restart, parameter updates, backup creation, or restore, which can affect availability or data state.

Mitigation: Use read-only diagnosis first and require explicit user confirmation before any mutating command.

Risk: Overbroad IAM permissions can give the agent more access than needed for routine troubleshooting.

Mitigation: Prefer RDS ReadOnlyAccess for diagnosis and grant write permissions only for confirmed remediation.

Risk: Huawei Cloud AK/SK credentials can be exposed through hardcoding, shell history, shared terminals, or CI logs.

Mitigation: Use hcloud profiles or environment variables, keep credentials tightly scoped or short-lived, and avoid printing or storing secret values.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-rds-troubleshoot)
- [CLI Installation Guide](artifact/references/cli-installation-guide.md)
- [IAM Policies](artifact/references/iam-policies.md)
- [Troubleshooting Guide](artifact/references/troubleshooting-guide.md)
- [Verification Method](artifact/references/verification-method.md)
- [Dataflow Diagram](artifact/references/dataflow-diagram.md)
- [Acceptance Criteria](artifact/references/acceptance-criteria.md)
- [Huawei Cloud KooCLI quick start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Interactive Markdown guidance with inline shell commands and concise diagnostic summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One diagnostic step at a time; mutating operations require explicit user confirmation.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
