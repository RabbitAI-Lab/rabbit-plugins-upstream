## Description:

Manages Huawei Cloud DDS and DCS instances through hcloud CLI commands and Huawei Cloud SDK fallbacks for query, analysis, creation, backup, restart, and deletion workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations teams use this skill to inspect, analyze, and operate Huawei Cloud DDS and DCS resources with documented CLI and SDK commands, including guarded mutating operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Default quality reporting may send prompts, session metadata, token counts, steps, and cloud command output to the configured endpoint.

Mitigation: Review the reporting endpoint and disable reporting before use with SKILL_QUALITY_DISABLE=1 or SKILL_QUALITY_REPORT=0 when that data should remain local.

Risk: The bundled installer can persist a local wrapper under the user's home directory and update shell startup files for PATH configuration.

Mitigation: Install and test in an isolated environment first, review scripts/ensure_cli.sh, and remove the wrapper or PATH entries if persistent local changes are not acceptable.

Risk: DDS and DCS management commands can create billable resources, delete instances, restart services, or use broad wildcard IAM permissions.

Mitigation: Prefer the least-privilege read-only or scoped IAM policies, require explicit confirmation for mutating operations, and create backups before destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-dds-dcs-instance-management)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies for DDS and DCS](references/iam-policies.md)
- [Detailed Command Reference](references/related-commands.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash, Python, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include hcloud commands, Huawei Cloud SDK snippets, IAM policy examples, and operational risk notes.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
