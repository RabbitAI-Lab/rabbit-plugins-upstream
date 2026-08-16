## Description:

Queries Huawei Cloud SFS Turbo file systems for the current tenant or project and returns names or key attributes such as id, status, size, protocol, and region.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud operators, and storage administrators use this skill to inspect Huawei Cloud SFS Turbo inventory, retrieve SFS names, and review read-only storage attributes for daily checks or cost review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Default-on execution telemetry may send run information to an external endpoint.

Mitigation: Review telemetry acceptability before installation, set SKILL_QUALITY_DISABLE=1 when telemetry must not leave the environment, or restrict SKILL_QUALITY_ENDPOINT to an approved endpoint.

Risk: Cloud inventory commands require authenticated Huawei Cloud access and may expose storage inventory details in command output.

Mitigation: Use least-privilege IAM such as sfsturbo:shares:listShares, avoid pasting credentials into chat, and confirm region and output scope before running the command.

## Reference(s):

- [Skill Page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-sfsturbo-list)
- [IAM Policies](references/iam-policies.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Verification Method](references/verification-method.md)
- [Dataflow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands and JSON or plain-text command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return one SFS name per line or JSON lines with file-system attributes.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
