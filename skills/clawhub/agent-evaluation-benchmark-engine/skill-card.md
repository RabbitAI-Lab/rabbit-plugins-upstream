## Description:

Use when measuring OpenClaw agent quality objectively via baseline benchmarks, regression detection, golden test suites, scoring, model comparison, security evaluation, and upgrade gating before accepting changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to evaluate OpenClaw agent, skill, workflow, and system changes with baselines, golden tests, scoring rubrics, regression checks, and upgrade gates. It supports evidence-based adoption, rejection, rollback, or further testing decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Evaluation results can lead to incorrect upgrade, rollback, or deployment decisions if treated as sufficient without review.

Mitigation: Keep human review around important deployments and confirm benchmark evidence before accepting changes.

Risk: Benchmark reports may be misleading if tests are altered, regressions are ignored, or sample sizes are too small.

Mitigation: Preserve baselines, use golden tests, report failures, and require multiple relevant trials for important conclusions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/pmuhammadagus-byte/skills/agent-evaluation-benchmark-engine)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown guidance and structured evaluation report text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only guidance for benchmark plans, scoring rubrics, regression reports, and upgrade recommendations.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact/_meta.json; artifact/SKILL.md frontmatter lists 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
