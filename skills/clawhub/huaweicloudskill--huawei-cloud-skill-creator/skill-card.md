## Description:

Huawei Cloud Skill Creator guides agents through a six-phase workflow for creating Huawei Cloud skills, including requirements gathering, CLI/SDK/API research, skill package generation, testing, cleanup, and compliance validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud engineers use this skill to package Huawei Cloud operational workflows into structured agent skills with documented prerequisites, command patterns, tests, and validation steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires Huawei Cloud credentials and may guide agents through workflows that test or operate against cloud services.

Mitigation: Use least-privilege credentials, verify credential status without exposing secrets, and require explicit confirmation for mutating operations.

Risk: Cloud commands are routed through an auto-installed telemetry CLI whose data scope is not fully defined in the evidence.

Mitigation: Review and approve skill-quality-cli installation and telemetry behavior before use, or set SKILL_QUALITY_REPORT=0 when telemetry is not acceptable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-skill-creator)
- [KooCLI Quick Start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [KooCLI Installation](https://support.huaweicloud.com/cli/index.html)
- [Huawei Cloud SDK Center](https://console.huaweicloud.com/apiexplorer/#/sdkcenter)
- [Huawei Cloud API Explorer](https://console.huaweicloud.com/apiexplorer/#/openapi)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [IAM Policies](references/iam-policies.md)
- [Related Commands](references/related-commands.md)
- [Verification Method](references/verification-method.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash, Python, JSON, and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces complete skill directory guidance, reference documentation, validation scripts, test templates, and phase summaries.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
