## Description:

Provides temporary SSH remote connection for Huawei Cloud Ascend devices with dynamic host, port, user, and password input, plus disk management, NPU monitoring, container management, security auditing, and log analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations engineers use this skill to connect to Huawei Cloud Ascend servers over SSH, monitor NPU health, manage disks and containers, and troubleshoot remote systems.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill performs SSH remote administration and can run broad privileged actions on target systems.

Mitigation: Use it only with hosts you control, prefer least-privilege non-root accounts, and review privileged operations before execution.

Risk: Security evidence reports disabled SSH host verification.

Mitigation: Verify SSH host keys outside the skill before connecting to any target host.

Risk: Security evidence reports that raw or one-shot commands can run without the promised confirmation prompts.

Mitigation: Treat every submitted command as executable immediately and independently confirm destructive or sensitive commands before use.

Risk: SSH key listing and key generation are sensitive administrative actions.

Mitigation: Limit key-management operations to authorized administrators and review generated or listed keys for exposure.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-ascend-remote-connect)
- [IAM Permission Policy](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Troubleshooting Guide](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Code, Guidance]

**Output Format:** [Markdown with inline bash code blocks and structured command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Remote command results may include target host, executed command, exit code, stdout, stderr, and duration.]

## Skill Version(s):

1.0.1 (source: server release evidence; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
