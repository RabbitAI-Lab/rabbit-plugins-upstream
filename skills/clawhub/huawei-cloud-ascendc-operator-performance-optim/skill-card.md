## Description: <br>
Develops and optimizes custom AscendC operators, analyzes performance bottlenecks, and validates optimizations for Ascend NPU workloads using the CANN toolkit. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to investigate AscendC operator bottlenecks, implement targeted operator optimizations, and validate functional correctness and performance improvement on Ascend NPU workloads. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill includes unsafe chmod 777 guidance for profiling output directories. <br>
Mitigation: Use a private profiling output directory with restrictive permissions instead of following chmod 777 guidance. <br>
Risk: Included profiling scripts delete OPPROF_* profiling outputs in the target operator workspace. <br>
Mitigation: Run the scripts only in an operator workspace where deleting existing OPPROF_* outputs is acceptable, and keep backups when prior profiling data must be preserved. <br>
Risk: Overbroad activation language may cause the skill to be used outside AscendC/CANN operator work. <br>
Mitigation: Install and use the skill only for AscendC/CANN custom operator development, profiling, and optimization tasks. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-ascendc-operator-performance-optim) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>
- [AscendC API Guide](references/ascendc-api/GUIDE.md) <br>
- [Kernel Constraints](references/ascendc-api/kernel-constraints.md) <br>
- [Tiling Optimization Reference](references/tiling-prof.md) <br>
- [Data Copy Optimization Reference](references/data-copy-prof.md) <br>
- [Memory Optimization Reference](references/memory-prof.md) <br>
- [Pipeline Optimization Reference](references/pipeline-prof.md) <br>
- [Scalar Optimization Reference](references/scalar-prof.md) <br>
- [API Usage Optimization Reference](references/api-usage-prof.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with code blocks, shell commands, JSON/CSV profiling report descriptions, and optimization recommendations.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference generated profiling artifacts such as summary.json, operator_stats.csv, timeline.json, recommendations.md, and before/after comparison reports.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
