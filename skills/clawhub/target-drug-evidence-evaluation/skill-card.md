## Description:

通过多维证据矩阵评估靶点-适应症关系的遗传学、机制、临床、竞争、专利和安全性证据，支持靶点药物项目的 Go/No-Go 立项判断。

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External pharma, biotech, BD, and translational research users use this skill to evaluate a target or target-indication pair for early project triage. It produces a structured verdict, six-dimension scorecard, evidence matrix, and next actions for Go/Watch/Niche Go/No-Go decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Target, indication, drug, and patent-related queries are sent to the configured Patsnap/pharma intelligence MCP services.

Mitigation: Use only data approved for those services and avoid confidential project details unless the services are approved for that use.

Risk: The output may be mistaken for legal, investment, or clinical decision advice.

Mitigation: Treat results as evidence triage and route FTO, investment, and clinical decisions to qualified reviewers.

Risk: Missing or weak evidence can make a Go/No-Go score unreliable.

Mitigation: Require evidence sources for each score and return Insufficient Evidence when more than three dimensions lack effective data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/target-drug-evidence-evaluation)
- [MCP Tool Map](references/mcp-tool-map.md)
- [Output Templates](references/output-templates.md)
- [Scoring Rubric](references/scoring-rubric.md)

## Skill Output:

**Output Type(s):** [analysis, markdown, guidance]

**Output Format:** [Markdown with structured sections and tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Four fixed sections: Executive Verdict, Scorecard, Evidence Matrix, and Next Actions.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
