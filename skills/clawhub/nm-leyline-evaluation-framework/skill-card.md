## Description: <br>
Provides weighted scoring, rubrics, and decision-threshold patterns. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, reviewers, and release teams use this skill to define evaluation criteria, assign weights, score artifacts, and map results to clear approval or review actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad activation triggers may cause the skill to influence evaluation or quality-gate discussions when a narrower framework is intended. <br>
Mitigation: Review and narrow trigger phrases before use in automated workflows where precise activation matters. <br>
Risk: Threshold-based scoring can produce misleading decisions if criteria, weights, or veto conditions are copied without context. <br>
Mitigation: Require reviewers to document criteria, weight derivation, decision thresholds, and sensitivity checks before relying on automated or high-impact decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-leyline-evaluation-framework) <br>
- [Project homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline) <br>
- [Scoring Patterns](modules/scoring-patterns.md) <br>
- [Decision Thresholds](modules/decision-thresholds.md) <br>
- [Evaluation Rubric](modules/evaluation-rubric.md) <br>
- [Quality Metrics](modules/quality-metrics.md) <br>
- [Multi-Metric Evaluation Methodology](modules/multi-metric-evaluation-methodology.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with YAML and Python examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only evaluation framework; no executable integration or API access is provided.] <br>

## Skill Version(s): <br>
1.9.16 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
