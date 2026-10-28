## Description:

Queries one Huawei Cloud ECS instance by ID and returns its details as text, JSON, or an optional Markdown file.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud operators and developers use this skill to inspect one Huawei Cloud ECS instance by ID for troubleshooting or as an input to follow-on workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unchecked command overrides and unvalidated region values can change what runs and where authenticated requests go.

Mitigation: Remove or restrict command overrides and validate region values against trusted Huawei Cloud endpoints before use.

Risk: The SDK fallback reads credentials directly from the environment.

Mitigation: Use a dedicated read-only cloud identity and keep credentials in the configured profile or environment.

Risk: Markdown export overwrites the selected file.

Mitigation: Choose a new, intended export path or preserve existing contents before exporting.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wlc-dev/skills/huawei-cloud-ecs-show)
- [KooCLI Installation & Credential Guide](references/cli-installation-guide.md)
- [Least-Privilege IAM Policy](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Huawei Cloud KooCLI Quick Start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown]

**Output Format:** [Human-readable instance details, raw JSON, or a Markdown document]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports one ECS instance per invocation; Markdown is written only when an export path is supplied.]

## Skill Version(s):

1.0.2 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
