## Description:

Huawei Cloud CTS trace management helps agents query and analyze Cloud Trace Service audit data, review retention posture, and prepare tracker or notification lifecycle commands through the hcloud CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud operators, security engineers, and compliance teams use this skill to inspect Huawei Cloud CTS trackers, audit traces, notifications, service operations, and trace resources. It also guides retention analysis and prepares create/delete commands that require explicit confirmation before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic quality reporting can send masked run inputs, outputs, errors, and possible stack data to the configured Huawei endpoint.

Mitigation: Enable reporting only in approved environments, pin or review SKILL_QUALITY_ENDPOINT and SKILL_QUALITY_INSECURE, or set SKILL_QUALITY_DISABLE=1 where external reporting is not approved.

Risk: Create and delete actions can change CTS trackers or notifications.

Mitigation: Use read-only CTS permissions by default and require explicit user confirmation after previewing the exact hcloud command for every write action.

Risk: Cloud credentials and audit data may be exposed if copied into prompts, scripts, or logs.

Mitigation: Use hcloud profiles or approved environment variables, avoid hardcoding AK/SK values, and mask credential-like values in outputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-cts-trace-management)
- [hcloud KooCLI quick start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [CLI installation guide](references/cli-installation-guide.md)
- [IAM policies](references/iam-policies.md)
- [Verification method](references/verification-method.md)
- [Data flow diagram](references/dataflow-diagram.md)
- [Acceptance criteria](references/acceptance-criteria.md)
- [Test report](references/test-report.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline hcloud CLI commands and JSON-oriented result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write operations are previewed as exact commands and require explicit user confirmation before execution.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
