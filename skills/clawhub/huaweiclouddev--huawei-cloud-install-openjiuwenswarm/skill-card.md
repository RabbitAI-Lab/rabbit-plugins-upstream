## Description:

Installs, configures, and starts JiuwenSwarm locally inside a Huawei Cloud development container, then returns the running service URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers working in Huawei Cloud development containers use this skill to run a standardized local JiuwenSwarm installation or restart flow. The skill handles runtime download, extraction, configuration, service startup, and final URL retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill performs high-impact local system changes, including package installation, global command changes, service startup, and process termination.

Mitigation: Run it only in a disposable Huawei Cloud development container and review write-operation confirmation points before execution.

Risk: The skill copies a Huawei Cloud API key from the kernel keyring into /root/.jiuwenswarm/config/.env, and verification guidance can print that file.

Mitigation: Use it only where that local credential copy is acceptable, keep the .env file private, and do not share verification output containing its contents.

Risk: The skill downloads a runtime archive and performs network activity during installation.

Mitigation: Confirm the container network policy and expected download source before running the installer.

## Reference(s):

- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Huawei Cloud CodeDao Skill Development Standards](https://developer.huawei.com/consumer/cn/doc/service/skill-development-standards-0000002592931546)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown instructions, shell command invocations, JSON error objects, progress text, and a final service URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs five sequential local phases and emits the Huawei Cloud workspace URL after successful startup.]

## Skill Version(s):

1.0.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
