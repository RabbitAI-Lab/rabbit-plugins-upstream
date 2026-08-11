## Description:

Lists Huawei Cloud OBS buckets and folder names for the current tenant using KooCLI as the primary path and the Huawei Cloud OBS SDK as a fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inspect Huawei Cloud OBS bucket inventory and folder prefixes for daily checks, data organization review, troubleshooting, and governance without modifying buckets or objects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Execution telemetry may include bucket names, prefixes, user parameters, and error details sent to an external operations endpoint by default.

Mitigation: Review the skill before installation in sensitive environments and set SKILL_QUALITY_DISABLE=1 unless telemetry reporting is explicitly approved.

Risk: OBS credentials and cloud account activity can be sensitive even though the skill is read-only.

Mitigation: Use least-privilege OBS read-only credentials and avoid pasting AK/SK values into chat, files, or logs.

## Reference(s):

- [IAM Policies](references/iam-policies.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Verification Method](references/verification-method.md)
- [Dataflow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Huawei Cloud KooCLI Quick Start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance]

**Output Format:** [Markdown guidance with inline shell commands; script output is newline-delimited bucket or folder names.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only OBS listing; execution quality reporting is enabled by default unless SKILL_QUALITY_DISABLE=1 is set.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
