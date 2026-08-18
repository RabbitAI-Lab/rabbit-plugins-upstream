## Description:

Based on Huawei Cloud COC (Cloud Operations Center) APIs for script management and remote execution, this skill supports creating custom scripts (Shell, Python, Bat) and batch execution on target host instances via UniAgent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations engineers use this skill to create, list, inspect, delete, execute, and query Huawei Cloud COC scripts for Flexus L instance operations such as deployment, maintenance, log cleanup, and emergency response.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can execute remote scripts as root on Huawei Cloud Flexus L instances.

Mitigation: Use least-privilege or temporary credentials, require an external approval process for production hosts, test scripts on one instance first, and verify the script UUID, target instance, region, execution user, timeout, and risk level before execution.

Risk: Huawei Cloud AK/SK or temporary tokens can be exposed if passed on the command line or echoed in conversation.

Mitigation: Prefer environment variables for credentials, avoid command-line AK/SK in shared environments, never print credential values, and rotate credentials according to the operator's key policy.

Risk: The skill can delete cloud scripts without a built-in confirmation step.

Mitigation: Confirm the script UUID and ownership before deletion, keep script source under version control, and use change-control review for shared or production scripts.

Risk: Execution output and script details may include host identifiers, logs, or sensitive operational data.

Mitigation: Limit output sharing to authorized operators and redact secrets, host identifiers, and operational details before copying results into tickets or conversations.

## Reference(s):

- [IAM Policy Configuration](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Project Dependencies Configuration](scripts/pyproject.toml)
- [Huawei Cloud COC SDK Package](https://pypi.org/project/huaweicloudsdkcoc/)
- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-flexus-l-server-scripts-excute)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON-style command responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Operations can return script UUIDs, execution UUIDs, paginated script summaries, script details, deletion status, and execution status or logs.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
