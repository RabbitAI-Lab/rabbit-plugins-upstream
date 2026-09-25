## Description:

Calculates Machine FLOP Utilization (MFU) for Ascend NPU operators such as matmul, GEMM, and FlashAttention, with formulas, worked steps, and optimization guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and performance engineers use this skill to calculate operator MFU from dimensions, execution time, and hardware peak FLOPs. It helps compare operator implementations, interpret utilization results, and identify optimization opportunities for Ascend NPU workloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Profiler CSVs and performance details can reveal workload characteristics.

Mitigation: Only provide profiler files and performance details that are intended for analysis in the current agent session.

Risk: Incorrect hardware peak FLOPs values or chip model assumptions can produce misleading MFU results.

Mitigation: Verify peak FLOPs values against current vendor documentation and confirm the target Ascend model and precision mode before relying on results.

## Reference(s):

- [Ascend 910B Series Technical Specifications](https://e.huawei.com/cn/products/computing/ascend-910)
- [MFU Calculation Methodology](references/mfu-calculation-methodology.md)
- [Verification Method](references/verification-method.md)
- [FlashAttention Technical Paper](https://arxiv.org/abs/2205.14135)

## Skill Output:

**Output Type(s):** [text, markdown, code, guidance]

**Output Format:** [Markdown guidance with formulas, calculations, interpretation notes, and optional Python snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use profiler timing data and user-provided hardware peak FLOPs values.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
