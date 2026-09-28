## Description:

Provides Huawei Cloud CTS audit and tracker management guidance through the hcloud CLI, covering trace queries, notifications, tracker lifecycle, and retention compliance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud operators, and security engineers use this skill to query Huawei Cloud CTS audit traces, inspect trackers and notifications, and analyze retention posture. It also proposes CTS create/delete commands with preview and explicit confirmation before write operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled quality-reporting wrapper can send agent prompt/context data and up to 6000 characters of cloud command output to Huawei reporting endpoints by default.

Mitigation: Set SKILL_QUALITY_REPORT=0 or SKILL_QUALITY_DISABLE=1 before running if reporting is not acceptable, and review reporting endpoint settings before deployment.

Risk: The CLI bootstrap can make persistent local changes under ~/.local/bin and shell profile files.

Mitigation: Review scripts/ensure_cli.sh before use and remove the installed wrapper or PATH profile entries if persistent installation is not desired.

Risk: CTS create/delete operations can change cloud audit tracker and notification configuration.

Mitigation: Use the documented preview-and-confirm flow, validate IAM permissions and OBS or SMN prerequisites, and execute write commands only after explicit approval.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-cts-trace-management)
- [hcloud (KooCLI) Installation & Authentication Guide](references/cli-installation-guide.md)
- [IAM Policies for Huawei Cloud CTS](references/iam-policies.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Huawei Cloud hcloud quick start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown with inline shell commands and JSON result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write operations require preview and explicit user confirmation; quality reporting can be disabled with documented environment variables.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
