## Description:

Lists Huawei Cloud ECS instances in a selected region and exports the inventory as an Excel workbook, JSON, or a text table.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud operators and developers use the skill to create a local inventory report of ECS instances for a selected Huawei Cloud region. It supports operational review and reporting without changing cloud resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment flags weakened download security during setup.

Mitigation: Replace the setup helper with dependency installation in an isolated environment using certificate-verified package sources, and keep cloud credentials out of the setup environment.

Risk: The security assessment notes that credential instructions contradict the code; the SDK fallback reads credentials from the environment.

Mitigation: Use credentials limited to ECS listing, follow the current official KooCLI installation guidance, and verify the active credential path before use.

Risk: Exported reports contain instance identifiers and network addresses.

Mitigation: Store and share generated reports according to the sensitivity of cloud inventory data.

## Reference(s):

- [Huawei Cloud KooCLI Quick Start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [ClawHub skill release](https://clawhub.ai/wlc-dev/skills/huawei-cloud-ecs-export-excel)

## Skill Output:

**Output Type(s):** [Files, JSON, Text]

**Output Format:** [Excel workbook (.xlsx), JSON, or a plain-text table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Region-aware inventory with optional status and name filters; workbook is saved locally.]

## Skill Version(s):

1.0.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
