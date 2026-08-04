## Description: <br>
Calculates Machine FLOP Utilization (MFU) for Ascend NPU operators such as matmul, GEMM, and FlashAttention, with formulas, derivations, and result interpretation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and performance engineers use this skill to calculate MFU for Ascend NPU operators, compare implementation efficiency, and identify optimization opportunities from supplied operator dimensions, execution time, and hardware peak FLOPs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bottleneck diagnosis or optimization advice may be misleading when profiler data, tensor dimensions, execution time, peak FLOPs, or device assumptions are incomplete or incorrect. <br>
Mitigation: Require users to supply relevant profiling data and verify dimensions, units, chip model, precision mode, and peak FLOPs before acting on MFU results or optimization recommendations. <br>


## Reference(s): <br>
- [Ascend 910B Series Technical Specifications](https://e.huawei.com/cn/products/computing/ascend-910) <br>
- [MFU Calculation Methodology](references/mfu-calculation-methodology.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [FlashAttention Technical Paper](https://arxiv.org/abs/2205.14135) <br>
- [GEMM Performance Optimization Guide](https://developer.nvidia.com/cuda-gemm-performance) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Code, Guidance] <br>
**Output Format:** [Markdown with formulas, worked calculations, and optional Python snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs depend on user-supplied operator dimensions, execution time, peak TFLOPs, and device assumptions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
