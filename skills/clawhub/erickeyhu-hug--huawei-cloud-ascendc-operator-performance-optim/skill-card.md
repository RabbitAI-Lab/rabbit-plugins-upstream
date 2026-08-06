## Description: <br>
Develop and optimize custom AscendC operators for Ascend NPU workloads by analyzing bottlenecks, applying performance optimizations, and validating results with CANN tooling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to optimize performance-critical AscendC custom operators, implement missing operators for Ascend NPU deployment, and validate functional accuracy and speedup with profiling results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Profiling helper scripts can remove existing OPPROF_* profiling output in the operator directory. <br>
Mitigation: Run helper scripts from a copied or dedicated operator directory and preserve any needed OPPROF_* results before profiling. <br>
Risk: Broad permissions on shared profiling output directories can expose or corrupt local profiling data. <br>
Mitigation: Avoid chmod 777 /tmp/opprof on shared machines and use a private per-user output directory instead. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-ascendc-operator-performance-optim) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [Verification Methods](references/verification-method.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>
- [Tiling Optimization Reference](references/tiling-prof.md) <br>
- [Data Copy Optimization Reference](references/data-copy-prof.md) <br>
- [API Usage Optimization Reference](references/api-usage-prof.md) <br>
- [Memory Optimization Reference](references/memory-prof.md) <br>
- [Pipeline Optimization Reference](references/pipeline-prof.md) <br>
- [Scalar Optimization Reference](references/scalar-prof.md) <br>
- [AscendC API Reference Guide](references/ascendc-api/GUIDE.md) <br>
- [AscendC Kernel Limitations and Pitfalls](references/ascendc-api/kernel-constraints.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline code and shell commands; profiling artifacts may include JSON, CSV, timeline data, and recommendation markdown.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an AscendC/CANN operator development environment and an operator source path or profiling data.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
