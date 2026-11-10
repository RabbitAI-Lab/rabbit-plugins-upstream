## Description:

Calculates Machine FLOP Utilization for Ascend NPU operators and analyzes profiling data to identify performance bottlenecks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to calculate MFU for Ascend operators, compare operator efficiency, and interpret profiling data for optimization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup helper can download and install an unverified CLI release automatically.

Mitigation: Run the bundled Python diagnoser directly. Before enabling the CLI, require a pinned, integrity-verified release.

Risk: The CLI wrapper reports telemetry, while the collected data and reporting destinations were unavailable for verification.

Mitigation: Prefer direct diagnoser use or set SKILL_QUALITY_REPORT=0; review documented data collection and reporting destinations before enabling the CLI.

## Reference(s):

- [Ascend 910B Series Technical Specifications](https://e.huawei.com/cn/products/computing/ascend-910)
- [MFU Calculation Methodology](artifact/references/mfu-calculation-methodology.md)
- [MFU Verification Method](artifact/references/verification-method.md)
- [FlashAttention Technical Paper](https://arxiv.org/abs/2205.14135)
- [ClawHub skill release](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-ascend-op-mfu-calculator)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Text]

**Output Format:** [Markdown or plain text with calculation results and optimization recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include per-operator bottleneck classifications and prioritized recommendations from profiling data.]

## Skill Version(s):

1.0.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
