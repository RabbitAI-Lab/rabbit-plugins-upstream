## Description:

医疗器械进出口路径判定器--基于官方规则源的零依赖决策支持工具，JSON IR 输出，覆盖TH-MED-005域（医疗器械全链路）。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and compliance reviewers use this skill as a decision-support CLI for routing medical-device import and export scenarios against stated NMPA, export certificate, FDA, and EU MDR rule sources. Its outputs require human review against current official regulatory texts before operational use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The tool may produce outdated or incomplete regulatory routing guidance if official NMPA, FDA, EU MDR, or export-certificate requirements have changed.

Mitigation: Treat outputs as decision support only and verify each result against current official regulatory texts and qualified human review.

Risk: CLI and documentation inconsistencies may cause users to provide unsupported arguments or misunderstand required inputs.

Mitigation: Check the command help and use the implemented inputs direction, is_registered, and dest_region when validating results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/import-export-router)
- [LGD theory](https://medxpert.cn/theory)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [JSON IR from a command-line interface, with concise text guidance in documentation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes rc status codes and GB45438-2025 aigc_mark metadata; no network or credential use was identified in the provided evidence.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
