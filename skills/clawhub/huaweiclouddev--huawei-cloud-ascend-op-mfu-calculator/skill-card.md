## Description: <br>
Calculate MFU (Machine FLOP Utilization) for operators like matmul, GEMM, and FlashAttention on Ascend NPU, providing clear formulas and derivation steps. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and performance engineers use this skill to calculate and interpret Machine FLOP Utilization for Ascend NPU operators, including matmul, GEMM, and FlashAttention. It helps compare operator efficiency and identify optimization opportunities from dimensions, timing, and hardware peak FLOPs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Profiling files or performance data may contain workload details the user did not intend to analyze. <br>
Mitigation: Provide only profiling files or performance data intended for MFU analysis. <br>
Risk: MFU results can be misleading if operator dimensions, execution time, hardware peak FLOPs, or sparse attention settings are incorrect. <br>
Mitigation: Verify dimensions, timing units, chip model, precision mode, and FlashAttention sparse mode before using the result for optimization decisions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-ascend-op-mfu-calculator) <br>
- [Publisher Profile](https://clawhub.ai/user/huaweiclouddev) <br>
- [MFU Calculation Methodology](references/mfu-calculation-methodology.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Ascend 910B Series Technical Specifications](https://e.huawei.com/cn/products/computing/ascend-910) <br>
- [FlashAttention Technical Paper](https://arxiv.org/abs/2205.14135) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Code, Guidance] <br>
**Output Format:** [Markdown with formulas, calculation steps, and optional Python snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses user-provided operator dimensions, execution time, device model, and peak TFLOPs to calculate and explain MFU.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
