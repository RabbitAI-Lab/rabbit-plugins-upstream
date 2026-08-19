## Description:

研发项目立项预审与提案审查，用于立项通过/否决决策、公开新颖性边界审查、创新点评估及有据可查的项目评级。

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External and internal R&D review teams use this skill to assess concrete project proposals, novelty boundaries, feasibility evidence, risks, material gaps, and pass/fail or conditional advancement recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may start a formal review workflow when a user merely provides a proposal.

Mitigation: Ask the user to confirm whether they want a review, summarization, translation, or editing before processing ambiguous proposal material.

Risk: External searches may expose sensitive project or proposal content.

Mitigation: Before searching, confirm whether external research is allowed and define the permitted source types, search scope, and redaction requirements.

Risk: Review artifacts may be written to an unintended location.

Mitigation: Confirm or create an approved writable run directory before generating reports, logs, source indexes, and claim ledgers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/rd-initiation-review-zhcn)
- [Workflow](references/workflow.md)
- [Source routing](references/source-routing.md)
- [Deliverables](references/deliverables.md)
- [Quality gates](references/quality-gates.md)
- [Evidence schema](references/evidence-schema.md)
- [Method benchmark](references/method-benchmark.md)
- [Domain playbooks](references/domain-playbooks.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Structured Markdown reports with supporting CSV evidence logs and optional docx or pdf exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces report.md, novelty-note.md, method decisions, query logs, source indexes, and claim ledgers in a writable run directory.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
