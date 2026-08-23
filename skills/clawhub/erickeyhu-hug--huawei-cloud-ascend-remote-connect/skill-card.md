## Description:

Provides temporary SSH remote connection for Huawei Cloud Ascend devices with dynamic connection parameters, NPU monitoring, disk and container management, security auditing, and log analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure operators use this skill to connect to authorized Huawei Cloud Ascend servers over SSH, monitor Ascend NPU health, manage disks and containers, inspect logs, and troubleshoot system issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can exercise broad SSH administration authority over remote Ascend servers.

Mitigation: Use only with authorized hosts and least-privilege, non-root accounts; restrict SSH access to trusted networks and review requested operations before execution.

Risk: Passwords and command outputs such as environment variables, logs, crontabs, and authorized keys may be sensitive.

Mitigation: Prefer key-based authentication, avoid exposing inline passwords, and treat returned system output as confidential.

Risk: Promised confirmation safeguards may not consistently apply to one-shot or raw command paths.

Mitigation: Do not rely on automated confirmations as the only control; manually review destructive commands and avoid raw execution for untrusted requests.

## Reference(s):

- [IAM Permission Policy](references/iam-policies.md)
- [Troubleshooting Guide](references/troubleshooting.md)
- [Verification Method](references/verification-method.md)
- [ClawHub Skill Page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-ascend-remote-connect)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance and structured SSH command output with stdout, stderr, exit code, target, and duration fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include remote administration results, troubleshooting suggestions, and sensitive system output from authorized target servers.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
