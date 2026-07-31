## Description: <br>
Provides weighted scoring, rubrics, and decision-threshold patterns. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and reviewers use this skill to design reusable evaluation rubrics, weighted scoring systems, quality gates, and decision thresholds for artifacts, proposals, code, documentation, and skill releases. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional measurement commands may be run in a repository without enough local review. <br>
Mitigation: Review and adapt commands before running them, preferably in a controlled checkout or disposable working tree. <br>
Risk: Broad activation may surface the framework in general quality or evaluation conversations. <br>
Mitigation: Apply the skill only when the task needs structured scoring, rubrics, metrics, quality gates, or decision thresholds. <br>
Risk: Verification text in the artifact may not match the documentation-only nature of the skill. <br>
Mitigation: Treat verification lines as prompts for local validation and confirm each referenced command exists before relying on it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-leyline-evaluation-framework) <br>
- [Leyline plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline) <br>
- [Scoring Patterns](artifact/modules/scoring-patterns.md) <br>
- [Decision Thresholds](artifact/modules/decision-thresholds.md) <br>
- [Evaluation Rubric](artifact/modules/evaluation-rubric.md) <br>
- [Multi-Metric Evaluation Methodology](artifact/modules/multi-metric-evaluation-methodology.md) <br>
- [Quality Metrics](artifact/modules/quality-metrics.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with YAML, Python, shell command, and text examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only reference framework; optional measurement commands should be reviewed before use.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata; artifact frontmatter says 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
